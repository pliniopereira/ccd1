import datetime
import math
import time
from datetime import timedelta

import ephem


def result():
        arq = 'H:\\Inicio_fim_OBS_SMS.txt'
        f = open(arq, 'wb')

        now_datetime = datetime.datetime.utcnow() + timedelta(minutes=1)
        now_datetime = datetime.datetime.utcnow().replace(hour=12).replace(minute=00).replace(second=0)
        # .replace(hour=19)
        # print(data)
        day = time.gmtime()
        obs = ephem.Observer()
        obs.lon = '-53.5'
        obs.lat = '-29.3'
        obs.elevation = 350
        obs.date = ephem.date(now_datetime)

        sun = ephem.Sun()
        sun.compute(obs)
        moon = ephem.Moon()
        moon.compute(obs)
        frac = moon.moon_phase
        j = 0
        d = 0
        # print(' ')
        ag_s = float(repr(sun.alt))
        s_ag = math.degrees(ag_s)
        ag_m = float(repr(moon.alt))
        m_ag = math.degrees(ag_m)
        flag = 0
        i = 0
        for d in range(1, 2):
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
                        # print('Moon Frac: ', float(frac))
                        ti = now_datetime
                        # print('Ini OBS: 1 ', now_datetime, 'Sun Elev ', sun.alt, 'Moon Elev', moon.alt)
                        # print('')
                        start = now_datetime

                        flag = 1

                elif float(s_ag) < -12.0 and float(m_ag) < 5.0 and float(frac) > 0.2:
                    if flag == 0:
                        # print('Moon Frac: ', float(frac))
                        # print('Inicio das OBS em SMS')
                        ti = now_datetime
                        # print('Ini OBS: 2 ', now_datetime, 'Sun Elev ', sun.alt, 'Moon Elev', moon.alt)
                        # print('')
                        start = now_datetime
                        flag = 1

                elif (float(s_ag) > -12.0 or float(m_ag) > 10.0) and float(frac) < 0.2 and flag == 1:
                    # print('Fim das OBS')
                    # print('Moon Frac: ', float(frac))
                    # print('End OBS: 1 ', now_datetime, 'Sun Elev ', sun.alt, 'Moon Elev', moon.alt)
                    # f.write('End OBS:  '+str(now_datetime)+ ' Sun Elev '+ str(sun.alt) +
                    # ' Moon Elev'+str(moon.alt)+'\n')
                    # f.write('End OBS:  ')
                    flag = 0
                    # print('Time   : ', now_datetime-ti, 'Hours')
                    # print('-------------------------------------------------------------')
                    # print(i)
                    end = now_datetime

                    break

                elif (float(s_ag) > -12.0 or float(m_ag) > 5.0) and float(frac) > 0.2 and flag == 1:
                    # print('Fim das OBS')
                    # print('Moon Frac: ', float(frac))
                    # print('End OBS: 2 ', now_datetime, 'Sun Elev ', sun.alt, 'Moon Elev', moon.alt)
                    # f.write('End OBS:  '+str(now_datetime)+ ' Sun Elev '+ str(sun.alt) +
                    #  ' Moon Elev'+str(moon.alt)+'\n')
                    # f.write('End OBS:  ')
                    flag = 0
                    # print('Time   : ', now_datetime-ti, 'Hours')
                    # print('-------------------------------------------------------------')
                    # print(i)
                    end = now_datetime

                    break

                now_datetime = datetime.datetime.utcnow().replace(hour=12).replace(minute=00).replace(second=0)+timedelta(minutes=j)
                # now_datetime = datetime.datetime.utcnow()+timedelta(minutes=j)
                j = j+1

            # now_datetime = datetime.datetime.utcnow()+timedelta(days=d)
            now_datetime = datetime.datetime.utcnow().replace(hour=12).replace(minute=00).replace(second=0)+timedelta(days=d)

            # print('')

            # print(now_datetime)
            # print(d)

        return start, end
