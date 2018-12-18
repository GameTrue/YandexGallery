import sys
import json
from dialog1 import Ui_Form1
from dialog2 import Ui_Form2
from dialog3 import Ui_Form3
from dialog4 import Ui_Form4
from PyQt5.QtWidgets import QMainWindow
from PIL import Image
from PIL.ImageQt import ImageQt
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication


class MyWidget(QMainWindow, Ui_Form1):
    def __init__(self, con):
        self.flg = True
        self.con = con
        super().__init__()
        self.setupUi(self)
        self.login_3.clicked.connect(self.con.dia1)
        self.Exit_3.clicked.connect(self.close)
        self.credits_2.clicked.connect(self.cred)

    def cred(self):
        self.label.setVisible(self.flg)
        if self.flg is True:
            self.flg = False
        else:
            self.flg = True


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
            if self.login_2.text() in data[0]:
                if self.passw_2.text() == data[0][self.login_2.text()]:
                    login = self.login_2.text()
                    self.login_2.setText('')
                    self.passw_2.setText('')
                    self.err_2.setText('')
                    self.con.dia3()
                else:
                    self.passw_2.setText('')
                    self.err_2.setText('!!!WRONG PASSWORD!!!')
            else:
                self.login_2.setText('')
                self.passw_2.setText('')
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
                        self.err_3.setText('')
                        json.dump(datas, out_file, sort_keys=True, indent=4)
                        self.login_3.setText('')
                        self.passw_3.setText('')
                        # self.con.dia1
                else:
                    self.login_3.setText('')
                    self.passw_3.setText('')
                    self.err_3.setText('This ID is already being used.')
            else:
                self.passw_3.setText('')
                self.err_3.setText("New password must be at least %d characters." % 8)
        else:
            self.login_3.setText('')
            self.passw_3.setText('')
            self.err_3.setText("New login must be at least %d characters." % 4)


