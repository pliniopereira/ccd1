import os
import sys
sys.path.append(os.path.dirname(os.getcwd()))

from PyQt5 import QtWidgets

from src.ui.mainWindow.main import Main


# sudo -u hiyoku python main.py
# Initiating the application
try:
    app = QtWidgets.QApplication(sys.argv)
    '''
    acessa a classe mainWindow/main.py para criacao da interface
    '''
    ex = Main()
    ex.show()
    sys.exit(app.exec_())
except Exception as e:
    print(e)
