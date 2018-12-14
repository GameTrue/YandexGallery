import sys
import json
from ProjectStarting import Ui_Form1
from ProjectStarting import Ui_Form2
from ProjectStarting import Ui_Form3
from ProjectStarting import Ui_Form4
from PyQt5.QtWidgets import QApplication, QMainWindow
from PIL import Image
from PIL.ImageQt import ImageQt
from PyQt5 import QtGui, QtCore


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
        self.in_2.clicked.connect(self.log)
        self.Back_2.clicked.connect(self.con.dia)
        self.Exit_2.clicked.connect(self.close)

    def log(self):
        global login
        with open('data.json', 'r') as out_file2:
            data = json.load(out_file2)
            # print(data)
            # print(self.login_2.text())
            # print(self.passw_2.text())
            if self.login_2.text() in data[0]:
                if self.passw_2.text() in data[0][self.login_2.text()]:
                    login = self.login_2.text()
                    self.con.dia3()
                else:
                    self.err_2.setText('!!!WRONG PASSWORD!!!')
            else:
                self.err_2.setText('!!!LOGIN NOT FOUND!!!')


class MyWidget2(QMainWindow, Ui_Form3):
    def __init__(self, con):
        self.con = con
        super().__init__()
        self.setupUi(self)
        self.in_3.clicked.connect(self.con.dia1)
        self.rg_3.clicked.connect(self.reg)
        self.Back_3.clicked.connect(self.con.dia1)
        self.Exit_3.clicked.connect(self.close)

    def reg(self):
        if len(self.login_3.text()) > 3:
            if len(self.passw_3.text()) > 7:
                with open('data.json', 'r') as out_file1:
                    datas = json.load(out_file1)
                if self.login_3.text() not in datas[0]:
                    with open('data.json', 'w') as out_file:
                        datas[0][self.login_3.text()] = self.passw_3.text()
                        # print(datas)
                        json.dump(datas, out_file, sort_keys=True, indent=4)
                else:
                    self.login_3.setText('')
                    self.passw_3.setText('')
                    self.err_3.setText('This ID is already being used.')
            else:
                self.login_3.setText('')
                self.passw_3.setText('')
                self.err_3.setText("New password must be at least %d characters." % 8)
        else:
            self.login_3.setText('')
            self.passw_3.setText('')
            self.err_3.setText("New login must be at least %d characters." % 4)


class MyWidget3(QMainWindow, Ui_Form4):
    def __init__(self, con):
        self.con = con
        super().__init__()
        self.setupUi(self)
        self.Back.clicked.connect(self.con.dia1)
        self.Exit.clicked.connect(self.close)
        self.Add_2.clicked.connect(self.Add_Image)

    def Add_Image(self):
        global login
        with open('data.json', 'r') as out_file2:
            dataf = json.load(out_file2)
        if login not in dataf[1]:
            dataf[1][login] = [[] for _ in range(9)]
            print(dataf)
        im = Image.open(self.login_4.text())
        pixels = im.load()
        x, y = im.size
        data = []
        for i in range(x):
            data.append([])
            for j in range(y):
                r, g, b = pixels[i, j]
                data[i].append([r, g, b])
        print(login)
        print(data)
        dataf[1][login][self.Value_2.value()].append([x, y])
        dataf[1][login][self.Value_2.value()].append(data)
        print(pixels)
        with open('data.json', 'w') as out_file:
            print(dataf)
            json.dump(dataf, out_file, sort_keys=True, indent=4)
        data1 = [self.label, self.label_2, self.label_3, self.label_4, self.label_5, self.label_6, self.label_7, self.label_8, self.label_9]
        qim = ImageQt(im)
        pix = QtGui.QPixmap.fromImage(qim)
        pix = pix.scaled(131, 91, QtCore.Qt.KeepAspectRatio)
        data1[self.Value_2.value() - 1].setPixmap(pix)



class Connector:
    def __init__(self):
        self.form = MyWidget(self)
        self.form1 = MyWidget1(self)
        self.form2 = MyWidget2(self)
        self.form3 = MyWidget3(self)

    def dia(self):
        self.exit()
        self.form.show()

    def dia1(self):
        self.exit()
        self.form1.show()

    def dia2(self):
        self.exit()
        self.form2.show()

    def dia3(self):
        self.exit()
        self.form3.show()

    def exit(self):
        lis = [self.form, self.form1, self.form2, self.form3]
        for x in lis:
            try:
                x.close()
            except Exception:
                pass


# def con(n):
#     data2.append(data[n]())
#     # ex = data[n]()
#     data2[-1].show()


# data = [MyWidget, MyWidget1, MyWidget2]
# data2 = []
app = QApplication(sys.argv)
try:
    with open('data.json', 'x') as out_file:
        dat = []
        dat.append({'1': '1'})
        dat.append({})
        json.dump(dat, out_file, sort_keys=True, indent=4)
except Exception:
    try:
        with open('data.json', 'r') as out_file:
            data = json.load(out_file)
    except Exception:
        with open('data.json', 'w') as out_file:
            dat = []
            dat.append({'1': '1'})
            dat.append({})
            json.dump(dat, out_file, sort_keys=True, indent=4)
login = '1'
connector = Connector()
connector.dia()
# ex = MyWidget2()
# ex.show()
sys.exit(app.exec_())
