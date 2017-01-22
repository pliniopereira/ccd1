from PyQt5 import QtGui


def get_qfont(bold):
    font = QtGui.QFont()
    font.setFamily("Courier")
    font.setBold(bold)
    font.setPixelSize(12)
    return font
