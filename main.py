import sys

from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic
from PyQt6.QtGui import QPixmap, QPainter
from PyQt6.QtCore import Qt
from statistic import Statistics_Window
from game import Chess
from rule import Rule


class Main_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(450, 500)
        uic.loadUi('Ui/Main_Window.ui', self)
        self.play_button.clicked.connect(self.play)
        self.rule_button.clicked.connect(self.rule)
        self.statistic_button.clicked.connect(self.statistic)
        self.setStyleSheet('.QWidget {background-image: url(Images/background.jpg);}')
        self.setWindowTitle('Меню')

    def play(self):
        self.ChessWindow = Chess()
        self.ChessWindow.show()
        self.hide()

    def rule(self):
        self.RuleWindow = Rule()
        self.RuleWindow.show()

    def statistic(self):
        self.StatisiticsWindow = Statistics_Window()
        self.StatisiticsWindow.show()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main_Window()
    ex.show()
    sys.exit(app.exec())