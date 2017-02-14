from PyQt5 import QtCore

from src.business.configuration.constants import system as s
from src.business.consoleThreadOutput import ConsoleThreadOutput


class ConfigSystem:
    def __init__(self):
        self._settings = QtCore.QSettings()
        self.setup_settings()
        self.console = ConsoleThreadOutput()

    def setup_settings(self):
        self._settings = QtCore.QSettings(s.FILENAME, QtCore.QSettings.IniFormat)
        self._settings.setFallbacksEnabled(False)

    def save_settings(self):
        self._settings.sync()

    def set_site_settings(self, GNU_linux_startup, log_path, image_path):
        self._settings.setValue(s.STARTUP, GNU_linux_startup)
        self._settings.setValue(s.LOG_PATH, log_path)
        self._settings.setValue(s.IMAGES_PATH, image_path)

    def get_site_settings(self):
        return self._settings.value(s.STARTUP, True, type=bool), self._settings.value(s.LOG_PATH),\
               self._settings.value(s.IMAGES_PATH)

    def get_image_path(self):
        return self._settings.value(s.IMAGES_PATH)

    def get_log_path(self):
        return self._settings.value(s.LOG_PATH)

