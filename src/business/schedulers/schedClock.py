from src.business.schedulers.qthreadClock import QThreadClock
from src.utils.singleton import Singleton


class SchedClock(metaclass=Singleton):
    def __init__(self, lcd_display):
        self.lcd = lcd_display
        self.threadClock = QThreadClock()
        self.threadClock.time_signal.connect(self.refresh)

    def start_scheduler(self):
        self.threadClock.start()

    # Refreshing Clock
    def refresh(self, value):
        self.lcd.setText(value)
