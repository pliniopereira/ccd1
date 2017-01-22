from PyQt5 import QtWidgets

from src.business.configuration.configProject import ConfigProject
from src.business.configuration.configSystem import ConfigSystem as cs
from src.ui.commons.layout import set_wvbox
from src.ui.mainWindow.ephemInfo import EphemInfo
from src.ui.mainWindow.siteInfo import SiteInfo


class ConfigsInfo(QtWidgets.QFrame):
    def __init__(self, parent=None):
        super(ConfigsInfo, self).__init__(parent)

        # Initing Widgets
        p = cs()
        self.confs = ConfigProject()

        # Init Widget Site Info
        infoSite = self.confs.get_site_settings()
        infoGeo = self.confs.get_geographic_settings()
        self.site = SiteInfo(infoSite[1], infoSite[2], infoGeo[0], infoGeo[1], infoGeo[2], infoGeo[3])

        infoMoon = self.confs.get_moonsun_settings()
        self.moon = EphemInfo(infoMoon[0], infoMoon[2], infoMoon[3])

        self.set_layout()

    def set_layout(self):
        self.setLayout(set_wvbox(self.site, self.moon))

