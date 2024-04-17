import pygame
import sys
import time

# Constants
WIDTH, HEIGHT = 500, 500
ROWS, COLS = 6, 6
SQ_SIZE = WIDTH // COLS

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Knight's Moves Animation")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 205, 100)

# Chessboard representation
chessboard = [[0, 15, 6, 25, 10, 13], [33, 24, 11, 14, 5, 26], [16, 1, 32, 7, 12, 9], [31, 34, 23, 20, 27, 4], [22, 17, 2, 29, 8, 19], [35, 30, 21, 18, 3, 28]]


def index_2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return (i, x.index(v))

def create_positions(board):
    moves = []
    for i in range(0,36):
        index = index_2d(board, i)
        moves.append(index)
    return moves

def create_moves(board):
    positions = create_positions(board)
    moves = [(0, 0)]
    for i, p in enumerate(positions):
        if i > 0:

            pre_x = positions[i-1][0]
            pre_y = positions[i-1][1]

            new_move = (p[0]-pre_x, p[1]-pre_y)

            moves.append(new_move)
    return moves

# Knight's possible moves (relative positions)
knight_moves = create_moves(chessboard)
def draw_chessboard():
    for row in range(ROWS):
        for col in range(COLS):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))

def draw_knight(x, y):
    pygame.draw.circle(screen, GREEN, (x * SQ_SIZE + SQ_SIZE // 2, y * SQ_SIZE + SQ_SIZE // 2), SQ_SIZE // 3)

def main():
    running = True
    knight_x, knight_y = 0, 0  # Initial position of the knight

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)
        draw_chessboard()

        # Animate knight's moves
        for dx, dy in knight_moves:
            new_x, new_y = knight_x + dx, knight_y + dy
            if 0 <= new_x < COLS and 0 <= new_y < ROWS:
                draw_knight(new_x, new_y)
                pygame.display.flip()
                time.sleep(0.5)  # Pause for animation effect
                knight_x, knight_y = new_x, new_y

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
