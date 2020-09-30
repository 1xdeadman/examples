# https://github.com/learnpyqt/python-qtwidgets
from PySide2.QtWidgets import QApplication, QWidget, QLCDNumber, QVBoxLayout
import power_bar
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        lcd = QLCDNumber(self)

        volume = power_bar.PowerBar(
            ["#053061",
            "#2166ac",
            "#4393c3",
            "#92c5de",
            "#d1e5f0",
            "#f7f7f7",
            "#fddbc7",
            "#f4a582",
            "#d6604d",
            "#b2182b",
            "#67001f"])
        volume.setBarSolidPercent(0.8)
        volume.setBarPadding(5)
        volume.show()

        vbox = QVBoxLayout()
        vbox.addWidget(volume)
        vbox.addWidget(lcd)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 250, 550)
        self.setWindowTitle('EXample fin')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
