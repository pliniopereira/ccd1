from PyQt5 import QtWidgets

from src.ui.cameraSettingsWindow.settingsWindow import SettingsWindow


class Main(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)

        self.a = SettingsWindow(self)
        self.setCentralWidget(self.a)

        self.setWindowTitle("Camera Settings")
