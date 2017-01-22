from PyQt5 import QtWidgets

from src.ui.ephemerisShooterWindow.ephemerisShooterWindow import EphemerisShooterWindow


class Main(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)

        self.a = EphemerisShooterWindow(self)
        self.setCentralWidget(self.a)

        self.setWindowTitle("Ephemeris Shooter")
