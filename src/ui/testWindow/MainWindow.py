import time
from threading import Thread

from PyQt5 import QtWidgets

from src.controller.camera import Camera


class MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.cam = Camera()
        self.button_start_count = QtWidgets.QPushButton('Start', self)
        self.button_stop_count = QtWidgets.QPushButton('Stop', self)

        self.set_layout()
        self.control = False
        self.count = 0
        self.setWindowTitle("oi")

    def set_layout(self):
        self.line1_layout = QtWidgets.QHBoxLayout()

        self.line1_layout.addWidget(self.button_start_count)
        self.line1_layout.addStretch(1)
        self.line1_layout.addWidget(self.button_stop_count)

        self.button_start_count.clicked.connect(self.cam.start_taking_photo)
        self.button_stop_count.clicked.connect(self.cam.stop_taking_photo)

        self.setLayout(self.line1_layout)

    def function_start_thread(self):
        t = Thread(target=self.start_count)
        self.control = True
        t.start()

    def function_stop_thread(self):
        self.control = False
        print("Stopped")

    def start_count(self):
        while self.control:
            self.count += 1
            print(self.count)
            time.sleep(1)


