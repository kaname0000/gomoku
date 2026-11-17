from const import BOARD_SIZE

def check_win(board, stone):
    """
    Check if the specified stone (1: Black, 2: White) has won 
    by aligning 5 stones horizontally, vertically, or diagonally.
    """
    # Directions: (dx, dy) -> Right, Down, Down-Right, Up-Right
    directions = [
        (1, 0),   # Horizontal
        (0, 1),   # Vertical
        (1, 1),   # Diagonal (\)
        (1, -1)   # Diagonal (/)
    ]

    for y in range(BOARD_SIZE):
        for x in range(BOARD_SIZE):
            # If the current cell doesn't match the stone, skip
            if board[y][x] != stone:
                continue

            for dx, dy in directions:
                count = 0
                for i in range(5):
                    nx = x + dx * i
                    ny = y + dy * i

                    # Check if coordinates are within the board and match the stone
                    if 0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE and board[ny][nx] == stone:
                        count += 1
                    else:
                        break

                # If 5 stones are aligned, return True (Win)
                if count == 5:
                    return True

    return False