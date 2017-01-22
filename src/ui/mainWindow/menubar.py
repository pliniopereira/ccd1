from PyQt5 import QtGui
from PyQt5 import QtWidgets

from src.controller.camera import Camera
from src.ui.cameraSettingsWindow.main import Main as csw
from src.ui.continuousShooterWindow.main import Main as conts
from src.ui.projectSettingsWindow.main import MainWindow
from src.ui.systemSettingsWindow.main import MainWindow as mw


def init_menu(self):
    # Creating the Menu Bar
    menubar = self.menuBar()

    a1 = action_close(self)
    add_to_menu(menubar, a1[1], a1[0])
    a2 = open_settings(self)
    add_to_menu(menubar, a2[1], a2[0], open_settings_system(self)[0], open_settings_camera(self)[0])
    a3 = action_connect_disconnect(self)
    add_to_menu(menubar, a3[0], a3[1], a3[2])

    a4 = action_continuous_shooter(self, menubar)
    add_to_menu(menubar, 'Operation Mode', a4)
    # add_to_menu(menubar, open_settings_system(self))


def menu_operation_mode(self, menubar):
    pass

# All actions needs return a QAction and a menuType, line '&File'


def action_close(self):
    # Creating the button to close the application
    aexit = QtWidgets.QAction(QtGui.QIcon('\icons\exit.png'), "&Exit", self)
    aexit.setShortcut("Ctrl+Q")
    aexit.setStatusTip("Exit Application")

    # noinspection PyUnresolvedReferences
    aexit.triggered.connect(qApp.exit)

    return aexit, "&File"


def action_continuous_shooter(self, menubar):
    menubar.addMenu('Operation Mode')
    ac = QtWidgets.QAction('&Manual', self)
    self.cont = conts()

    ac.triggered.connect(self.cont.show)


def open_settings(self):
    settings = QtWidgets.QAction('Project Settings', self)
    settings.setShortcut("Ctrl+P")
    settings.setStatusTip("Open Settings window")
    self.a = MainWindow()

    settings.triggered.connect(self.a.show)

    return settings, "&Options"


def open_settings_system(self):
    setS = QtWidgets.QAction('System Settings', self)
    setS.setShortcut('Ctrl+T')
    self.b = mw()

    setS.triggered.connect(self.b.show)

    return setS, "&Options"


def open_settings_camera(self):
    setC = QtWidgets.QAction('Camera Settings', self)
    setC.setShortcut("Ctrl+C")
    self.c = csw()

    setC.triggered.connect(self.c.show)

    return setC, "&Options"


def action_connect_disconnect(self):
    setAC = QtWidgets.QAction('Connect', self)
    setAD = QtWidgets.QAction('Disconnect', self)
    self.cam = Camera()

    setAC.triggered.connect(self.cam.connect)

    setAD.triggered.connect(self.cam.disconnect)

    return 'Connection', setAC, setAD


def add_to_menu(menubar, menu, *args):
    m = menubar.addMenu(menu)
    for w in args:
        m.addAction(w)
