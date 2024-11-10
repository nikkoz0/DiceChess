import sys

from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget,
                             QHBoxLayout, QPushButton, QVBoxLayout, QLabel)
from PyQt6 import uic
from pieces import Board_Image


class Chess(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 700, 700)
        self.setFixedSize(700, 700)
        central = QWidget()
        self.setCentralWidget(central)
        layout = QHBoxLayout(central)

        #self.box = QVBoxLayout(self)

        #self.button = QPushButton()
        #self.dice_1 = QLabel(self)
        #self.dice_2 = QLabel(self)
        #self.dice_3 = QLabel(self)

        self.board = Board_Image()

        #self.box.addWidget(self.dice_1)
        #self.box.addWidget(self.dice_2)
        #self.box.addWidget(self.dice_3)
        #self.box.addWidget(self.button)

        layout.addWidget(self.board)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Chess()
    ex.show()

    sys.exit(app.exec())
