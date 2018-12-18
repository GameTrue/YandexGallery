# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sec.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap


class Ui_Form2(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 380)
        Form.setStyleSheet("QWidget { background-color: gray }")
        self.rg_2 = QtWidgets.QPushButton(Form)
        self.rg_2.setGeometry(QtCore.QRect(390, 180, 71, 23))
        self.rg_2.setObjectName("rg_2")
        self.passw_2 = QtWidgets.QLineEdit(Form)
        self.passw_2.setGeometry(QtCore.QRect(190, 150, 271, 20))
        self.passw_2.setObjectName("passw_2")
        self.err_2 = QtWidgets.QLabel(Form)
        self.err_2.setGeometry(QtCore.QRect(240, 90, 221, 16))
        self.err_2.setStyleSheet("QLabel { color:red\n"
                                 "                            }")
        self.err_2.setText("")
        self.err_2.setObjectName("err_2")
        self.Exit_2 = QtWidgets.QPushButton(Form)
        self.Exit_2.setGeometry(QtCore.QRect(390, 260, 75, 23))
        self.Exit_2.setObjectName("Exit_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(190, 130, 51, 16))
        self.label_3.setObjectName("label_3")
        self.in_2 = QtWidgets.QPushButton(Form)
        self.in_2.setGeometry(QtCore.QRect(310, 180, 71, 23))
        self.in_2.setObjectName("in_2")
        self.login_2 = QtWidgets.QLineEdit(Form)
        self.login_2.setGeometry(QtCore.QRect(190, 110, 271, 20))
        self.login_2.setObjectName("login_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(190, 90, 47, 13))
        self.label_4.setObjectName("label_4")
        self.Back_2 = QtWidgets.QPushButton(Form)
        self.Back_2.setGeometry(QtCore.QRect(390, 230, 75, 23))
        self.Back_2.setObjectName("Back_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.rg_2.setText(_translate("Form", "Registration"))
        self.Exit_2.setText(_translate("Form", "Exit"))
        self.label_3.setText(_translate("Form", "PIN:"))
        self.in_2.setText(_translate("Form", "Login"))
        self.label_4.setText(_translate("Form", "UserID:"))
        self.Back_2.setText(_translate("Form", "Back"))
