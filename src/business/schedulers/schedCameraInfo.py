import time

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger

from src.utils.singleton import Singleton


class SchedClock(metaclass=Singleton):
    def __init__(self, lcd_display):
        self.lcd = lcd_display

    def start_scheduler(self):
        scheduler = BackgroundScheduler()
        scheduler.add_job(self.refresh, IntervalTrigger(seconds=1))
        scheduler.start()

    def refresh(self):
        self.lcd.setText(time.strftime('%H:%M:%S'))
