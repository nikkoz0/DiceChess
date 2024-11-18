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
        self.tableWidget.setRowCount(len(result))
        if result:
            for i, row in enumerate(result):
                self.tableWidget.setRowCount(
                    self.tableWidget.rowCount() + 1)
                for j, elem in enumerate(row):
                    self.tableWidget.setItem(
                        i, j, QTableWidgetItem(str(elem)))
        self.setWindowTitle('Статистика игр')



