import sqlite3

from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem


class Statistics_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(600, 400)
        uic.loadUi('Ui/statistics.ui', self)
        self.con = sqlite3.connect('statistics/statistics.db')
        cur = self.con.cursor()
        result = cur.execute("""SELECT * FROM statistics""").fetchall()
        if not result:
            self.statusBar().showMessage('Пока игроков нет')
            return
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))
        self.titles =[description[0] for description in cur.description]
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        self.setWindowTitle('Статистика игр')



