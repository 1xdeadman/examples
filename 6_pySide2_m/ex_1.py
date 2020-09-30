# Gtk vs Qt(PySide 2 vs PyQt5)
# GPL, LGPL, MIT, Apache license
# https://www.qt.io/
# https://www.qt.io/download
# https://doc.qt.io/qtforpython/
# https://doc.qt.io/qtforpython/contents.html
# https://doc.qt.io/qtforpython/api.html#basic-modules
# https://doc.qt.io/qtforpython/PySide2/QtWidgets/QWidget.html


# pip install PySide2
import os
import sys
import  PySide2.QtCore
from  PySide2.QtWidgets import QApplication, QWidget

# Prints PySide2 version
# e.g. 5.11.1a1
print(PySide2.__version__)

if __name__ == '__main__':

    del os.environ["QT_DEVICE_PIXEL_RATIO"]
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(250, 150)
    w.move(0, 0)
    w.setWindowTitle('example 1')
    w.show()

    sys.exit(app.exec_())