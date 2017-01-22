from PyQt5 import QtCore
from PyQt5 import QtWidgets

from src.ui.commons.layout import set_lvbox, set_hbox
from src.ui.commons.widgets import get_qfont


class SiteInfo(QtWidgets.QFrame):
    def __init__(self, sitename, imagername, lat, long, elev, press, parent=None):
        super(SiteInfo, self).__init__(parent)

        # Init Widgets
        self.init_site_widgets(sitename, imagername)
        self.init_geo_widgets(lat, long, elev, press)
        self.config_widget()

        self.make_layout()

    def init_site_widgets(self, sitename, imagername):
        self.title = QtWidgets.QLabel("Site Information", self)
        self.site = QtWidgets.QLabel("Site Name:", self)
        self.imager = QtWidgets.QLabel("Label Name:", self)
        self.siter = QtWidgets.QLabel(str(sitename), self)
        self.imagerr = QtWidgets.QLabel(str(imagername), self)

    def init_geo_widgets(self, lat, long, elev, press):
        self.lat = QtWidgets.QLabel("Latitude:", self)
        self.long = QtWidgets.QLabel("Longitude:", self)
        self.elev = QtWidgets.QLabel("Elevation:", self)
        self.press = QtWidgets.QLabel("Pressure:", self)

        self.latr = QtWidgets.QLabel(str(lat) + "º", self)
        self.longr = QtWidgets.QLabel(str(long) + "º", self)
        self.elevr = QtWidgets.QLabel(str(elev) + "m", self)
        self.pressr = QtWidgets.QLabel(str(press) + "mb", self)

    def set_site_values(self, sitename, imagername):
        self.siter.setText(sitename)
        self.imagerr.setText(imagername)

    def set_geo_values(self, lat, lon, ele, pre):
        self.latr.setText(lat)
        self.longr.setText(lon)
        self.elevr.setText(ele)
        self.pressr.setText(pre)

    def make_layout(self):
        self.setLayout(set_lvbox(set_hbox(self.title),
                                 set_hbox(self.site, self.siter),
                                 set_hbox(self.imager, self.imagerr),
                                 set_hbox(self.lat, self.latr),
                                 set_hbox(self.long, self.longr),
                                 set_hbox(self.elev, self.elevr),
                                 set_hbox(self.press, self.pressr)))

    def config_widget(self):
        self.title.setFont(get_qfont(True))
        self.title.setAlignment(QtCore.Qt.AlignCenter)

        self.setStyleSheet("background-color: rgb(50, 50, 50); border-radius: 10px; color: white;")
