# https://doc.qt.io/qtforpython/PySide2/QtWidgets/QLabel.html
# https://doc.qt.io/qtforpython/PySide2/QtWidgets/QFormLayout.html
# https://doc.qt.io/qtforpython/PySide2/QtWidgets/QLineEdit.html
# https://doc.qt.io/qtforpython/PySide2/QtWidgets/QTextEdit.html
# https://doc.qt.io/qtforpython/PySide2/QtWidgets/QInputDialog.html

import sys

from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QFormLayout, QLineEdit, QTextEdit, QInputDialog


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._init_UI()
    
    def set_text(self):
        input_d = QInputDialog(self)
        res_text, res_ok = input_d.getText(self, "title", "text:")
        if res_ok:
            self.text.setText(res_text)

    def set_title(self):
        self.setWindowTitle(self.form_name.text())

    def _init_UI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Example 7')


        self.label_name = QLabel("form name", self)
        self.text = QTextEdit("kek", self)

        # self.kek_btn = QLabel("kek", self)
        self.kek_btn = QPushButton("kek", self)
        self.form_name = QLineEdit(self.windowTitle(), self)


        self.layout = QFormLayout(self)
        self.layout.addRow(self.label_name, self.form_name)
        self.layout.addRow(self.kek_btn, self.text)

        self.form_name.textChanged.connect(self.set_title)
        self.kek_btn.clicked.connect(self.set_text)
        # self.layout.addWidget(self.kek_btn, 0, 0)
        # self.layout.addWidget(self.text, 0, 1)

        self.setLayout(self.layout)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWidget()
    sys.exit(app.exec_())