class MyWidget3(QMainWindow, Ui_Form4):
    def __init__(self, con):
        global data2
        self.flg = True
        self.con = con
        super().__init__()
        self.setupUi(self)
        self.Back.clicked.connect(self.con.dia1)
        self.Exit.clicked.connect(self.close)
        self.Add_2.clicked.connect(self.Add_Image)
        self.Show_3.clicked.connect(self.BigIm)
        self.Dele_4.clicked.connect(self.deleted)
        try:
            with open('data.json', 'r') as oute:
                datak = json.load(oute)
                if datak[0]['FARELE']:
                    data2 = [self.label, self.label_2, self.label_3, self.label_4, self.label_5, self.label_6,
                             self.label_7,
                             self.label_8, self.label_9]
                    datak[0]['FARELE'] = False
                    with open('data.json', 'w') as inte:
                        json.dump(datak, inte, sort_keys=True, indent=4)
        except Exception as f:
            print(f)
        try:
            data = [self.label, self.label_2, self.label_3, self.label_4, self.label_5, self.label_6, self.label_7,
                    self.label_8, self.label_9]
            with open('data.json', 'r') as out_file2:
                dataf = json.load(out_file2)
            for i in range(9):
                if dataf[1][login][i][1]:
                    x, y = dataf[1][login][i][0]
                    im = Image.new('RGB', (x, y), 'white')
                    pixels2 = im.load()
                    for j in range(x):
                        for k in range(y):
                            r, g, b = dataf[1][login][i][1][j][k]
                            pixels2[j, k] = r, g, b
                    im.save('im.png')
                    qim = ImageQt(im)
                    pix = QtGui.QPixmap.fromImage(qim)
                    pix = pix.scaled(131, 91, QtCore.Qt.KeepAspectRatio)
                    data[i].setPixmap(pix)
        except Exception as a:
            print(a)

    def deleted(self):
        global data2
        try:
            with open('data.json', 'r') as out_file2:
                dat = [self.label, self.label_2, self.label_3, self.label_4, self.label_5, self.label_6, self.label_7,
                       self.label_8, self.label_9]
                data = json.load(out_file2)
                with open('data.json', 'w') as out_file3:
                    if data[1][login][self.Value.value() - 1][1]:
                        data[1][login][self.Value.value() - 1] = [[], [], []]
                        connector.dia3()
                        json.dump(data, out_file3, sort_keys=True, indent=4)
        except Exception as a:
            print('Delete:', a)

    def BigIm(self):
        try:
            if self.flg:
                data = [self.label, self.label_2, self.label_3, self.label_4, self.label_5, self.label_6, self.label_7,
                        self.label_8, self.label_9]
                with open('data.json', 'r') as out_file2:
                    dataf = json.load(out_file2)
                try:
                    if dataf[1][login][self.Value.value() - 1][1] and dataf[1][login][self.Value.value() - 1][0] and \
                            dataf[1][login][self.Value.value() - 1][2]:
                        for x in data:
                            x.setVisible(False)
                        x, y = dataf[1][login][self.Value.value() - 1][0]
                        im = Image.new('RGB', (x, y), 'white')
                        pixels2 = im.load()
                        for j in range(x):
                            for k in range(y):
                                r, g, b = dataf[1][login][self.Value.value() - 1][1][j][k]
                                pixels2[j, k] = r, g, b
                        qim = ImageQt(im)
                        pix = QtGui.QPixmap.fromImage(qim)
                        pix = pix.scaled(431, 311, QtCore.Qt.KeepAspectRatio)
                        self.label_10.setPixmap(pix)
                        self.label_10.setVisible(True)
                        if self.flg is True:
                            self.flg = False
                        else:
                            self.flg = True
                except Exception as a:
                    print(a)
            else:
                try:
                    data = [self.label, self.label_2, self.label_3, self.label_4, self.label_5, self.label_6,
                            self.label_7,
                            self.label_8, self.label_9]
                    for x in data:
                        x.setVisible(True)
                    self.label_10.setVisible(False)
                    if self.flg is True:
                        self.flg = False
                    else:
                        self.flg = True
                except Exception as a:
                    print(a)
        except Exception as a:
            print('Show:', a)

    def Add_Image(self):
        global login
        try:
            with open('data.json', 'r') as out_file2:
                dataf = json.load(out_file2)
            if login not in dataf[1]:
                dataf[1][login] = [[[], [], []] for _ in range(9)]
            im = Image.open(self.login_4.text())
            pixels = im.load()
            x, y = im.size
            data = []
            for i in range(x):
                data.append([])
                for j in range(y):
                    r, g, b = pixels[i, j]
                    data[i].append([r, g, b])
            dataf[1][login][self.Value_2.value() - 1][0] = [x, y]
            dataf[1][login][self.Value_2.value() - 1][1] = data
            # print(pixels)
            data1 = [self.label, self.label_2, self.label_3, self.label_4, self.label_5, self.label_6, self.label_7,
                     self.label_8, self.label_9]
            qim = ImageQt(im)
            pix = QtGui.QPixmap.fromImage(qim)
            pix = pix.scaled(131, 91, QtCore.Qt.KeepAspectRatio)
            data1[self.Value_2.value() - 1].setPixmap(pix)
            dataf[1][login][self.Value_2.value() - 1][2] = self.login_4.text()
            with open('data.json', 'w') as out_file:
                print(dataf)
                json.dump(dataf, out_file, sort_keys=True, indent=4)
        except Exception:
            pass


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
        self.form3 = MyWidget3(self)
        self.form3.show()

    def exit(self):
        lis = [self.form, self.form1, self.form2, self.form3]
        for x in lis:
            try:
                x.close()
            except Exception as d:
                print(d)


data2 = []
login = '1'
app = QApplication(sys.argv)
try:
    with open('data.json', 'x') as out_file:
        dat = []
        dat.append({'1': '1', 'FARELE': True})
        dat.append({})
        json.dump(dat, out_file, sort_keys=True, indent=4)
except Exception:
    try:
        with open('data.json', 'r') as out_file:
            data = json.load(out_file)
    except Exception:
        with open('data.json', 'w') as out_file:
            dat = []
            dat.append({'1': '1', 'FARELE': True})
            dat.append({})
            json.dump(dat, out_file, sort_keys=True, indent=4)
connector = Connector()
connector.dia()
sys.exit(app.exec_())
