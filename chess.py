WHITE = 1
BLACK = 2


def opponent(color):
    if color == WHITE:
        return BLACK
    else:
        return WHITE


def correct_coords(row, col):
    return 0 <= row < 8 and 0 <= col < 8


class Board:
    def __init__(self):
        self.color = WHITE
        self.field = []
        for row in range(8):
            self.field.append([None] * 8)

        self.field[0] = [
            Rook(WHITE), Knight(WHITE), Bishop(WHITE), Queen(WHITE),
            King(WHITE), Bishop(WHITE), Knight(WHITE), Rook(WHITE)
        ]
        self.field[1] = [
            Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE),
            Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE)
        ]
        self.field[6] = [
            Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK),
            Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK)
        ]
        self.field[7] = [
            Rook(BLACK), Knight(BLACK), Bishop(BLACK), Queen(BLACK),
            King(BLACK), Bishop(BLACK), Knight(BLACK), Rook(BLACK)
        ]

    def current_player_color(self):
        return self.color

    def cell(self, row, col):
        piece = self.field[row][col]
        if piece is None:
            return ' '
        color = piece.get_color()
        c = 'w' if color == WHITE else 'b'
        return c + piece.char()

    def get_piece(self, row, col):
        if correct_coords(row, col):
            return self.field[row][col]
        else:
            return None

    def move_piece(self, row, col, row1, col1):
        '''Переместить фигуру из точки (row, col) в точку (row1, col1).
        Если перемещение возможно, метод выполнит его и вернёт True.
        Если нет --- вернёт False'''

        if not correct_coords(row, col) or not correct_coords(row1, col1):
            return False
        if row == row1 and col == col1:
            return False  # нельзя пойти в ту же клетку
        piece = self.field[row][col]
        if piece is None:
            return False
        if piece.get_color() != self.color:
            return False
        if (not (piece.can_move(self, row, col, row1, col1)) and
                not (piece.can_attack(self, row, col, row1, col1))):
            return False
        self.field[row][col] = None
        self.field[row1][col1] = piece
        return True

    def move_and_promote_pawn(self, row, col, row1, col1, char):
        if char in 'QRBN' and not (self.get_piece(row, col) is None):
            piece = self.get_piece(row, col)
            if piece.char() != 'P':
                return False
            if piece.can_move(self.field, row, col, row1, col1) or piece.can_attack(self.field, row, col, row1, col1):
                if piece.can_move(self.field, row, col, row1, col1):
                    if not (self.field[row1][col1] is None):
                        return False
                self.field[row][col] = None
                color = piece.get_color()
                if char == 'Q':
                    self.field[row1][col1] = Queen(color)
                elif char == 'R':
                    self.field[row1][col1] = Rook(color)
                elif char == 'B':
                    self.field[row1][col1] = Bishop(color)
                else:
                    self.field[row1][col1] = Knight(color)
                return True
        return False


class Queen:
    def __init__(self, color):
        self.color = color

    def can_move(self, board, row, col, row1, col1):
        if correct_coords(row1, col1):
            step_row = 1 if (row1 >= row) else -1
            step_col = 1 if (col1 >= col) else -1
            piece1 = board.get_piece(row1, col1)
            if not (piece1 is None):
                if piece1.get_color() == self.color:
                    return False
            if row == row1 or col == col1:
                for c in range(col + step_col, col1, step_col):
                    piece_1 = board.get_piece(row, c)
                    if not (piece_1 is None):
                        return False
                for r in range(row + step_row, row1, step_row):
                    piece_1 = board.get_piece(r, col)
                    if not (piece_1 is None):
                        return False
                return True
            else:
                if abs(row - row1) != abs(col - col1):
                    return False
                if row - col == row1 - col1:
                    for r in range(row + step_row, row1, step_row):
                        c = col - row + r
                        piece_1 = board.get_piece(r, c)
                        if not (piece_1 is None):
                            return False
                else:
                    for r in range(row + step_row, row1, step_row):
                        c = col + row - r
                        piece_1 = board.get_piece(r, c)
                        if not (piece_1 is None):
                            return False
                return True
        return False

    def get_color(self):
        return self.color

    def char(self):
        return 'Q'

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)


class Rook:

    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def char(self):
        return 'R'

    def can_move(self, board, row, col, row1, col1):
        if row != row1 and col != col1:
            return False
        piece1 = board.get_piece(row1, col1)
        if not (piece1 is None):
            if piece1.get_color() == self.color:
                return False

        step = 1 if (row1 >= row) else -1
        for r in range(row + step, row1, step):
            # Если на пути по горизонтали есть фигура
            if not (board.get_piece(r, col) is None):
                return False

        step = 1 if (col1 >= col) else -1
        for c in range(col + step, col1, step):
            if not (board.get_piece(row, c) is None):
                return False

        return True

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)


class Pawn:

    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def char(self):
        return 'P'

    def can_move(self, board, row, col, row1, col1):
        if col != col1:
            return False

        if self.color == WHITE:
            direction = 1
            start_row = 1
        else:
            direction = -1
            start_row = 6

        # ход на 1 клетку
        if row + direction == row1:
            return True

        piece1 = board.get_piece(row1, col1)
        if not (piece1 is None):
            if piece1.get_color() == self.color:
                return False

        if (row == start_row
                and row + 2 * direction == row1
                and board.field[row + direction][col] is None):
            return True

        return False

    def can_attack(self, board, row, col, row1, col1):
        direction = 1 if (self.color == WHITE) else -1
        a = (row + direction == row1 and (col + 1 == col1 or col - 1 == col1))
        piece = board.get_piece(row1, col1)
        if piece is None:
            return a
        color = piece.get_color()
        b = color != self.color
        return a and b


class Knight:

    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def char(self):
        return 'N'

    def can_move(self, board, row, col, row1, col1):
        if correct_coords(row1, col1):
            if abs(row1 - row) == 2 and abs(col1 - col) == 1 or (
                    abs(row1 - row) == 1 and abs(col1 - col) == 2):
                piece = board.get_piece(row1, col1)
                if not(piece is None):
                    if piece.get_color() == self.get_color():
                        return False

                return True

        return False

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)


class King:

    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def char(self):
        return 'K'

    def can_move(self, board, row, col, row1, col1):
        if correct_coords(row1, col1):
            if (abs(row - row1) == 1 and abs(col - col1) == 0 ) or (abs(col - col1) == 1 and abs(row - row1) == 0) or (abs(row - row1) == 1 and abs(col - col1) == 1):
                piece = board.get_piece(row1, col1)
                if not(piece is None):
                    if piece.get_color() == self.get_color():
                        return False
                return True

        return False

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)


class Bishop:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def char(self):
        return 'B'

    def can_move(self, board, row, col, row1, col1):
        if correct_coords(row1, col1):
            piece1 = board.get_piece(row1, col1)
            if not (piece1 is None):
                if piece1.get_color() == self.color:
                    return False

            if abs(row - row1) != abs(col - col1):
                return False
            step_row = 1 if (row1 >= row) else -1
            if row - col == row1 - col1:
                for r in range(row + step_row, row1, step_row):
                    c = col - row + r
                    piece_1 = board.get_piece(r, c)
                    if not (piece_1 is None):
                        return False
            else:
                for r in range(row + step_row, row1, step_row):
                    c = col + row - r
                    piece_1 = board.get_piece(r, c)
                    if not (piece_1 is None):
                        return False
            return True
        return False

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)