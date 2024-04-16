import pygame
import sys
import time

# Constants
WIDTH, HEIGHT = 400, 400
ROWS, COLS = 5, 5
SQ_SIZE = WIDTH // COLS

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Knight's Moves Animation")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Chessboard representation
chessboard = [[0, 5, 14, 9, 20],
              [13, 8, 19, 4, 15],
              [18, 1, 6, 21, 10],
              [7, 12, 23, 16, 3],
              [24, 17, 2, 11, 22]]

# Knight's possible moves (relative positions)
knight_moves = [(2, 1), (1, 2), (-1, 2), (-2, 1),
                (-2, -1), (-1, -2), (1, -2), (2, -1)]

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