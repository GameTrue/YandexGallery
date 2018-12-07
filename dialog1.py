# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frst.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from wi import Ui_Form

class Ui_Form1(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 380)
        self.Exit_3 = QtWidgets.QPushButton(Form)
        self.Exit_3.setGeometry(QtCore.QRect(260, 210, 151, 31))
        self.Exit_3.setObjectName("Exit_3")
        self.credits_2 = QtWidgets.QPushButton(Form)
        self.credits_2.setGeometry(QtCore.QRect(260, 170, 151, 31))
        self.credits_2.setObjectName("credits_2")
        self.login_3 = QtWidgets.QPushButton(Form)
        self.login_3.setGeometry(QtCore.QRect(260, 90, 151, 31))
        self.login_3.setObjectName("login_3")
        self.info_2 = QtWidgets.QPushButton(Form)
        self.info_2.setGeometry(QtCore.QRect(260, 130, 151, 31))
        self.info_2.setObjectName("info_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Exit_3.setText(_translate("Form", "Exit"))
        self.credits_2.setText(_translate("Form", "Credits"))
        self.login_3.setText(_translate("Form", "Login"))
        self.login_3.clicked.connect(self.log_2)
        self.info_2.setText(_translate("Form", "Info"))

    def log_2(self):
        ex = MyWidget1()
        ex.show()

class MyWidget1(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
