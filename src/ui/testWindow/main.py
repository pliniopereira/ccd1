import sys

from PyQt5 import QtWidgets

from src.ui.mainWindow.tempMonitor import TempMonitor
from src.ui.testWindow.MainWindow2 import MainWindow2


class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.a = MainWindow2(self)

        menu = self.menuBar()

        ac = QtWidgets.QAction('&Manual', self)
        ac.triggered.connect(self.a.show)

        m = menu.addMenu("&File")
        m.addAction(ac)

        self.temp = TempMonitor()
        self.setWindowTitle("Main")
        self.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec_())