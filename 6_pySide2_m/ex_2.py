# https://doc.qt.io/qt-5/signalsandslots.html
# https://wiki.qt.io/Qt_for_Python_Signals_and_Slots
# https://doc.qt.io/qtforpython/PySide6/QtWidgets/index.html
# https://doc.qt.io/qtforpython/PySide6/QtWidgets/QToolTip.html
# https://doc.qt.io/qtforpython/PySide6/QtWidgets/QPushButton.html
# https://doc.qt.io/qtforpython/PySide6/QtWidgets/QMessageBox.html
# https://doc.qt.io/qtforpython/PySide6/QtWidgets/QMenu.html
# https://doc.qt.io/qtforpython/PySide6/QtWidgets/QAction.html

import sys
import time
from PySide6.QtWidgets import (QApplication, QWidget, QToolTip, QPushButton, QMessageBox, QMenu)
from PySide6.QtGui import QFont, QAction


class Example_2(QWidget):

    def __init__(self):
        super().__init__()
        self.init_UI()

    def ok(self):
        print('start sleep')
        time.sleep(5)
        print('end sleep')

    def ney(self):
        print('Ney!')

    def show_question_message_box(self):
        sender = self.sender()
        
        reply = QMessageBox.question(
            self,
            'Message',
            "Are you sure to quit?",
            QMessageBox.Yes | QMessageBox.Yes | QMessageBox.Cancel,
            QMessageBox.Yes)

        '''
        mesg_bx = QMessageBox(self)
        mesg_bx.setWindowTitle("title")
        mesg_bx.setText("Message")
        mesg_bx.addButton(QMessageBox.Yes)
        mesg_bx.addButton(QMessageBox.No)
        mesg_bx.addButton(QMessageBox.Cancel)
        mesg_bx.setDefaultButton(QMessageBox.Yes)
        reply = mesg_bx.exec()
        '''

        btn_text = ""
        if reply == QMessageBox.Yes:
            btn_text = "OK"
            
            self.ok()
        elif reply == QMessageBox.No:
            btn_text = "No"
            self.ney()
        elif reply == QMessageBox.Cancel:
            btn_text = "Cancel"
            print("hop hey, lalaley")

        sender.setText(btn_text)

    def show_message_box(self):
        reply = QMessageBox.about(
            self,
            'Message',
            "lel")

    def init_UI(self):

        QToolTip.setFont(QFont('TimesNeWRoman', 14))
        self.setFont(QFont('SansSerif', 10))
        self.simple_button()
        self.menu_button()

        self.setGeometry(650, 400, 500, 150)  # (300, 300, 300, 200)
        self.setWindowTitle('example 2')
        self.show()

    def simple_button(self):
        sleep_btn = QPushButton('Sleep Button', self)
        # sleep_btn = QPushButton('&Sleep Button', self)  # Alt + S
        sleep_btn.setToolTip('This is a <b>QPushButton</b> widget')
        sleep_btn.resize(sleep_btn.sizeHint())
        sleep_btn.move(50, 50)
        sleep_btn.clicked.connect(self.show_question_message_box)

    def menu_button(self):
        sleep_btn = QPushButton('Sleep Button', self)
        # sleep_btn = QPushButton('&Sleep Button', self)  # Alt + S
        sleep_btn.setToolTip('This is a menu')
        sleep_btn.resize(sleep_btn.sizeHint())
        sleep_btn.move(200, 50)

        menu = QMenu("kek", self)
        menu.addAction(self.new_action('1', shortcut="Ctrl+A"))
        menu.addAction(self.new_action('2'))

        sleep_btn.setMenu(menu)
        # sleep_btn.clicked.connect(self.show_question_message_box)

    def new_action(self, name: str, tip: str="", shortcut: str='Ctrl+Q'):
        action = QAction(name, self)
        action.setShortcut(shortcut)
        action.setStatusTip(tip)
        action.triggered.connect(self.show_message_box)
        return action


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example_2()
    sys.exit(app.exec_())