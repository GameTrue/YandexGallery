import sys
from ProjectStarting import Ui_Form1
from ProjectStarting import Ui_Form2
from ProjectStarting import Ui_Form3
from ProjectStarting import Ui_Form4
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets


class MyWidget(QMainWindow, Ui_Form1):
    def __init__(self, con):
        self.con = con
        super().__init__()
        self.setupUi(self)
        self.login_3.clicked.connect(self.con.dia1)
        self.Exit_3.clicked.connect(self.close)


class MyWidget1(QMainWindow, Ui_Form2):
    def __init__(self, con):
        self.con = con
        super().__init__()
        self.setupUi(self)
        self.rg_2.clicked.connect(self.con.dia2)
        self.in_2.clicked.connect(self.con.dia3)
        self.Back_2.clicked.connect(self.)
        self.Exit_2.clicked.connect(self.close)


class MyWidget2(QMainWindow, Ui_Form3):
    def __init__(self, con):
        self.con = con
        super().__init__()
        self.setupUi(self)
        self.Exit_3.clicked.connect(self.close)


class MyWidget3(QMainWindow, Ui_Form4):
    def __init__(self, con):
        self.con = con
        super().__init__()
        self.setupUi(self)
        self.Exit.clicked.connect(self.close)


class Connector():
    def __init__(self):
        self.form = MyWidget(self)
        self.form1 = MyWidget1(self)
        self.form2 = MyWidget2(self)
        self.form3 = MyWidget3(self)

    def dia(self):
        self.form.show()

    def dia1(self):
        self.form1.show()

    def dia2(self):
        self.form2.show()

    def dia3(self):
        self.form3.show()


# def con(n):
#     data2.append(data[n]())
#     # ex = data[n]()
#     data2[-1].show()


# data = [MyWidget, MyWidget1, MyWidget2]
# data2 = []
app = QApplication(sys.argv)
connector = Connector()
connector.dia()
# ex = MyWidget2()
# ex.show()
sys.exit(app.exec_())
