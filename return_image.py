from pieces import Pawn_Image,Queen_Image, Bishop_Image, Knight_Image, King_Image, Rook_Image
from PyQt6.QtGui import QPixmap


def return_image(piece, x, y, board):
    if piece.char() == 'B':
        a = Bishop_Image(x, y, board, piece.get_color())
        return a
    elif piece.char() == 'K':
        return King_Image(x, y,board, piece.get_color())
    elif piece.char() == 'N':
        return Knight_Image(x, y,board, piece.get_color())
    elif piece.char() == 'P':
        a = Pawn_Image(x, y,board, piece.get_color())
        return a
    elif piece.char() == 'R':
        return Rook_Image(x, y,board, piece.get_color())
    elif piece.char() == 'Q':
        return Queen_Image(x, y,board, piece.get_color())

def image_for_dice(char, label, color):
    if char == 'B':
        if color == 1:
            label.setPixmap(QPixmap('Images/wb.png'))
        else:
            label.setPixmap(QPixmap('Images/bb.png'))
    elif char == 'K':
        if color == 1:
            label.setPixmap(QPixmap('Images/wk.png'))
        else:
            label.setPixmap(QPixmap('Images/bk.png'))
    elif char == 'N':
        if color == 1:
            label.setPixmap(QPixmap('Images/wn.png'))
        else:
            label.setPixmap(QPixmap('Images/bn.png'))
    elif char == 'P':
        if color == 1:
            label.setPixmap(QPixmap('Images/wp.png'))
        else:
            label.setPixmap(QPixmap('Images/bp.png'))
    elif char == 'R':
        if color == 1:
            label.setPixmap(QPixmap('Images/wr.png'))
        else:
            label.setPixmap(QPixmap('Images/br.png'))
    elif char == 'Q':
        if color == 1:
            label.setPixmap(QPixmap('Images/wq.png'))
        else:
            label.setPixmap(QPixmap('Images/bq.png'))



