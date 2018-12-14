import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap


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
        self.info_2.setText(_translate("Form", "Info"))


class Ui_Form2(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 380)
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


class Ui_Form3(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 380)
        self.in_3 = QtWidgets.QPushButton(Form)
        self.in_3.setGeometry(QtCore.QRect(310, 180, 71, 23))
        self.in_3.setObjectName("in_3")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(190, 130, 51, 16))
        self.label_5.setObjectName("label_5")
        self.err_3 = QtWidgets.QLabel(Form)
        self.err_3.setGeometry(QtCore.QRect(240, 90, 221, 16))
        self.err_3.setStyleSheet("QLabel { color:red\n"
                                 "                            }")
        self.err_3.setText("")
        self.err_3.setObjectName("err_3")
        self.rg_3 = QtWidgets.QPushButton(Form)
        self.rg_3.setGeometry(QtCore.QRect(390, 180, 71, 23))
        self.rg_3.setObjectName("rg_3")
        self.Exit_3 = QtWidgets.QPushButton(Form)
        self.Exit_3.setGeometry(QtCore.QRect(390, 260, 75, 23))
        self.Exit_3.setObjectName("Exit_3")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(190, 90, 47, 13))
        self.label_6.setObjectName("label_6")
        self.login_3 = QtWidgets.QLineEdit(Form)
        self.login_3.setGeometry(QtCore.QRect(190, 110, 271, 20))
        self.login_3.setObjectName("login_3")
        self.passw_3 = QtWidgets.QLineEdit(Form)
        self.passw_3.setGeometry(QtCore.QRect(190, 150, 271, 20))
        self.passw_3.setObjectName("passw_3")
        self.Back_3 = QtWidgets.QPushButton(Form)
        self.Back_3.setGeometry(QtCore.QRect(390, 230, 75, 23))
        self.Back_3.setObjectName("Back_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.in_3.setText(_translate("Form", "Autorization"))
        self.label_5.setText(_translate("Form", "PIN:"))
        self.rg_3.setText(_translate("Form", "Create"))
        self.Exit_3.setText(_translate("Form", "Exit"))
        self.label_6.setText(_translate("Form", "UserID:"))
        self.Back_3.setText(_translate("Form", "Back"))


class Ui_Form4(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 380)
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(340, 250, 131, 91))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")

        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(100, 70, 311, 231))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 30, 131, 91))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.Exit = QtWidgets.QPushButton(Form)
        self.Exit.setGeometry(QtCore.QRect(510, 320, 75, 23))
        self.Exit.setObjectName("Exit")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(40, 140, 131, 91))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(340, 140, 131, 91))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(190, 250, 131, 91))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(190, 30, 131, 91))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(340, 30, 131, 91))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(40, 250, 131, 91))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(190, 140, 131, 91))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.Back = QtWidgets.QPushButton(Form)
        self.Back.setGeometry(QtCore.QRect(510, 290, 75, 23))
        self.Back.setObjectName("Back")
        self.Add_2 = QtWidgets.QPushButton(Form)
        self.Add_2.setGeometry(QtCore.QRect(510, 100, 71, 23))
        self.Add_2.setObjectName("Add_2")
        self.Value = QtWidgets.QSpinBox(Form)
        self.Value.setGeometry(QtCore.QRect(510, 170, 71, 22))
        self.Value.setMinimum(1)
        self.Value.setMaximum(9)
        self.Value.setObjectName("Value")
        self.Show_3 = QtWidgets.QPushButton(Form)
        self.Show_3.setGeometry(QtCore.QRect(530, 200, 51, 23))
        self.Show_3.setObjectName("Show_3")
        self.Dele_4 = QtWidgets.QPushButton(Form)
        self.Dele_4.setGeometry(QtCore.QRect(530, 230, 51, 23))
        self.Dele_4.setObjectName("Dele_4")
        self.Value_2 = QtWidgets.QSpinBox(Form)
        self.Value_2.setGeometry(QtCore.QRect(510, 40, 71, 22))
        self.Value_2.setMinimum(1)
        self.Value_2.setMaximum(9)
        self.Value_2.setObjectName("Value_2")
        self.login_4 = QtWidgets.QLineEdit(Form)
        self.login_4.setGeometry(QtCore.QRect(480, 70, 101, 20))
        self.login_4.setObjectName("login_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_9.setText(_translate("Form", "No Image"))
        self.label_10.setText(_translate("Form", "image"))
        self.label.setText(_translate("Form", "No Image"))
        self.Exit.setText(_translate("Form", "Exit"))
        self.label_4.setText(_translate("Form", "No Image"))
        self.label_6.setText(_translate("Form", "No Image"))
        self.label_8.setText(_translate("Form", "No Image"))
        self.label_2.setText(_translate("Form", "No Image"))
        self.label_3.setText(_translate("Form", "No Image"))
        self.label_7.setText(_translate("Form", "No Image"))
        self.label_5.setText(_translate("Form", "No Image"))
        self.Back.setText(_translate("Form", "Back"))
        self.Add_2.setText(_translate("Form", "Add"))
        self.Show_3.setText(_translate("Form", "Show"))
        self.Dele_4.setText(_translate("Form", "Delete"))
