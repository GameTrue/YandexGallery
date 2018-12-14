# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frst.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 380)
        self.Exit_3 = QtWidgets.QPushButton(Form)
        self.Exit_3.setGeometry(QtCore.QRect(260, 170, 151, 31))
        self.Exit_3.setObjectName("Exit_3")
        self.credits_2 = QtWidgets.QPushButton(Form)
        self.credits_2.setGeometry(QtCore.QRect(260, 130, 151, 31))
        self.credits_2.setObjectName("credits_2")
        self.login_3 = QtWidgets.QPushButton(Form)
        self.login_3.setGeometry(QtCore.QRect(260, 90, 151, 31))
        self.login_3.setObjectName("login_3")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(150, 230, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Exit_3.setText(_translate("Form", "Exit"))
        self.credits_2.setText(_translate("Form", "Credits"))
        self.login_3.setText(_translate("Form", "Login"))
        self.label.setText(_translate("Form", "Author and creator of this project: Alexander Fomin"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

