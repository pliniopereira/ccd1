from datetime import datetime

from PyQt5 import QtWidgets


class ConsoleLogWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(ConsoleLogWidget, self).__init__(parent)

        self.logOutput = QtWidgets.QTextEdit(self)
        self.configLogOutput()

        self.setStyleSheet("background-color: rgb(50, 50, 50); border-radius: 10px; color: white;")

    def get_logOutput(self):
        return self.logOutput

    def configLogOutput(self):
        self.logOutput.setReadOnly(True)
        self.logOutput.setMinimumWidth(558)
        self.logOutput.setMaximumHeight(100)

    def scrollDown(self):
        sb = self.logOutput.verticalScrollBar()
        sb.setValue(sb.maximum())

    def newLine(self, text, level):
        if level == 0:
            self.setStyleSheet("background-color: rgb(50, 50, 50); border-radius: 10px; color: white;")
        elif level == 1:
            self.setStyleSheet("background-color: rgb(90, 255, 90); border-radius: 10px; color: black;")
        elif level == 2:
            self.setStyleSheet("background-color: rgb(255, 240, 0); border-radius: 10px; color: black;")
        else:
            self.setStyleSheet("background-color: rgb(255, 5, 0); border-radius: 10px; color: black;")

        self.logOutput.insertPlainText(datetime.utcnow().strftime('[%Y-%m-%d @ %H:%M:%S UTC]') + ' - ' + text + '\n')
        self.scrollDown()
