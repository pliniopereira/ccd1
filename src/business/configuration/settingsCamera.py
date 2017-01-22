from PyQt5 import QtCore

from src.business.configuration.constants import camera as c


class SettingsCamera:
    def __init__(self):
        self._settings = QtCore.QSettings()
        self.setup_settings()

    def setup_settings(self):
        self._settings = QtCore.QSettings(c.FILENAME, QtCore.QSettings.IniFormat)
        self._settings.setFallbacksEnabled(False)

    def save_settings(self):
        self._settings.sync()

    def set_camera_settings(self, temperature_camera, pre, exp, bin, time, time_cooling, get_level1,\
                            get_level2, dark_photo):
        self._settings.setValue(c.TEMPERATURE, temperature_camera)
        self._settings.setValue(c.PREFIXO, pre)
        self._settings.setValue(c.EXPOSICAO, exp)
        self._settings.setValue(c.BINNING, bin)
        self._settings.setValue(c.TIMEPHOTO, time)
        self._settings.setValue(c.TIMECOOLING, time_cooling)
        self._settings.setValue(c.GET_LEVEL1, get_level1)
        self._settings.setValue(c.GET_LEVEL2, get_level2)
        self._settings.setValue(c.DARK_PHOTO, dark_photo)


    def get_camera_settings(self):
        return self._settings.value(c.TEMPERATURE), self._settings.value(c.PREFIXO), self._settings.value(c.EXPOSICAO),\
               self._settings.value(c.BINNING), self._settings.value(c.TIMEPHOTO), self._settings.value(c.TIMECOOLING), \
               self._settings.value(c.GET_LEVEL1), self._settings.value(c.GET_LEVEL2), self._settings.value(c.DARK_PHOTO)

    def get_filepath(self):
        return self._settings.value(c.FILENAME)
