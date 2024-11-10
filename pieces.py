from PyQt6.QtWidgets import QWidget, QGridLayout, QLabel
from PyQt6.QtGui import QPainter, QPixmap
from PyQt6.QtCore import Qt
from chess import *


class Piece_Image(QLabel):
    def __init__(self, color):
        super().__init__()

    def paintEvent(self, event):
        qp = QPainter(self)
        size = min(self.width(), self.height())
        qp.drawPixmap(0, 0, self.image.scaled(size, size, Qt.AspectRatioMode.KeepAspectRatio))

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            pass



class Pawn_Image(Piece_Image):
    def __init__(self, color):
        super().__init__(color)
        if color == WHITE:
            self.image = QPixmap('Images/wp.png')
        else:
            self.image = QPixmap('Images/bp.png')


class King_Image(Piece_Image):
    def __init__(self, color):
        super().__init__(color)
        if color == WHITE:
            self.image = QPixmap('Images/wk.png')
        else:
            self.image = QPixmap('Images/bk.png')


class Queen_Image(Piece_Image):
    def __init__(self, color):
        super().__init__(color)
        if color == WHITE:
            self.image = QPixmap('Images/wq.png')
        else:
            self.image = QPixmap('Images/bq.png')


class Rook_Image(Piece_Image):
    def __init__(self, color):
        super().__init__(color)
        if color == WHITE:
            self.image = QPixmap('Images/wr.png')
        else:
            self.image = QPixmap('Images/br.png')


class Bishop_Image(Piece_Image):
    def __init__(self, color):
        super().__init__(color)
        if color == WHITE:
            self.image = QPixmap('Images/wb.png')
        else:
            self.image = QPixmap('Images/bb.png')


class Knight_Image(Piece_Image):
    def __init__(self, color):
        super().__init__(color)
        if color == WHITE:
            self.image = QPixmap('Images/wn.png')
        else:
            self.image = QPixmap('Images/bn.png')


class Empty(QLabel):
    def __init__(self):
        super().__init__()


class Board_Image(QWidget):
    def __init__(self, board):
        super().__init__()
        layout = QGridLayout(self)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        self.autoFillBackground = QPixmap('Images/desk.png')

        for i in range(8):
            layout.setRowStretch(i, 1)
            layout.setColumnStretch(i, 1)

        for row in range(8):
            for col in range(8):
                piece = board.get_piece(row, col)
                if piece:
                    row1 = 7 - row
                    if piece.char() == 'P':
                        layout.addWidget(Pawn_Image(piece.get_color()), row1, col)
                    elif piece.char() == 'Q':
                        layout.addWidget(Queen_Image(piece.get_color()), row1, col)
                    elif piece.char() == 'K':
                        layout.addWidget(King_Image(piece.get_color()), row1, col)
                    elif piece.char() == 'N':
                        layout.addWidget(Knight_Image(piece.get_color()), row1, col)
                    elif piece.char() == 'B':
                        layout.addWidget(Bishop_Image(piece.get_color()), row1, col)
                    elif piece.char() == 'R':
                        layout.addWidget(Rook_Image(piece.get_color()), row1, col)
                else:
                    row1 = 7 - row
                    layout.addWidget(Empty(), row1, col)

    def paintEvent(self, event):
        qp = QPainter(self)
        rect = self.layout().geometry()
        qp.drawPixmap(rect, self.autoFillBackground.scaled(rect.size(),
                                                           Qt.AspectRatioMode.KeepAspectRatio))
