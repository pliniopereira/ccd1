from PyQt5 import QtWidgets

from src.ui.commons.layout import set_hbox, set_lvbox


class WidgetsSun(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(WidgetsSun, self).__init__(parent)

        # Creating Labels
        self.lmse = QtWidgets.QLabel("Max Solar Elevation (º):", self)
        self.lmle = QtWidgets.QLabel("Max Lunar Elevation (º):", self)
        self.lmlp = QtWidgets.QLabel("Max Lunar Phase (%):", self)

        # Creating Input Line
        self.emse = QtWidgets.QLineEdit(self)
        self.eilp = QtWidgets.QCheckBox('Ignore Lunar Position', self)
        self.emle = QtWidgets.QLineEdit(self)
        self.emlp = QtWidgets.QLineEdit(self)

        self.setting_up()

    def setting_up(self):
        vbox = set_lvbox(set_hbox(self.lmse, self.emse),
                         set_hbox(self.eilp),
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
