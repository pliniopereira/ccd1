from PyQt5 import QtCore
from PyQt5 import QtWidgets

from src.business.schedulers.schedClock import SchedClock
from src.ui.commons.layout import set_wvbox
from src.ui.commons.widgets import get_qfont


class Clock(QtWidgets.QFrame):
    
    def __init__(self, parent=None):
        super(Clock, self).__init__(parent)
        self.title = QtWidgets.QLabel('Universal Time Coordinated', self)

        self.lcd = QtWidgets.QLabel(self)
        self.sc = SchedClock(lcd_display=self.lcd)

        self.init_ui()
        self.config_widgets()

        self.setLayout(set_wvbox(self.title, self.lcd))
        self.setStyleSheet("background-color: rgb(50, 50, 50); border-radius: 10px; color: white;")

    def init_ui(self):
        self.sc.start_scheduler()

    def config_widgets(self):
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.lcd.setAlignment(QtCore.Qt.AlignCenter)

        self.title.setFont(get_qfont(True))
        self.lcd.setFont(get_qfont(False))

