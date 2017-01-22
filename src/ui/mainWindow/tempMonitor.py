from PyQt5 import QtWidgets

from src.business.schedulers.SchedTemperature import SchedTemperature
from src.ui.commons.layout import set_hbox


class TempMonitor(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(TempMonitor, self).__init__(parent)
        self.tempMonitor = QtWidgets.QLabel(self)
        self.Sched = SchedTemperature(self.tempMonitor)

        self.label = QtWidgets.QLabel("Temperature:", self)

        self.setLayout(set_hbox(self.label, self.tempMonitor, stretch=1))

    def stop_monitor(self):
        self.Sched.stop_job()

    def start_monitor(self):
        self.Sched.start_job()
