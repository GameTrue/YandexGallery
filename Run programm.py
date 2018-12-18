import sys
import json
from PyQt5.QtWidgets import QApplication
from conecting_files import Connector

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
# ex = MyWidget2()
# ex.show()
sys.exit(app.exec_())
