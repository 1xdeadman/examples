# https://doc.qt.io/qtforpython/tutorials/basictutorial/uifiles.html
# https://doc.qt.io/qtforpython/tutorials/
# https://doc.qt.io/qtforpython/tutorials/basictutorial/uifiles.html
# https://doc.qt.io/qtforpython/api.html
# https://doc.qt.io/qtforpython/PySide2/QtWidgets/index.html#module-PySide2.QtWidgets

import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QFile

from Ui_MainWindow import press_F


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.method1()
    
    def method1(self):
        self.ui.test.textCursor().insertText("asd")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())