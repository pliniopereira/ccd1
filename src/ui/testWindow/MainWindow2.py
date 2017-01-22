from PyQt5 import QtWidgets

from src.ui.testWindow.MainWindow import MainWindow


class MainWindow2(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow2, self).__init__(parent)
        a = MainWindow(self)
        self.setCentralWidget(a)
