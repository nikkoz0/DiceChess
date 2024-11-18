from PyQt6.QtWidgets import QWidget, QGridLayout, QLabel
from PyQt6.QtGui import QPainter, QPixmap
from PyQt6.QtCore import Qt
from chess import *


PIECE_CLICKED = [None, None]
PIECE_TO_MOVE = [None, None]


class Piece_Image(QLabel):
    def __init__(self, x, y, board):
        self.x = x
        self.y = y
        self.board = board
        super().__init__()

    def paintEvent(self, event):
        qp = QPainter(self)
        size = min(self.width(), self.height())
        qp.drawPixmap(0, 0, self.image.scaled(size, size, Qt.AspectRatioMode.KeepAspectRatio))

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            if (PIECE_CLICKED[0] is None):
                PIECE_CLICKED[0] = self.x
                PIECE_CLICKED[1] = self.y
            else:
                piece = self.board.get_piece(PIECE_CLICKED[0], PIECE_CLICKED[1])
                piece_2 = self.board.get_piece(self.x, self.y)
                if piece is None:
                    PIECE_CLICKED[0] = self.x
                    PIECE_CLICKED[1] = self.y
                else:
                    if piece_2.get_color() == piece.get_color():
                        PIECE_CLICKED[0] = self.x
                        PIECE_CLICKED[1] = self.y
                    else:
                        PIECE_TO_MOVE[0] = self.x
                        PIECE_TO_MOVE[1] = self.y



class Pawn_Image(Piece_Image):
    def __init__(self, x, y, board, color):
        super().__init__(x, y, board)
        if color == WHITE:
            self.image = QPixmap('Images/wp.png')
        else:
            self.image = QPixmap('Images/bp.png')


class King_Image(Piece_Image):
    def __init__(self, x, y,board, color):
        super().__init__(x, y, board)
        if color == WHITE:
            self.image = QPixmap('Images/wk.png')
        else:
            self.image = QPixmap('Images/bk.png')


class Queen_Image(Piece_Image):
    def __init__(self, x, y, board, color):
        super().__init__(x, y, board)
        if color == WHITE:
            self.image = QPixmap('Images/wq.png')
        else:
            self.image = QPixmap('Images/bq.png')


class Rook_Image(Piece_Image):
    def __init__(self, x, y, board, color):
        super().__init__(x, y, board)
        if color == WHITE:
            self.image = QPixmap('Images/wr.png')
        else:
            self.image = QPixmap('Images/br.png')


class Bishop_Image(Piece_Image):
    def __init__(self, x, y, board,  color):
        super().__init__(x, y, board)
        if color == WHITE:
            self.image = QPixmap('Images/wb.png')
        else:
            self.image = QPixmap('Images/bb.png')


class Knight_Image(Piece_Image):
    def __init__(self, x, y, board, color):
        super().__init__(x, y,board)
        if color == WHITE:
            self.image = QPixmap('Images/wn.png')
        else:
            self.image = QPixmap('Images/bn.png')


class Empty(QLabel):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        super().__init__()

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            if not PIECE_CLICKED[0] is None:
                PIECE_TO_MOVE[0] = self.x
                PIECE_TO_MOVE[1] = self.y


class Board_Image(QWidget):
    def __init__(self, board):
        super().__init__()
        self.layout = QGridLayout(self)
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.autoFillBackground = QPixmap('Images/desk.png')

        for row in range(8):
            for col in range(8):
                piece = board.get_piece(row, col)
                row1 = 7 - row
                if piece:
                    if piece.char() == 'P':
                        self.layout.addWidget(Pawn_Image(row, col, board, piece.get_color()), row1, col)
                    elif piece.char() == 'Q':
                        self.layout.addWidget(Queen_Image(row, col,board,  piece.get_color()), row1, col)
                    elif piece.char() == 'K':
                        self.layout.addWidget(King_Image(row, col,board,  piece.get_color()), row1, col)
                    elif piece.char() == 'N':
                        self.layout.addWidget(Knight_Image(row, col,board, piece.get_color()), row1, col)
                    elif piece.char() == 'B':
                        self.layout.addWidget(Bishop_Image(row, col,board, piece.get_color()), row1, col)
                    elif piece.char() == 'R':
                        self.layout.addWidget(Rook_Image(row, col,board, piece.get_color()), row1, col)
                else:
                    self.layout.addWidget(Empty(row, col), row1, col)
    def paintEvent(self, event):
        qp = QPainter(self)
        rect = self.layout.geometry()
        qp.drawPixmap(rect, self.autoFillBackground.scaled(rect.size(),
                                                           Qt.AspectRatioMode.KeepAspectRatio))

