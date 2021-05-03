# Gtk vs Qt(PySide 2 vs PyQt5)
# GPL, LGPL, MIT, Apache license
# https://www.qt.io/
# https://www.qt.io/download
# https://doc.qt.io/qtforpython/
# https://doc.qt.io/qtforpython/tutorials/index.html
# https://doc.qt.io/qtforpython/contents.html
# https://doc.qt.io/qtforpython/api.html
# https://doc.qt.io/qtforpython/PySide6/QtWidgets/QWidget.html

# pip install PySide6
import sys
import PySide6.QtCore
from PySide6.QtWidgets import QApplication, QWidget

print(PySide6.__version__)

if __name__ == '__main__':

    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(250, 150)
    w.move(0, 0)
    w.setWindowTitle('example 1')
    w.show()

    sys.exit(app.exec_())
