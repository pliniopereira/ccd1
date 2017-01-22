from PyQt5 import QtCore
from PyQt5 import QtWidgets

from src.controller.fan import Fan
from src.ui.commons.layout import set_hbox
from src.ui.mainWindow.status import Status


class FanStatus(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(FanStatus, self).__init__(parent)

        self.status = Status()

        # Creating the Widgets
        self.FanField = QtWidgets.QLabel(self)
        self.FanLabel = QtWidgets.QLabel("Fan: ", self)

        # Creating a Fan Object
        self.fan = Fan()
        self.fan.set_fanField(self.FanField)

        # Setting up
        self.setting_up()

        # Set up the layout
        self.setLayout(set_hbox(self.FanLabel, self.FanField))

    def setting_up(self):
        self.FanField.setAlignment(QtCore.Qt.AlignCenter)

        self.FanField.setText(self.fan.fan_status())
