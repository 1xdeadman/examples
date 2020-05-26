# https://doc.qt.io/qt-5/qlcdnumber.html
# https://doc.qt.io/qt-5/qslider.html
# https://doc.qt.io/qt-5/qvboxlayout.html
# https://doc.qt.io/qtforpython/PySide2/QtCore/QObject.html#PySide2.QtCore.PySide2.QtCore.QObject.findChild
# https://doc.qt.io/qtforpython/overviews/layout.html
import sys
from PySide2.QtCore import Qt
from PySide2.QtWidgets import ( QApplication, QWidget, QRadioButton, QLCDNumber, QSlider, QVBoxLayout)


class Example(QWidget):



    def __init__(self):
        super().__init__()

        self.initUI()

    def switch_binary(self):
        sender = self.sender()
        lcd = self.findChild(QLCDNumber)  # findChildren
        if sender.isChecked() == True:
            # lcd.setHexMode()
            # lcd.setDecMode()
            lcd.setBinMode()
        else:
            lcd.setDecMode()


    def initUI(self):

        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)
        is_binary = QRadioButton("is binary?", self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)
        vbox.addWidget(is_binary)

        self.setLayout(vbox)
        # sld.setRange(0, 10)
        sld.setMaximum(1000)
        sld.setMinimum(-100)

        sld.valueChanged.connect(lcd.display)
        is_binary.toggled.connect(self.switch_binary)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('EXample 6')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
