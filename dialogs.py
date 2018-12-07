# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frst.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 380)
        self.login = QtWidgets.QPushButton(Dialog)
        self.login.setGeometry(QtCore.QRect(240, 80, 151, 31))
        self.login.setObjectName("login")
        self.info = QtWidgets.QPushButton(Dialog)
        self.info.setGeometry(QtCore.QRect(240, 120, 151, 31))
        self.info.setObjectName("info")
        self.credits = QtWidgets.QPushButton(Dialog)
        self.credits.setGeometry(QtCore.QRect(240, 160, 151, 31))
        self.credits.setObjectName("credits")
        self.Exit = QtWidgets.QPushButton(Dialog)
        self.Exit.setGeometry(QtCore.QRect(240, 200, 151, 31))
        self.Exit.setObjectName("Exit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.login.setText(_translate("Dialog", "Login"))
        self.info.setText(_translate("Dialog", "Info"))
        self.credits.setText(_translate("Dialog", "Credits"))
        self.Exit.setText(_translate("Dialog", "Exit"))

