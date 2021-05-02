import sys
from PySide2.QtWidgets import QApplication, QPushButton
from PySide2.QtCore import QObject, Signal, Slot

app = QApplication(sys.argv)


@Slot(int)
@Slot(str)
def say_something(stuff):
    print(stuff)


class Communicate(QObject):
    speak_number = Signal(int)
    speak_word = Signal(str)

    def run(self):
        self.speak_number.emit(10)
        self.speak_word.emit("Hello everybody!")


someone = Communicate()
someone.speak_number.connect(say_something)
someone.speak_word.connect(say_something)

someone.run()
