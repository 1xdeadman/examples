import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader

ui_file = QFile("E:/projects/UI/test_1.ui")
ui_file.open(QFile.ReadOnly)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    loader = QUiLoader()
    window = loader.load(ui_file)
    window.show()

    sys.exit(app.exec_())
