from PyQt5 import QtWidgets

from src.business.consoleThreadOutput import ConsoleThreadOutput
from src.ui.commons.layout import add_all_to_vbox, set_wvbox
from src.ui.mainWindow.Shooter import Shooter
from src.ui.mainWindow.StartEndEphem import StartEndEphem
from src.ui.mainWindow.cameraInfo import CameraInfo
from src.ui.mainWindow.clock import Clock
from src.ui.mainWindow.configsInfo import ConfigsInfo
from src.ui.mainWindow.consoleLogWidget import ConsoleLogWidget


class MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        # Init the Layouts
        self.MainHBox = QtWidgets.QHBoxLayout()   # Main Box
        self.VBox = QtWidgets.QVBoxLayout()   # Vertical Box in the Left Box
        self.all_h_boxes = []
        self.console = ConsoleThreadOutput()
        self.console.set_widget_console(ConsoleLogWidget(self))

        self.MainHBox.addLayout(self.VBox)
        self.MainHBox.addStretch(1)
        self.MainHBox.addLayout(set_wvbox(self.console.get_widget_console(), Shooter(self)))

        add_all_to_vbox(self.VBox, Clock(self), ConfigsInfo(self), StartEndEphem(self), CameraInfo(self))
        self.VBox.addStretch(1)

        self.setLayout(self.MainHBox)
