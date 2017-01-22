from PyQt5 import QtWidgets

from src.ui.commons.layout import set_hbox, set_lvbox


class WidgetsPath(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(WidgetsPath, self).__init__(parent)

        self.cStart = QtWidgets.QCheckBox('Automatic Mode Start', self)

        self.lLog = QtWidgets.QLabel('Log Path:', self)
        self.eLog = QtWidgets.QLineEdit(self)
        self.pbutton = QtWidgets.QPushButton("Select Folder", self)


        '''self.lProjPath = QtWidgets.QLabel('Project Path:')
        self.eProjPath = QtWidgets.QLineEdit(self)
        self.pbutton = QtWidgets.QPushButton("Open File", self)'''

        self.lImagesPath = QtWidgets.QLabel('Images Path:')
        self.eImagesPath = QtWidgets.QLineEdit(self)
        self.ibutton = QtWidgets.QPushButton('Select Folder', self)

        self.filename = ""
        self.path = ""

        self.setting_up()

    def setting_up(self):
        vbox = set_lvbox(set_hbox(self.cStart),
                         set_hbox(self.lLog, self.eLog, self.pbutton),
                         set_hbox(self.lImagesPath, self.eImagesPath, self.ibutton))

        self.pbutton.clicked.connect(self.open_projectpath)
        self.ibutton.clicked.connect(self.open_imagepath)

        self.setLayout(vbox)

    def get_values(self):
        return self.cStart.isChecked(), self.eLog.text(), self.eImagesPath.text()

    def set_values(self, cstart, elog, eip):
        self.cStart.setChecked(cstart)
        self.eLog.setText(elog)
        self.eImagesPath.setText(eip)

    def open_projectpath(self):
        try:
            filename = QtWidgets.QFileDialog.getExistingDirectory(self, 'OpenFile')
            self.eLog.setText(str(filename))

            self.filename = filename
        except Exception as e:
            print(e)

    def open_imagepath(self):
        try:
            path = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select a Folder')
            self.eImagesPath.setText(str(path))

            self.path = path
        except Exception as e:
            print(e)

    def clear_path(self):
        self.cStart.setChecked(False)
        self.eLog.clear()
        self.eImagesPath.clear()
