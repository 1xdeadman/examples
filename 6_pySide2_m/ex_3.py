# РАНО ЕЩЕ
# https://doc.qt.io/qt-5/qdesktopwidget.html
# https://doc.qt.io/qt-5/qrect.html
# https://doc.qt.io/qt-5/qwidget.html#frameGeometry-prop
import sys
from PySide6.QtWidgets import QWidget, QDesktopWidget, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.set_UI()


    def set_UI(self):

        self.resize(250, 150)
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        self.setWindowTitle('Center')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())