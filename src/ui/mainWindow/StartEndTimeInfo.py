import datetime
import math
from datetime import timedelta

import ephem

from src.business.configuration.configProject import ConfigProject


def result():
        config = ConfigProject()

        info = config.get_geographic_settings()
        infosun = config.get_moonsun_settings()

        max_solar_elevation = infosun[0]  # -12
        max_lunar_elevation = infosun[2]  # 8
        max_lunar_phase = infosun[3]  # 1

        now_datetime = datetime.datetime.utcnow().replace(hour=12).replace(minute=00).replace(second=0)
        obs = ephem.Observer()

        obs.lat = info[0]
        obs.lon = info[1]
        obs.elevation = float(info[2])
        obs.date = ephem.date(now_datetime)

        sun = ephem.Sun()
        sun.compute(obs)
        moon = ephem.Moon()
        moon.compute(obs)
        j = 0
        flag = 0
        for i in range(1, 3000):

            obs.date = ephem.date(now_datetime)
            sun = ephem.Sun()
            sun.compute(obs)

            moon = ephem.Moon()
            moon.compute(obs)
            frac = moon.moon_phase

            ag_s = float(repr(sun.alt))
            s_ag = math.degrees(ag_s)
            ag_m = float(repr(moon.alt))
            m_ag = math.degrees(ag_m)

            if float(s_ag) < -12.0 and float(m_ag) < 10.0 and float(frac) < 0.2:

                if flag == 0:
                    start = now_datetime
                    flag = 1

            elif float(s_ag) < -12.0 and float(m_ag) < 5.0 and float(frac) > 0.2:
                if flag == 0:
                    start = now_datetime
                    flag = 1

            elif (float(s_ag) > -12.0 or float(m_ag) > 10.0) and float(frac) < 0.2 and flag == 1:
                end = now_datetime
                break

            elif (float(s_ag) > -12.0 or float(m_ag) > 5.0) and float(frac) > 0.2 and flag == 1:
                end = now_datetime
                break

            # now_datetime = datetime.datetime.utcnow().replace(hour=12).replace(minute=00).replace(second=0) \
            #                + timedelta(minutes=j)
            now_datetime += timedelta(minutes=j)

            j += 1

        obs_time = end - start

        print(start)
        print(end)

        return start, end, obs_time
