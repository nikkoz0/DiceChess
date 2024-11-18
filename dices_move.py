def can_move(board, color, dices):
    flag = False
    for row in range(7, -1, -1):
        for col in range(8):
            piece = board.get_piece(row, col)
            if piece:
                if piece.char() in dices:
                    if piece.get_color() == color:
                        for row1 in range(7, -1, -1):
                            for col1 in range(8):
                                if piece.can_move(board, row, col, row1, col1):
                                    flag = True
                                    return flag
    return flag