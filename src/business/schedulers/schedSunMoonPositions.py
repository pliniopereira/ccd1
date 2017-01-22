from src.business.consoleThreadOutput import ConsoleThreadOutput
from src.business.schedulers.qthreadSunMoon import QThreadSunMoon
from src.utils.singleton import Singleton


class SchedSunMoonPositions(metaclass=Singleton):

    def __init__(self, sunElevationField, moonElevationField, moonPhaseField):
        self.sunElevationField = sunElevationField
        self.moonElevationField = moonElevationField
        self.moonPhaseField = moonPhaseField
        self.console = ConsoleThreadOutput()
        self.thread_sun_moon = QThreadSunMoon()
        self.thread_sun_moon.signal_update_sun_moon.connect(self.refresh_info)

        self.thread_sun_moon.start()


    def refresh_info(self, info):
        try:
            self.sunElevationField.setText(info[0])
            self.moonElevationField.setText(info[1])
            self.moonPhaseField.setText(info[2])
        except Exception as e:
            self.console.raise_text("Error sun and moon Scheduler\n{}".format(e))

