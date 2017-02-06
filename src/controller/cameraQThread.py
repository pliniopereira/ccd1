from PyQt5 import QtCore

from src.controller.commons import cameraActions as cam
from src.controller.commons.Locker import Locker
from src.controller.fan import Fan
from src.utils.camera.SbigDriver import (establishinglink, open_deviceusb, open_driver)


class CameraQThread(QtCore.QThread):
    """
    Threads são fluxos de programas que executam em paralelo dentro de uma aplicação, isto é,\
    uma ramificação de uma parte da aplicação que é executada de forma independente e\
    escalonada independentemente do fluxo inicial da aplicação.
    Fonte: http://imasters.com.br/artigo/20127/py/threads-em-python/?trace=1519021197&source=single
    Essa thread controla a camera
    """
    connectSignal = QtCore.pyqtSignal()
    disconnectSignal = QtCore.pyqtSignal()
    fanOnSignal = QtCore.pyqtSignal()
    fanOffSignal = QtCore.pyqtSignal()

    def __init__(self, parent):
        super(CameraQThread, self).__init__()
        self.fan = Fan()
        self.lock = Locker()
        self.parent = parent
        self.conditional = None
        self.text = None

    def set_conditional(self, conditional):
        self.conditional = conditional

    def set_text(self, text):
        self.text = text

    def run(self):
        try:
            if self.conditional == cam.CONNECT:
                self.camera_connect()
                self.connectSignal.emit()
            elif self.conditional == cam.DISCONNECT:
                self.disconnectSignal.emit()
            elif self.conditional == cam.FAN_ON:
                self.fanOnSignal.emit()
            elif self.conditional == cam.FAN_OFF:
                self.fanOffSignal.emit()
            else:
                print('Nothing')
        except Exception as e:
            print(e)
        finally:
            self.conditional = None

    def camera_connect(self):
        try:
            self.lock.set_acquire()
            a = open_driver()
            open_deviceusb()
            c = establishinglink()
            if a is True and c is True:
                self.text = "Successfully connected! {} {}".format(a, c)
            else:
                self.text = "Error in connection"
        except Exception as e:
            self.text = 'Failed to connect to camera!\n{}'.format(e)
        finally:
            self.lock.set_release()
