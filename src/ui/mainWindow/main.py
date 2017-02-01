from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon

from src.business.configuration.configSystem import ConfigSystem
from src.controller.camera import Camera
from src.ui.cameraSettingsWindow.main import Main as csw
from src.ui.ephemerisShooterWindow.main import Main as eph
from src.ui.mainWindow.mainWindow import MainWindow
from src.ui.mainWindow.status import Status
from src.ui.projectSettingsWindow.main import MainWindow as sw
from src.ui.systemSettingsWindow.main import MainWindow as mw
from src.ui.testWindow.MainWindow2 import MainWindow2 as conts


class Main(QtWidgets.QMainWindow):
    """
    classe de criacao da interface
    """
    def __init__(self):
        super(Main, self).__init__()
        Status(self)
        # Init Layouts
        self.init_widgets()
        self.init_user_interface()

    def init_user_interface(self):
        self.cont = conts(self)
        self.ephem = eph(self)
        self.a = sw(self)
        self.b = mw(self)
        self.c = csw(self)
        self.cam = Camera()
        self.init_menu()
        self.init_window_geometry()

        self.cs = ConfigSystem()

        info = self.cs.get_site_settings()

        # Connect Camera
        if info[0] == True:
            self.cam.connect()
            self.cam.start_ephemeris_shooter()

    def init_widgets(self):
        a = MainWindow(self)
        self.setCentralWidget(a)

    def init_window_geometry(self):
        self.setGeometry(300, 100, 800, 700)
        self.setWindowTitle("CCD Controller 1.0.0")
        self.show()

    # Creating menubar

    def init_menu(self):
        """
        Creating the Menu Bar
        """
        menubar = self.menuBar()

        a1 = self.action_close()
        self.add_to_menu(menubar, a1[1], a1[0])
        a3 = self.action_connect_disconnect()
        self.add_to_menu(menubar, a3[0], a3[1], a3[2])
        a4 = self.action_continuous_shooter()
        a5 = self.action_ephemeris_shooter()
        m = self.add_to_menu(menubar, 'Operation Mode')
        self.add_to_menu(m, 'Manual', a4[0], a4[1])
        self.add_to_menu(m, 'Automatic', a5[0], a5[1])
        a2 = self.open_settings()
        self.add_to_menu(menubar, a2[1], self.open_settings_system()[0], a2[0], self.open_settings_camera()[0])

        # add_to_menu(menubar, open_settings_system(self))

    # All actions needs return a QAction and a menuType, line '&File'
    def action_close(self):
        """
        Creating the button to close the application
        """
        aexit = QtWidgets.QAction(QIcon('\icons\exit.png'), "&Exit", self)
        aexit.setShortcut("Ctrl+Q")
        aexit.setStatusTip("Exit Application")

        # noinspection PyUnresolvedReferences
        aexit.triggered.connect(QtWidgets.qApp.exit)

        return aexit, "&File"

    def action_continuous_shooter(self):
        """
        Inicia e para o modo manual
        """
        actionStart = QtWidgets.QAction('&Start', self)
        actionStop = QtWidgets.QAction('&Stop', self)

        actionStart.triggered.connect(self.cam.start_taking_photo)
        actionStop.triggered.connect(self.cam.stop_taking_photo)

        return actionStart, actionStop

    def action_ephemeris_shooter(self):
        """
        Inicia e para o modo automatico
        """
        actionStart = QtWidgets.QAction('&Start', self)
        actionStop = QtWidgets.QAction('&Stop', self)

        actionStart.triggered.connect(self.cam.start_ephemeris_shooter)
        actionStop.triggered.connect(self.cam.stop_ephemeris_shooter)

        return actionStart, actionStop

    def open_settings(self):
        settings = QtWidgets.QAction('Project Settings', self)
        settings.setShortcut("Ctrl+P")
        settings.setStatusTip("Open Settings window")

        settings.triggered.connect(self.a.show)

        return settings, "&Options"

    def open_settings_system(self):
        setS = QtWidgets.QAction('System Settings', self)
        setS.setShortcut('Ctrl+T')

        setS.triggered.connect(self.b.show)

        return setS, "&Options"

    def open_settings_camera(self):
        setC = QtWidgets.QAction('Camera Settings', self)
        setC.setShortcut("Ctrl+C")

        setC.triggered.connect(self.c.show)

        return setC, "&Options"

    def action_connect_disconnect(self):
        setAC = QtWidgets.QAction('Connect', self)
        setAD = QtWidgets.QAction('Disconnect', self)

        setAC.triggered.connect(self.cam.connect)

        setAD.triggered.connect(self.cam.disconnect)

        return 'Connection', setAC, setAD

    def add_to_menu(self, menubar, menu, *args):
        m = menubar.addMenu(menu)
        for w in args:
            m.addAction(w)

        return m

