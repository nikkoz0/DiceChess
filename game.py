import random

from PyQt6.QtWidgets import (QMainWindow,
                             QHBoxLayout, QPushButton, QVBoxLayout,)
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon
from pieces import *
from return_image import return_image, image_for_dice
from chess import Board
from Game_End import End
from dices_move import can_move

all_pieces = ['Q', 'P', 'N', 'K', 'B', 'R']


class Chess(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 700, 700)
        self.setFixedSize(1000, 700)
        self.central = QWidget()
        self.setCentralWidget(self.central)
        self.layout = QHBoxLayout(self.central)
        self.piece_can_move = []

        self.box = QVBoxLayout(self)

        self.button = QPushButton()
        self.button.setFixedSize(300, 200)
        self.button.setIcon(QIcon('Images/button.png'))
        self.button.setIconSize(QSize(300, 200))

        self.dice_1 = QLabel(self)
        self.dice_2 = QLabel(self)
        self.dice_3 = QLabel(self)
        self.dices = []

        self.b = Board()
        self.board = Board_Image(self.b)

        self.box.addWidget(self.dice_1)
        self.box.addWidget(self.dice_2)
        self.box.addWidget(self.dice_3)
        self.box.addWidget(self.button)

        self.layout.addWidget(self.board)
        self.layout.addLayout(self.box)
        self.button.clicked.connect(self.but)
        self.setWindowTitle('Игра')

    def but(self):
        if not (self.dices):
            color = self.b.current_player_color()
            p_1 = random.choice(all_pieces)
            p_2 = random.choice(all_pieces)
            p_3 = random.choice(all_pieces)
            self.dices = [p_1, p_2, p_3]
            image_for_dice(p_1, self.dice_1, color)
            image_for_dice(p_2, self.dice_2, color)
            image_for_dice(p_3, self.dice_3, color)
            if not (can_move(self.b, color, self.dices)):
                self.dices = []
                self.b.color = opponent(color)

    def mouseReleaseEvent(self, event):
        desk = []
        color = self.b.current_player_color()
        row, col = PIECE_CLICKED
        row1, col1 = PIECE_TO_MOVE
        if not (row1 is None) and not (row is None):
            piece_1 = self.b.get_piece(row, col)
            piece_2 = self.b.get_piece(row1, col1)
            if piece_2:
                if piece_1.can_attack(self.b, row, col, row1, col1) and piece_1.char() in self.dices:
                    piece_to_remove = self.board.layout.itemAtPosition(7 - row, col)
                    self.board.layout.removeWidget(piece_to_remove.widget())
                    piece_image_1 = return_image(piece_1, row1, col1, self.b)
                    piece_to_remove = self.board.layout.itemAtPosition(7 - row1, col1)
                    self.board.layout.removeWidget(piece_to_remove.widget())
                    self.board.layout.addWidget(piece_image_1, 7 - row1, col1)
                    self.board.layout.addWidget(Empty(row, col), 7 - row, col)
                    self.b.move_piece(row, col, row1, col1)
                    self.dices.remove(piece_1.char())
            else:
                if piece_1.can_move(self.b, row, col, row1, col1) and piece_1.char() in self.dices:
                    piece_to_remove = self.board.layout.itemAtPosition(7 - row, col)
                    self.board.layout.removeWidget(piece_to_remove.widget())
                    piece_to_remove = self.board.layout.itemAtPosition(7 - row1, col1)
                    self.board.layout.removeWidget(piece_to_remove.widget())
                    piece_image_1 = return_image(piece_1, row1, col1, self.b)
                    self.board.layout.addWidget(piece_image_1, 7 - row1, col1)
                    self.board.layout.addWidget(Empty(row, col), 7 - row, col)
                    self.b.move_piece(row, col, row1, col1)
                    self.dices.remove(piece_1.char())

            if not (can_move(self.b, color, self.dices)):
                self.dices = []
                self.b.color = opponent(color)

            for row in range(7, -1, -1):
                for col in range(8):
                    cell = self.b.cell(row, col)
                    cell = cell if cell != ' ' else '-'
                    desk.append(cell)
            if 'wK' not in desk or 'bK' not in desk:
                self.setEnabled(False)
                if 'wk' not in desk:
                    end = End(0)
                else:
                    end = End(1)
                end.show()
