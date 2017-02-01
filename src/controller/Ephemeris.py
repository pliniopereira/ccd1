import datetime
import sys
from math import degrees
from threading import Thread
from time import sleep

import ephem

from src.business.configuration.configProject import ConfigProject


class Ephemeris:
    def __init__(self):
        self.config = ConfigProject()
        info = self.config.get_geographic_settings()
        self.latitude = info[0] #'-45.51'
        self.longitude = info[1] #'-23.12'
        self.elev = info[2] #350
        self.shootOn = False

        t = Thread(target=self.check_all)
        t.start()

    def refresh_data(self):
        info = self.config.get_geographic_settings()
        self.latitude = info[0]  # '-45.51'
        self.longitude = info[1]  # '-23.12'
        self.elev = info[2]  # 350

    def print_time_elapsed(self):
        init_time = datetime.datetime.utcnow()

        while True:
            now_datetime = datetime.datetime.utcnow()
            sys.stdout.write("\r Time elapsed from init: {}".format(now_datetime - init_time))
            sys.stdout.flush()
            sleep(1)

    def check_all(self):
        log = open('logging.txt', 'a')

        tTime = Thread(target=self.print_time_elapsed)
        tTime.start()

        try:
            while True:
                now_datetime = datetime.datetime.utcnow()
                obs = ephem.Observer()
                obs.lon = self.longitude
                obs.lat = self.latitude
                obs.elevation = self.elev
                obs.date = ephem.date(now_datetime)

                sun = ephem.Sun()
                sun.compute(obs)

                moon = ephem.Moon()
                moon.compute(obs)
                frac = moon.moon_phase

                a = ephem.degrees(str(sun.alt))
                b = ephem.degrees(str(moon.alt))
                if degrees(a) < -12 and degrees(b) < 10:
                    self.shootOn = True
                else:
                    self.shootOn = False

                # Creating a log
                log.write("{} - {} - ".format(self.shootOn, now_datetime))
                log.write("Sun: {:.4f}  Moon: {:.4f}\n".format(degrees(a), degrees(b)))

                # Printing on the stdout
                # sys.stdout.write("\rShooting: {}".format(str(self.shootOn)))
                # sys.stdout.flush()
                sleep(60)
        except Exception as e:
            print(e)
            log.close()

    '''
        print('Sun Elev: {}'.format(degrees(a)))
        print('Moon Elev: {}'.format(degrees(b)))
        print('Moon ilumi: %f' %round(frac*100,1))
        print('Sun next rising %s\r' %obs.next_rising(sun))
        print('Sun next setting %s\r' %obs.next_setting(sun))
        print('Moon next rising %s\r' %obs.next_rising(moon))
        print('Moon next setting %s' %obs.next_setting(moon))
        print('%s\r' %str(sun.alt)),
        print('%s\r' %str(moon.alt)),
        print('%s\r' %str(obs.date)),
        sys.stdout.flush()
    '''

if __name__ == '__main__':
    a = Ephemeris()
