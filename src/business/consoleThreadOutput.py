from src.business.logger import Logger
from src.utils.singleton import Singleton


class ConsoleThreadOutput(metaclass=Singleton):
    def __init__(self):
        self.logger = Logger()

    def get_widget_console(self):
        return self.log

    def set_widget_console(self, c):
        self.log = c

    def raise_text(self, text, level=0):
        self.log.newLine(text, level)
        self.save_log(text)
        print(text)

    def save_log(self, text):
        self.logger.set_text(text)
        self.logger.start()
