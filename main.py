import sys

from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic


class Main_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(450, 500)
        uic.loadUi('Ui/Main_Window.ui', self)
        self.play_button.clicked.connect(self.play)
        self.rule_button.clicked.connect(self.rule)
        self.statistic_button.clicked.connect(self.statistic)

    def play(self):
        pass

    def rule(self):
        pass

    def statistic(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main_Window()
    ex.show()
    sys.exit(app.exec())