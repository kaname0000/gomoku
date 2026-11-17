from const import BOARD_SIZE

def ai_move(board):
    for y in range(BOARD_SIZE):
        for x in range(BOARD_SIZE):
            if board[y][x] == 0:
                return x, y
    return None, None