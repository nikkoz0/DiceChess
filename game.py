import sys

from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget,
                             QHBoxLayout, QPushButton, QVBoxLayout, QLabel)
from PyQt6.QtCore import Qt
from PyQt6 import uic
from pieces import *
from chess import *

BOARD = Board()


class Chess(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 700, 700)
        self.setFixedSize(700, 700)
        central = QWidget()
        self.setCentralWidget(central)
        layout = QHBoxLayout(central)

        #self.box = QVBoxLayout(self)

        self.button = QPushButton()
        #self.dice_1 = QLabel(self)
        #self.dice_2 = QLabel(self)
        #self.dice_3 = QLabel(self)

        self.board = Board_Image(BOARD)

        #self.box.addWidget(self.dice_1)
        #self.box.addWidget(self.dice_2)
        #self.box.addWidget(self.dice_3)
        #self.box.addWidget(self.button)

        layout.addWidget(self.board)
        layout.addWidget(self.button)
        self.button.clicked.connect(self.move)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            x = event.pos().x()
            y = event.pos().y()

    def move(self):
        row, col = PIECE_CLICKED
        row1, col1 = PIECE_TO_MOVE
        BOARD.move_piece(row, col, row1, col1)
        self.board = Board_Image(BOARD)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Chess()
    ex.show()
    sys.exit(app.exec())
