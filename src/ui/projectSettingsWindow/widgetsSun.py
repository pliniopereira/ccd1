from PyQt5 import QtCore
from PyQt5 import QtWidgets

from src.ui.commons.layout import set_hbox, set_lvbox


class WidgetsSun(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(WidgetsSun, self).__init__(parent)

        # Creating Labels
        self.lmse = QtWidgets.QLabel("Max Solar Elevation (º):", self)
        self.lmse.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        self.lmle = QtWidgets.QLabel("Max Lunar Elevation (º):", self)
        self.lmle.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        self.lmlp = QtWidgets.QLabel("Max Lunar Phase (%):", self)
        self.lmlp.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)


        # Creating Input Line
        self.emse = QtWidgets.QLineEdit(self)
        self.emse.setMaximumWidth(100)

        self.ignore_lunar_position_label = QtWidgets.QLabel("    Ignore Lunar Position:", self)
        self.ignore_lunar_position_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.eilp = QtWidgets.QCheckBox()

        self.emle = QtWidgets.QLineEdit(self)
        self.emle.setMaximumWidth(100)

        self.emlp = QtWidgets.QLineEdit(self)
        self.emlp.setMaximumWidth(100)

        self.setting_up()

    def setting_up(self):
        vbox = set_lvbox(set_hbox(self.lmse, self.emse),
                         set_hbox(self.ignore_lunar_position_label, self.eilp),
                         set_hbox(self.lmle, self.emle),
                         set_hbox(self.lmlp, self.emlp))

        self.setLayout(vbox)

    def get_sun(self):
        return self.emse.text(), self.eilp.isChecked(), self.emle.text(), self.emlp.text()

    def set_sun(self, mse, ilp, mle, mlp):
        self.emse.setText(mse)
        self.eilp.setChecked(ilp)
        self.emle.setText(mle)
        self.emlp.setText(mlp)

    def clear_sun(self):
        self.emse.clear()
        self.eilp.setChecked(False)
        self.emle.clear()
        self.emlp.clear()
