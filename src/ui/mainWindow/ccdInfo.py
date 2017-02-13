from PyQt5 import QtCore
from PyQt5 import QtWidgets

from src.controller.camera import Camera
from src.ui.commons.layout import set_hbox, set_lvbox
from src.ui.commons.widgets import get_qfont


class CCDInfo(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(CCDInfo, self).__init__(parent)
        self.cam = Camera()
        self.init_widgets()
        self.config_widgets()

    def init_widgets(self):
        self.title = QtWidgets.QLabel("CCD Information", self)

        """
        Function to initiate the Widgets of CCD Information
        """
        # Camera Firmware
        lf = QtWidgets.QLabel("Firmware:", self)

        # LineEdit to show Firmware version
        tfirm = QtWidgets.QLabel(self)

        # Camera Name
        ln = QtWidgets.QLabel("Camera:", self)

        pixels_field = QtWidgets.QLabel(self)

        X_Pixels = QtWidgets.QLabel("", self)
        Y_Pixels = QtWidgets.QLabel(self)

        self.cam.set_firmware_and_model_fields(lf, ln, X_Pixels, Y_Pixels)
        # LineEdit to show camera model
        cn = QtWidgets.QLabel(self)
        cn.setAlignment(QtCore.Qt.AlignCenter)

        # Setting the layout
        self.setLayout(set_lvbox(set_hbox(self.title),
                                 set_hbox(lf, tfirm),
                                 set_hbox(ln, cn),
                                 set_hbox(X_Pixels, Y_Pixels, pixels_field)))

    def config_widgets(self):
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setFont(get_qfont(True))

        self.setStyleSheet("background-color: rgb(50, 50, 50); border-radius: 10px; color: white;")