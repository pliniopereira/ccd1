from src.business.consoleThreadOutput import ConsoleThreadOutput
from src.business.schedulers.qthreadTemperature import QThreadTemperature
from src.utils.singleton import Singleton


class SchedTemperature(metaclass=Singleton):

    def __init__(self, valor=None):

        self.console = ConsoleThreadOutput()

        self.object = valor

        self.stemp = QThreadTemperature()
        self.stemp.temp_signal.connect(self.refresh_temp)
        self.stemp.start()

    def refresh_temp(self, value):
        self.object.setText(value)
