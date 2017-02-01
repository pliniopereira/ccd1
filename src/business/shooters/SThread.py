import time

from PyQt5 import QtCore

from src.business.configuration.settingsCamera import SettingsCamera
from src.business.models.image import Image
from src.controller.commons.Locker import Locker
from src.utils.camera import SbigDriver


class SThread(QtCore.QThread):
    '''
    Roda em paralelo, manda tirar as fotos.
    '''

    def __init__(self):
        super(SThread, self).__init__()
        self.lock = Locker()
        self.info = []
        self.img = None
        self.generic_count = 0

    def get_camera_settings(self):
        '''
        pega os valores no ini camera
        info[0] = temperature_camera
        info[1] = prefixo/filter name
        info[2] = tempo_exposicao
        info[3] = tempo_fotos(tempo entre fotos)
        info[4] = time_cooling(CCD cooling time)
        info[5] = Image contrast: bottom
        info[6] = Image contrast: top level
        info[7] = Booleano para decidir se a foto é dark
        '''
        settings = SettingsCamera()
        info = settings.get_camera_settings()
        return info

    def take_dark(self):
        '''
        Manda instrução para o SbigDriver para tirar uma foto dark(shooter fechado)\
        com os valores na info[]
        '''
        try:
            self.set_etime_pre_binning()
            self.lock.set_acquire()
            self.info = SbigDriver.photoshoot(self.etime, self.pre, self.b, 1, self.get_level1, self.get_level2)
            self.init_image()
        except Exception as e:
            print(e)
        finally:
            time.sleep(1)
            self.lock.set_release()

    def set_etime_pre_binning(self):
        '''
        seta os valores para o tempo de exposição = etime, prefixo, binning, se a foto é dark ou não,\
        e valores Image contrast: bottom e top level
        '''

        try:
            info = self.get_camera_settings()

            self.get_level1 = float(info[6])
            self.get_level2 = float(info[7])

            self.etime = float(info[2])
            if self.etime <= 0.12:
                self.etime = 0.12 * 100
            elif self.etime >= 3600:
                self.etime = 3600 * 100
            else:
                self.etime = float(info[2]) * 100
            self.etime = int(self.etime)

            self.pre = str(info[1])

            self.b = int(info[3])

            self.dark_photo = int(info[8])

        except Exception as e:
            print(e)
            self.etime = 100
            self.dark_photo = 1
            self.get_level1 = 0.1
            self.get_level2 = 0.99
            if str(info[1]) != '':
                self.pre = str(info[1])
            else:
                self.pre = 'pre'

    def run(self):
        self.set_etime_pre_binning()
        self.lock.set_acquire()
        try:
            self.info = SbigDriver.photoshoot(self.etime, self.pre, self.b, self.dark_photo, self.get_level1,\
                                              self.get_level2)
            self.init_image()
        except Exception as e:
            print(e)
        finally:
            self.lock.set_release()

    def init_image(self):
        try:
            for i in self.info:
                print(i)

            self.img = Image(self.info[0], self.info[1], self.info[2], self.info[3], self.info[4])
        except Exception as e:
            self.img = Image('','','','','')
        return self.img

    def get_image_info(self):
        return self.img
