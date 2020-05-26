# https://pythonworld.ru/gui/pyqt5-menustoolbars.html

import sys
from PySide2.QtWidgets import QMainWindow, QApplication, QPushButton


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def clicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was clicked!')


    def initUI(self):
        btn = QPushButton("kek", self)
        btn.clicked.connect(self.clicked)

        self.statusBar().showMessage('Ready')

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Statusbar')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())