import pygame
import sys
from const import (
    WINDOW_SIZE, MARGIN, BOARD_SIZE, GRID_SIZE,
    COLOR_BOARD, COLOR_LINE, COLOR_STAR, COLOR_BLACK, COLOR_WHITE
)
from ai import ai_move
from judge import check_win

def draw_board(screen, board):
    screen.fill(COLOR_BOARD)
    
    # Draw grid lines
    for i in range(BOARD_SIZE):
        start_x = MARGIN
        start_y = MARGIN + i * GRID_SIZE
        end_x = MARGIN + (BOARD_SIZE - 1) * GRID_SIZE
        end_y = MARGIN + i * GRID_SIZE
        pygame.draw.line(screen, COLOR_LINE, (start_x, start_y), (end_x, end_y), 2)
        
        start_x = MARGIN + i * GRID_SIZE
        start_y = MARGIN
        end_x = MARGIN + i * GRID_SIZE
        end_y = MARGIN + (BOARD_SIZE - 1) * GRID_SIZE
        pygame.draw.line(screen, COLOR_LINE, (start_x, start_y), (end_x, end_y), 2)

    # Draw star points
    star_points = [3, 9, 15]
    for x in star_points:
        for y in star_points:
            px = MARGIN + x * GRID_SIZE
            py = MARGIN + y * GRID_SIZE
            pygame.draw.circle(screen, COLOR_STAR, (px, py), 5)

    # Draw stones on the board
    for y in range(BOARD_SIZE):
        for x in range(BOARD_SIZE):
            stone = board[y][x]
            if stone != 0:
                px = MARGIN + x * GRID_SIZE
                py = MARGIN + y * GRID_SIZE
                radius = int(GRID_SIZE / 2 * 0.85)
                
                if stone == 1:  # Black stone
                    pygame.draw.circle(screen, COLOR_BLACK, (px, py), radius)
                elif stone == 2:  # White stone
                    pygame.draw.circle(screen, COLOR_WHITE, (px, py), radius)
                    pygame.draw.circle(screen, COLOR_LINE, (px, py), radius, 1)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("19x19 Gomoku vs AI")
    
    clock = pygame.time.Clock()
    
    # Board data (0: Empty, 1: Black(Human), 2: White(AI))
    board = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    
    # Turn management (1: Human turn, 2: AI turn)
    current_turn = 1
    game_over = False
    winner_text = ""
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            # Handle human click only if game is active and it's human's turn
            elif event.type == pygame.MOUSEBUTTONDOWN and current_turn == 1 and not game_over:
                if event.button == 1:
                    mouse_x, mouse_y = event.pos
                    grid_x = round((mouse_x - MARGIN) / GRID_SIZE)
                    grid_y = round((mouse_y - MARGIN) / GRID_SIZE)
                    
                    if 0 <= grid_x < BOARD_SIZE and 0 <= grid_y < BOARD_SIZE:
                        if board[grid_y][grid_x] == 0:
                            # Human places black stone
                            board[grid_y][grid_x] = 1
                            
                            # Check if human won
                            if check_win(board, 1):
                                game_over = True
                                winner_text = "Black (Human) Wins!"
                            else:
                                # Switch to AI turn
                                current_turn = 2

        # AI turn processing
        if current_turn == 2 and not game_over:
            ai_x, ai_y = ai_move(board)
            if ai_x is not None and ai_y is not None:
                # AI places white stone
                board[ai_y][ai_x] = 2
                
                # Check if AI won
                if check_win(board, 2):
                    game_over = True
                    winner_text = "White (AI) Wins!"
                else:
                    # Switch back to human turn
                    current_turn = 1

        # Draw board and stones
        draw_board(screen, board)
        
        # Draw game over message if applicable
        if game_over:
            font = pygame.font.SysFont(None, 48)
            text_surface = font.render(winner_text, True, (255, 0, 0))
            text_rect = text_surface.get_rect(center=(WINDOW_SIZE // 2, WINDOW_SIZE // 2))
            screen.blit(text_surface, text_rect)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()