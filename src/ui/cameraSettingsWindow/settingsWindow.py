from PyQt5 import QtWidgets

from src.business.configuration.settingsCamera import SettingsCamera
from src.business.consoleThreadOutput import ConsoleThreadOutput
from src.business.shooters.SThread import SThread
from src.controller.camera import Camera
from src.controller.fan import Fan
from src.ui.commons.layout import set_lvbox, set_hbox
from src.utils.camera.SbigDriver import (getlinkstatus)


class SettingsWindow(QtWidgets.QWidget):
    '''
    Cria os campos e espaços no menu settings window
    '''
    def __init__(self, parent=None):
        super(SettingsWindow, self).__init__(parent)
        self.cam = SettingsCamera()
        self.camera = Camera()
        self.console = ConsoleThreadOutput()
        #self.a_temp_regulation = TempRegulation(self)
        self.create_cam_widgets()
        self.p = parent
        self.fan = Fan(self.fanButton)

        #self.button_clear = QtWidgets.QPushButton('Clear', self)

        self.setField_temperature = QtWidgets.QLineEdit(self)
        self.setting_values()

        self.one_photo = SThread()

        self.setLayout(set_lvbox(set_hbox(self.setField_temperature_label, self.setField_temperature),
                                 set_hbox(self.pre, self.prel),
                                 set_hbox(self.exp, self.expl),
                                 set_hbox(self.binning, self.combo),
                                 set_hbox(self.tempo_fotos_label, self.tempo_fotos),
                                 set_hbox(self.time_colling_label, self.time_colling),
                                 set_hbox(self.dark, self.close_open),
                                 set_hbox(self.getlevel1, self.getlevel1l),
                                 set_hbox(self.getlevel2, self.getlevel2l),
                                 set_hbox(self.btn_one_photo, self.tempButton, self.fanButton, stretch2=1),
                                 set_hbox(self.buttonok, self.button_clear, self.buttoncancel, stretch2=1)))

    def get_camera_settings(self):
        settings = SettingsCamera()
        info = settings.get_camera_settings()
        return info

    def get_values(self):
        return self.cam.get_camera_settings()

    def setting_values(self):
        info = self.get_values()
        self.set_values(info[0], info[1], info[2], info[3], info[4], info[5], info[6], info[7], info[8])

    def set_values(self, temperature_camera, prefixo, exposicao, binning, tempo_entre_fotos, time_colling, get_level1, get_level2, dark_photo):
        self.setField_temperature.setText(temperature_camera)
        self.prel.setText(prefixo)
        self.expl.setText(exposicao)

        try:
            b = int(binning)
        except:
            b = 0
        try:
            open_or_close = int(dark_photo)
        except:
            open_or_close = 0
        self.tempo_fotos.setText(tempo_entre_fotos)
        self.time_colling.setText(time_colling)
        self.combo.setCurrentIndex(b)
        self.close_open.setCurrentIndex(open_or_close)
        self.getlevel1l.setText(get_level1)
        self.getlevel2l.setText(get_level2)

    def create_cam_widgets(self):
        self.setField_temperature_label = QtWidgets.QLabel("Temperature(°C):", self)
        self.pre = QtWidgets.QLabel("Filter name:", self)
        self.prel = QtWidgets.QLineEdit(self)

        self.exp = QtWidgets.QLabel("Exposure time(s):", self)
        self.expl = QtWidgets.QLineEdit(self)

        self.binning = QtWidgets.QLabel("Binning:", self)
        self.combo = QtWidgets.QComboBox(self)
        self.fill_combo()

        self.dark = QtWidgets.QLabel("Shooter:", self)
        self.close_open = QtWidgets.QComboBox(self)
        self.fill_combo_close_open()

        self.getlevel1 = QtWidgets.QLabel("Image contrast: bottom level:", self)
        self.getlevel1l = QtWidgets.QLineEdit(self)

        self.getlevel2 = QtWidgets.QLabel("Image contrast:       top level:", self)
        self.getlevel2l = QtWidgets.QLineEdit(self)

        self.button_clear = QtWidgets.QPushButton('Clear', self)
        self.button_clear.clicked.connect(self.clear_all)

        self.btn_one_photo = QtWidgets.QPushButton('Take Photo', self)
        self.btn_one_photo.clicked.connect(self.camera.start_one_photo)

        self.tempButton = QtWidgets.QPushButton("Set Temp", self)
        self.tempButton.clicked.connect(self.btn_temperature)

        self.fanButton = QtWidgets.QPushButton("Fan (On/Off)")
        self.fanButton.clicked.connect(self.button_fan_func)

        self.buttonok = QtWidgets.QPushButton("Save", self)
        self.buttonok.clicked.connect(self.button_ok_func)

        self.buttoncancel = QtWidgets.QPushButton("Cancel", self)
        self.buttoncancel.clicked.connect(self.func_cancel)

        self.tempo_fotos_label = QtWidgets.QLabel("Time between photo(s):", self)
        self.tempo_fotos = QtWidgets.QLineEdit(self)

        self.time_colling_label = QtWidgets.QLabel("CCD Cooling Time:", self)
        self.time_colling = QtWidgets.QLineEdit(self)

    def button_ok_func(self):
        try:
            # Saving the Settings
            self.cam.set_camera_settings(self.setField_temperature.text(), self.prel.text(), self.expl.text(),\
                                         self.combo.currentIndex(), self.tempo_fotos.text(), self.time_colling.text(), \
                                         self.getlevel1l.text(), self.getlevel2l.text(), self.close_open.currentIndex())
            self.cam.save_settings()
            self.console.raise_text("Camera settings successfully saved!", 1)
        except Exception as e:
            self.console.raise_text("Camera settings were not saved.", 3)
        finally:
            pass
            #self.p.close()

    def clear_all(self):
        self.setField_temperature.clear()
        self.prel.clear()
        self.expl.clear()
        self.tempo_fotos.clear()

    def take_one_photo(self):
        try:
            info = self.get_camera_settings()
            if int(info[8]) == 1:
                self.console.raise_text("Taking dark photo", 1)
                self.one_photo.start()
            else:
                self.console.raise_text("Taking photo", 1)
                self.one_photo.start()
        except Exception:
            self.console.raise_text("Not possible taking photo", 1)

    def func_cancel(self):
        self.p.close()

    def button_fan_func(self):
        if getlinkstatus() is True:
            try:
                self.fan.set_fan()
                self.console.raise_text('State changed Fan!', 2)
            except Exception:
                self.console.raise_text("The camera is not connected!", 3)
                self.console.raise_text('State Fan unchanged', 3)
        else:
            self.console.raise_text("The camera is not connected!", 3)
            self.console.raise_text('State Fan unchanged', 3)

    def fill_combo(self):
        self.combo.addItem("1x1", 0)
        self.combo.addItem("2x2", 1)
        self.combo.addItem("3x3", 2)

    def fill_combo_close_open(self):
        self.close_open.addItem("Open", 0)
        self.close_open.addItem("Close", 1)

    def btn_temperature(self):
            try:
                value = self.setField_temperature.text()
                if value is '':
                    pass
                else:
                    self.camera.set_temperature(float(value))
            except Exception as e:
                print("Exception -> {}".format(e))
