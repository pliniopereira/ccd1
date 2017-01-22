import math
import time
from datetime import datetime

import ephem
from PyQt5 import QtCore

from src.business.EphemObserverFactory import EphemObserverFactory
from src.business.configuration.configProject import ConfigProject


class QThreadSunMoon(QtCore.QThread):
    signal_update_sun_moon = QtCore.pyqtSignal([list], name="signalUpdateSunMoon")

    def __init__(self):
        super(QThreadSunMoon, self).__init__()
        self.eof = EphemObserverFactory()
        self.latitude = None
        self.longitude = None
        self.elevation = None
        self.config = None

        self.obs = None

    def get_info(self):
        # Criando uma instância do ConfigProject
        self.config = ConfigProject()

        # Recebendo as informações
        info = self.config.get_geographic_settings()

        # Atribuindo valor as variáveis de geolocalização
        self.latitude = info[0]  # '-45.51'
        self.longitude = info[1]  # '-23.12'
        self.elevation = info[2]  # 350

    def set_observer(self, longitude, latitude, elevation):
        """ Essa função cria um Observatório do PyEphem para utilizar nos cálculos """
        self.obs = self.eof.create_observer(longitude=longitude,
                                            latitude=latitude,
                                            elevation=elevation)

    def run(self):
        # Pegando as informações
        self.get_info()

        # Criando um Observatório
        self.set_observer(self.longitude, self.latitude, self.elevation)

        while True:
            now_datetime = datetime.utcnow()
            self.obs.date = ephem.date(now_datetime)

            sun = ephem.Sun(self.obs)

            moon = ephem.Moon(self.obs)
            frac = moon.moon_phase

            sun_alt = ephem.degrees(sun.alt)
            moon_alt = ephem.degrees(moon.alt)

            sun_elevation = "{:.2f}º".format(float(math.degrees(sun_alt)))
            moon_elevation = "{:.2f}º".format(float(math.degrees(moon_alt)))
            moon_phase = "{0:.2f}%".format(frac * 100)

            self.signal_update_sun_moon.emit([sun_elevation, moon_elevation, moon_phase])
            time.sleep(1)
