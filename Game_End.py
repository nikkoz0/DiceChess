from PyQt6.QtWidgets import QMainWindow, QLabel, QDialog
from PyQt6 import uic
import sqlite3


class End(QDialog):
    def __init__(self, winner, white_name, black_name):
        super().__init__()
        uic.loadUi('Ui/End_Game.ui', self)
        win = ['Чёрные', 'Белые']
        self.Deckstop_Button.clicked.connect(self.deckstop)
        self.Menu_Button.clicked.connect(self.menu)
        self.label.setText(f'Победили {win[winner]}')
        con = sqlite3.connect('statistics/statistics.db')
        print(white_name)
        print(black_name)
        cur = con.cursor()
        res_black = cur.execute("""SELECT * FROM statistics WHERE name = ? """, (black_name,))
        res_white = cur.execute("""SELECT * FROM statistics WHERE name = ? """, (white_name,))
        if [i for i in res_black]:
            if not (winner):
                cur.execute("""UPDATE statistics SET win = win + 1 WHERE name = ?""", (black_name,))
            else:
                cur.execute("""UPDATE statistics SET lose = lose + 1 WHERE name = ?""", (black_name,))
        else:
            if not (winner):
                cur.execute("""INSERT INTO statistics(name, win, lose) VALUES(?, 1, 0);""", (black_name,))
            else:
                cur.execute("""INSERT INTO statistics(name, win, lose) VALUES(?, 0, 1);""", (black_name,))

        if [i for i in res_white]:
            if winner:
                cur.execute("""UPDATE statistics SET win = win + 1 WHERE name = ?""", (white_name,))
            else:
                cur.execute("""UPDATE statistics SET lose = lose + 1 WHERE name = ?""", (white_name,))
        else:
            if winner:
                cur.execute("""INSERT INTO statistics(name, win, lose) VALUES(?, 1, 0);""", (white_name,))
            else:
                cur.execute("""INSERT INTO statistics(name, win, lose) VALUES(?, 0, 1);""", (white_name,))
        con.commit()
        cur.close()

    def deckstop(self):
        self.close()

    def menu(self):
        self.close()