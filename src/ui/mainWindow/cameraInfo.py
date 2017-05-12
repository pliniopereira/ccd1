from PyQt5 import QtWidgets

from src.ui.commons.layout import set_wvbox
from src.ui.mainWindow.ccdInfo import CCDInfo
from src.ui.mainWindow.fanStatus import FanStatus
from src.ui.mainWindow.tempMonitor import TempMonitor


class CameraInfo(QtWidgets.QFrame):
    def __init__(self, parent=None):
        super(CameraInfo, self).__init__(parent)

        self.ccd = CCDInfo(self)
        self.fan = FanStatus(self)
        self.temp = TempMonitor(self)
        # self.temp = None
        self.setLayout(set_wvbox(self.ccd, self.fan, self.temp))
        self.setStyleSheet("background-color: rgb(50, 50, 50); border-radius: 10px; color: white;")
