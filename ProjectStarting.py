import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from dialog1 import Ui_Form1


class MyWidget(QMainWindow, Ui_Form1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)




app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())