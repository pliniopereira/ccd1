import ephem


class EphemObserverFactory:
    def __init__(self):
        pass

    def create_observer(self, longitude=None, latitude=None, elevation=None):
        try:
            o = ephem.Observer()
            o.lon = longitude
            o.lat = latitude
            o.elevation = float(elevation)
        except Exception as e:
            print(e)
            o.lon = 0
            o.lat = 0
            o.elevation = 0
        return o

    def set_observer_parameters(self, observer, obsLongitude, obsLatitude, obsElevation):
        try:
            observer.lon = obsLongitude
            observer.lat = obsLatitude
            observer.elevation = float(obsElevation)
        except Exception as e:
            print(e)
            observer.lon = 0
            observer.lat = 0
            observer.elevation = 0