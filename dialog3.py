# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'third.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form3(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 380)
        self.in_3 = QtWidgets.QPushButton(Form)
        self.in_3.setGeometry(QtCore.QRect(300, 190, 71, 23))
        self.in_3.setObjectName("in_3")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(180, 140, 51, 16))
        self.label_5.setObjectName("label_5")
        self.err_3 = QtWidgets.QLabel(Form)
        self.err_3.setGeometry(QtCore.QRect(230, 100, 221, 16))
        self.err_3.setStyleSheet("QLabel { color:red\n"
"                            }")
        self.err_3.setText("")
        self.err_3.setObjectName("err_3")
        self.rg_3 = QtWidgets.QPushButton(Form)
        self.rg_3.setGeometry(QtCore.QRect(380, 190, 71, 23))
        self.rg_3.setObjectName("rg_3")
        self.Exit_3 = QtWidgets.QPushButton(Form)
        self.Exit_3.setGeometry(QtCore.QRect(380, 270, 75, 23))
        self.Exit_3.setObjectName("Exit_3")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(180, 100, 47, 13))
        self.label_6.setObjectName("label_6")
        self.login_3 = QtWidgets.QLineEdit(Form)
        self.login_3.setGeometry(QtCore.QRect(180, 120, 271, 20))
        self.login_3.setObjectName("login_3")
        self.passw_3 = QtWidgets.QLineEdit(Form)
        self.passw_3.setGeometry(QtCore.QRect(180, 160, 271, 20))
        self.passw_3.setObjectName("passw_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.in_3.setText(_translate("Form", "Autorization"))
        self.label_5.setText(_translate("Form", "Password:"))
        self.rg_3.setText(_translate("Form", "Create"))
        self.Exit_3.setText(_translate("Form", "Exit"))
        self.label_6.setText(_translate("Form", "Login:"))

