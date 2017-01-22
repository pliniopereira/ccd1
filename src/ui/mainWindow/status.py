from src.utils.singleton import Singleton


class Status(metaclass=Singleton):
    _mainwindow = None

    def __init__(self, parent=None):
        self._mainwindow = parent

    def set_status(self, message):
        self._mainwindow.statusBar().showMessage(message)

    def clear_status(self):
        self._mainwindow.statusBar().clearMessage()
