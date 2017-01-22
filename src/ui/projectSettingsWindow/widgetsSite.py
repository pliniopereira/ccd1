from PyQt5 import QtWidgets

from src.ui.commons.layout import set_hbox, set_lvbox


class WidgetsSite(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(WidgetsSite, self).__init__(parent)

        # Creating Labels
        self.lPName = QtWidgets.QLabel("Project Name:", self)
        self.lSite = QtWidgets.QLabel("Site ID:", self)
        self.lImager = QtWidgets.QLabel("Imager ID:", self)

        # Creating Input Line
        self.ePName = QtWidgets.QLineEdit(self)
        self.eSite = QtWidgets.QLineEdit(self)
        self.eImager = QtWidgets.QLineEdit(self)

        self.setting_up()

    def setting_up(self):
        vbox = set_lvbox(set_hbox(self.lPName, self.ePName),
                         set_hbox(self.lSite, self.eSite),
                         set_hbox(self.lImager, self.eImager))

        self.setLayout(vbox)

    def get_site_info(self):
        return self.ePName.text(), self.eSite.text(), self.eImager.text()

    def set_site_info(self, projectName, siteName, imagerName):
        self.ePName.setText(projectName)
        self.eSite.setText(siteName)
        self.eImager.setText(imagerName)

    def clear_site(self):
        self.ePName.clear()
        self.eSite.clear()
        self.eImager.clear()

    def get_name(self):
        return self.ePName.text()
