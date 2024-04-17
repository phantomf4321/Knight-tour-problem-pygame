import pygame
import sys
import time

# Constants
WIDTH, HEIGHT = 500, 500
ROWS, COLS = 8, 8
SQ_SIZE = WIDTH // COLS

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Knight's Moves")

# Colors
WHITE = (200, 200, 200)
BLACK = (50, 50, 50)

# Chessboard representation
chessboard = [[0, 59, 38, 33, 30, 17, 8, 63], [37, 34, 31, 60, 9, 62, 29, 16], [58, 1, 36, 39, 32, 27, 18, 7], [35, 48, 41, 26, 61, 10, 15, 28], [42, 57, 2, 49, 40, 23, 6, 19], [47, 50, 45, 54, 25, 20, 11, 14], [56, 43, 52, 3, 22, 13, 24, 5], [51, 46, 55, 44, 53, 4, 21, 12]]


def index_2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return (i, x.index(v))

def create_positions(board):
    moves = []
    for i in range(0, 64):
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

def print_chess_board():
    for r in chessboard:
        for c in r:
            print("| {} |".format(c), end=" ")
        print("")
        print("-----------------------------------------------------")

# Knight's possible moves (relative positions)
knight_moves = create_moves(chessboard)
def draw_chessboard():
    for row in range(ROWS):
        for col in range(COLS):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))


# Load the image (do this outside the draw_knight function)
knight_image = pygame.image.load('knight.png').convert()
knight_image = pygame.transform.smoothscale(knight_image,(62,62))


def draw_knight(x, y):
    # Calculate the position where the image will be placed
    image_x = x * SQ_SIZE
    image_y = y * SQ_SIZE

    # Blit the image onto the screen at the calculated position
    screen.blit(knight_image, (image_x, image_y))
def main():
    running = True
    knight_x, knight_y = 0, 0  # Initial position of the knight

    move_counter = 0

    while running and move_counter<64:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)
        draw_chessboard()

        # Animate knight's moves
        for dx, dy in knight_moves:
            move_counter = move_counter+1
            new_x, new_y = knight_x + dx, knight_y + dy
            if 0 <= new_x < COLS and 0 <= new_y < ROWS:
                draw_knight(new_x, new_y)
                pygame.display.flip()
                time.sleep(0.1)  # Pause for animation effect
                knight_x, knight_y = new_x, new_y

        pygame.display.flip()
        print_chess_board()

    pygame.quit()
    sys.exit()




if __name__ == "__main__":
    main()
