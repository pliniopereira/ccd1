from datetime import datetime, timedelta

from src.business.configuration.settingsCamera import SettingsCamera
from src.business.consoleThreadOutput import ConsoleThreadOutput
from src.business.shooters.ContinuousShooterThread import ContinuousShooterThread
from src.business.shooters.EphemerisShooter import EphemerisShooter
from src.business.shooters.SThread import SThread
from src.controller.cameraQThread import CameraQThread
from src.controller.commons.Locker import Locker
from src.controller.fan import Fan
from src.ui.mainWindow.status import Status
from src.utils.camera.SbigDriver import (ccdinfo, set_temperature, get_temperature,
                                         establishinglink, open_deviceusb, open_driver,
                                         close_device, close_driver, getlinkstatus)
from src.utils.singleton import Singleton


class Camera(metaclass=Singleton):
    '''
        classe de controle que faz comunicao com a camera fisica.
    '''

    def __init__(self):
        self.lock = Locker()
        self.console = ConsoleThreadOutput()
        self.settings = SettingsCamera()
        self.settings.setup_settings()
        self.fan = Fan()

        # Campos da janela principal para as informações da câmera
        self.firmware_field = None
        self.model_field = None
        self.valor_pixels_x = None
        self.valor_pixels_y = None

        self.main = Status()
        self.now_plus_10 = datetime.now()
        self.settedhour = datetime.now()
        """
        executa o modo manual continuousShooterThread
        """
        self.continuousShooterThread = ContinuousShooterThread(int(self.settings.get_camera_settings()[4]))
        """
        executa o modo automatico ephemerisShooterThread
        """
        self.ephemerisShooterThread = EphemerisShooter()

        self.sthread = SThread()

        self.commands = CameraQThread(self)
        self.shooting = False
        # Initiating the Slots
        self.init_slots()

        self.info_ini = []

        info_ini = self.get_camera_settings_ini()
        self.aux_temperature = int(info_ini[0])

        self.temp = 0
        self.temp_contador = 0
        self.temp_contador_manual = 0

    def init_slots(self):
        """
        Ephemeris Shooter Slots
        """
        self.ephemerisShooterThread.started.connect(self.eshooter_started)
        self.ephemerisShooterThread.finished.connect(self.eshooter_finished)
        self.ephemerisShooterThread.signal_started_shooting.connect(self.shooter_mode)
        self.ephemerisShooterThread.signal_temp.connect(self.check_temp)
        self.ephemerisShooterThread.continuousShooterThread.signal_temp.connect(self.check_temp)

        self.ephemerisShooterThread.continuousShooterThread.started.connect(self.eshooter_observation_started)
        self.ephemerisShooterThread.continuousShooterThread.finished.connect(self.eshooter_observation_finished)
        """
        Criando connect da temperatura
        """
        # self.ephemerisShooterThread.continuousShooterThread.signalAfterShooting.connect()
        self.continuousShooterThread.signal_temp.connect(self.check_temp_manual)
        self.continuousShooterThread.finished.connect(self.standby_mode)

        # Camera Commands Slots
        self.commands.finished.connect(self.eita)
        self.commands.connectSignal.connect(self.connect_mainwindow_update)

    def get_firmware_and_model_and_pixels(self):
        info = self.get_info()
        return str(info[0]), str(info[2])[2:len(str(info[2]))-1], str(info[-2]), str(info[-1])

    def set_firmware_and_model_fields(self, firmwareField, modelField, X_Pixels, Y_Pixels):
        self.firmware_field = firmwareField
        self.model_field = modelField
        self.valor_pixels_x = X_Pixels
        self.valor_pixels_y = Y_Pixels

    def set_firmware_and_model_values(self):
        firmware, model, y_pixels, x_pixels = self.get_firmware_and_model_and_pixels()
        self.firmware_field.setText("Firmware: " + firmware)
        self.model_field.setText("Camera: " + model)
        self.valor_pixels_x.setText(x_pixels + " X " + y_pixels + " Pixels")

    def clear_firmware_and_model_values(self):
        self.firmware_field.setText("Firmware: ")
        self.model_field.setText("Camera: ")

    def get_info(self):
        '''
        Function to get the CCD Info
        This function will return [CameraFirmware, CameraType, CameraName, Pixels]
        '''
        ret = None
        self.lock.set_acquire()
        try:
            ret = tuple(ccdinfo())
        except Exception as e:
            self.console.raise_text("Failed to get camera information.\n{}".format(e))
        finally:
            self.lock.set_release()
        return ret

    def connect(self):
        try:
            a = open_driver()
            open_deviceusb()
            c = establishinglink()
            if a is True and c is True:
                self.console.raise_text("Open Device = {}".format(a), 2)
                self.console.raise_text("Established Link = {}".format(c), 2)
                self.console.raise_text("Successfully connected!", 2)
                self.set_firmware_and_model_values()

                '''
                Fan Field sera atualizado automaticamente
                atualizado pela thread de refresh temp.
                '''
                # self.fan.refresh_fan_status()
                return True
            else:
                self.console.raise_text("Connection error", 3)

        except Exception as e:
            self.console.raise_text('Failed to connect the camera!\n{}'.format(e), 3)

        return False

    def disconnect(self):
        try:
            self.standby_mode()
            cd = close_device()
            cdr = close_driver()

            if cd and cdr:
                self.console.raise_text("Close Device = {}".format(cd), 2)
                self.console.raise_text("Close Driver = {}".format(cdr), 2)
                self.console.raise_text("Successfully disconnected", 2)
                self.clear_firmware_and_model_values()
            else:
                self.console.raise_text("Error disconnect! {} {}".format(cd, cdr), 3)
        except Exception as e:
            self.console.raise_text("It failed to disconnect the camera!\n{}".format(e), 3)

    def set_temperature(self, value):
        if getlinkstatus() is True:
            self.lock.set_acquire()
            try:
                set_temperature(regulation=True, setpoint=value, autofreeze=False)
            except Exception as e:
                self.console.raise_text("Error setting the temperature.\n{}".format(e), 3)
            finally:
                self.lock.set_release()
                self.console.raise_text("Temperature set to {}°C".format(int(value)), 1)
        else:
            self.console.raise_text("The camera is not connected!", 3)

    def get_temperature(self):
        temp = "None"
        try:
            if getlinkstatus() is True:
                if not self.lock.is_locked():
                    self.lock.set_acquire()
                    temp = tuple(get_temperature())[3]
                    self.temp = temp
                    self.lock.set_release()
                else:
                    temp = "None"
            else:
                # if getlinkstatus() is True:
                #     sleep(1)
                #     self.lock.set_acquire()
                #     temp = tuple(get_temperature())[3]
                #     self.lock.set_release()
                temp = "None"
        except Exception as e:
            self.console.raise_text("Unable to retrieve the temperature.\n{}".format(e), 3)

        return temp

    def check_link(self):
        return getlinkstatus()

    def get_camera_settings_ini(self):
        settings = SettingsCamera()
        info_ini = settings.get_camera_settings()
        return info_ini

    # Camera Mode
    def standby_mode(self):
        self.set_temperature(15.00)
        self.fan.set_fan_off()

    def shooter_mode(self):
        info_ini = self.get_camera_settings_ini()
        self.aux_temperature = int(info_ini[0])
        self.set_temperature(int(self.aux_temperature))
        self.fan.set_fan_on()
        self.console.raise_text("Waiting temperature to " + str(self.aux_temperature) + "°C", 2)

    # Shooters
    def start_one_photo(self):

        try:
            self.continuousShooterThread.one_photo = True
            self.continuousShooterThread.wait_temperature = True
            self.continuousShooterThread.start_continuous_shooter()
            self.continuousShooterThread.start()
        except Exception as e:
            print(e)

    def start_taking_photo(self):
        try:
            if getlinkstatus() is True:
                self.shooter_mode()
                self.continuousShooterThread.start_continuous_shooter()
                self.continuousShooterThread.start()
            else:
                self.console.raise_text("The camera is not connected", 3)
        except Exception as e:
            print(e)

    def stop_taking_photo(self):
        if getlinkstatus() is True:
            self.continuousShooterThread.stop_continuous_shooter()
        else:
            self.console.raise_text("The camera is not connected!", 3)

    def start_ephemeris_shooter(self):
        if getlinkstatus() is True:
            self.ephemerisShooterThread.start()
        else:
            self.console.raise_text("The camera is not connected!", 3)

    def stop_ephemeris_shooter(self):
        if getlinkstatus() is True:
            self.ephemerisShooterThread.stop_shooter()
        else:
            self.console.raise_text("The camera is not connected!", 3)

    # All PyQt Slots

    def eshooter_started(self):
        self.console.raise_text("Shooter Ephemeris Started!", 1)
        self.standby_mode()

    def eshooter_finished(self):
        self.console.raise_text('Shooter finalized\n', 1)

    def eshooter_observation_started(self):
        self.shooting = True
        self.console.raise_text("Observation Started", 1)

    def eshooter_observation_finished(self):
        self.console.raise_text("Observation Finalized", 1)
        self.standby_mode()
        self.continuousShooterThread.wait_temperature = False
        self.continuousShooterThread.one_photo = False
        self.ephemerisShooterThread.wait_temperature = False
        self.ephemerisShooterThread.continuousShooterThread.wait_temperature = False
        self.temp_contador_manual = 0
        self.shooting = False

    # Commands Slots
    def check_temp_manual(self):
        '''
        funcao que espera temperatura setada ou tempo pre-determinado
        '''
        try:
            now = datetime.now()
            if self.temp_contador_manual == 0:
                self.now_plus_10 = datetime.now() + timedelta(minutes=10)
                self.temp_contador_manual += 2
            elif self.temp <= int(self.aux_temperature) or now >= self.now_plus_10:
                self.continuousShooterThread.wait_temperature = True
                self.temp_contador_manual = 0
            else:
                self.temp_contador_manual += 2

        except Exception as e:
            print(e)

    def check_temp(self):
        '''
        funcao que espera temperatura setada ou tempo pre-determinado
        '''
        try:
            now = datetime.now()
            if self.temp_contador == 0:
                self.now_plus_10 = datetime.now() + timedelta(minutes=10)
                self.temp_contador += 1
            if self.temp <= int(self.aux_temperature) or now >= self.now_plus_10:
                self.ephemerisShooterThread.wait_temperature = True
                self.ephemerisShooterThread.continuousShooterThread.wait_temperature = True

                self.temp_contador = 0
        except Exception as e:
            print(e)

    def connect_mainwindow_update(self):
        self.set_firmware_and_model_values()
        self.fan.refresh_fan_status()

    def eita(self):
        self.console.raise_text(self.commands.text, 1)
