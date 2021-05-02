# https://doc.qt.io/qt-5/qicon.html

import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox
from PySide6.QtGui import QIcon, QAction


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def show_version(self):
        QMessageBox.about(self, "about", "version 0.0.1a")

    def show_qt_version(self):
        QMessageBox.aboutQt(self, "about")

    def initUI(self):

        exitAction = QAction(QIcon('icons/exit.bmp'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        helpAction = QAction(QIcon('icons/help.png'), 'Version', self)
        helpAction.setShortcut('Ctrl+D')
        helpAction.setStatusTip('Show application\'s version')
        helpAction.triggered.connect(self.show_version)

        qt_version_helpAction = QAction(QIcon('icons/help.png'), "Qt's version", self)
        qt_version_helpAction.setShortcut('Ctrl+A')
        qt_version_helpAction.setStatusTip('Show Qt\'s version')
        qt_version_helpAction.triggered.connect(self.show_qt_version)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        menubar.addMenu('Edit')
        helpMenu = menubar.addMenu('Help')
        fileMenu.addAction(exitAction)
        helpMenu.addAction(helpAction)
        helpMenu.addSeparator()
        helpMenu.addAction(qt_version_helpAction)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Menubar')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
