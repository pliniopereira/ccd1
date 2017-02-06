from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets

from src.controller.camera import Camera
from src.ui.commons.layout import set_hbox, set_lvbox


# Aux Functions
def set_width(*s):
    for o in s:
        o.setMaximumWidth(25)
        o.setMaxLength(2)


class Shooter(QtWidgets.QWidget):
    """
    Class for Taking photo Widget
    """

    def __init__(self, parent=None):
        super(Shooter, self).__init__(parent)
        self.cam = Camera()
        self.cond = 0

        # Label for Image
        self.img = QtWidgets.QLabel(self)
        self.config_img_label()

        # Creating a Pallete
        self.pa = QtGui.QPalette()

        self.set_layout()
        self.link_signals()

    def link_signals(self):
        self.cam.ephemerisShooterThread.continuousShooterThread.ss.finished.connect(self.get_image_automatic)
        self.cam.continuousShooterThread.ss.finished.connect(self.get_image_manual)

    def get_image_automatic(self):
        img = self.cam.ephemerisShooterThread.continuousShooterThread.ss.get_image_info()
        self.set_image(img)

    def get_image_manual(self):
        img = self.cam.continuousShooterThread.ss.get_image_info()
        self.set_image(img)

    def set_layout(self):
        # self.fill_combo()
        #
        # hbox = set_hbox(self.sbutton, self.tb,
        # QLabel("Prefixo:", self), self.pre,
        # QLabel("Binning:", self), self.combo,
        # self.abutton,
        # QLabel("Hora:", self), self.htext,
        # QLabel("Min:", self), self.mtext)

        hb2 = set_hbox(self.prefix, self.date, self.hour)

        self.setLayout(set_lvbox(set_hbox(self.img), hb2))
        self.config_pallete()

    def config_img_label(self):
        self.img.setPixmap(QtGui.QPixmap("noimage.png"))
        self.prefix = QtWidgets.QLabel(self)
        self.date = QtWidgets.QLabel(self)
        self.hour = QtWidgets.QLabel(self)

    def config_pallete(self):
        self.pa.setColor(QtGui.QPalette.Foreground, QtCore.Qt.red)  # Setting the style
        self.prefix.setPalette(self.pa)
        self.date.setPalette(self.pa)
        self.hour.setPalette(self.pa)

    def shoot_function(self):
        self.cam.shoot(int(self.tb.text()), self.pre.text(), int(self.combo.currentIndex()))
        self.set_image()

    def auto_shoot(self):
        try:
            self.cam.autoshoot(int(self.htext.text()), int(self.mtext.text()), int(self.tb.text()), self.pre.text(), int(self.combo.currentIndex()))
        except Exception as e:
            print(e)

    def set_image(self, img):
        print("Setting Pixmap")
        try:
            path = img.path + img.png_name
            self.img.setPixmap(QtGui.QPixmap(path))
            print(path)
            #self.fill_image_info(img.png_name, img.date, img.hour)

        except Exception as e:
            print(e)

    def fill_combo(self):
        self.combo.addItem("1x1", 0)
        self.combo.addItem("2x2", 1)
        self.combo.addItem("3x3", 2)

    '''def fill_image_info(self, filename, time, hora):
        self.prefix.setText(filename)
        self.date.setText(time)
        self.hour.setText(hora)'''

    def clear_image_info(self):
        self.prefix.clear()
