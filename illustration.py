from Board import *
import pygame
import sys
import time

class Illustrator:
    def __init__(self, chessboard):
        self.n = len(chessboard[0])
        self.board1 = Board(self.n)
        self.knight = Knight()
        self.moves = Moves(chessboard)

        self.data = self.board1.get_data()
        self.knight_image = self.knight.get_knight()
        self.chessboard_matrix = self.moves.get_chessboard_matrix()

        # Initialize Pygame
        pygame.init()
        self.screen = pygame.display.set_mode((self.data['width'], self.data['height']))
        pygame.display.set_caption("Knight's Moves")


    def draw_chessboard(self):
        for row in range(self.data['row']):
            for col in range(self.data['col']):
                color = self.data['white'] if (row + col) % 2 == 0 else self.data['black']
                pygame.draw.rect(self.screen, color, (col * self.data['sq_size'], row * self.data['sq_size'], self.data['sq_size'], self.data['sq_size']))

    def draw_knight(self, x, y):
        # Calculate the position where the image will be placed
        image_x = x * self.data['sq_size']
        image_y = y * self.data['sq_size']

        # Blit the image onto the screen at the calculated position
        self.screen.blit(self.knight_image, (image_x, image_y))


    def print_chess_board(self):
        for r in self.chessboard_matrix:
            for c in r:
                print("| {} |".format(c), end=" ")
            print("")
            print("-----------------------------------------------------")

    def illustrate(self):
        running = True
        knight_x, knight_y = 0, 0  # Initial position of the knight

        move_counter = 0

        while running and move_counter < self.n * self.n:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill(self.data['black'])
            self.draw_chessboard()

            # Animate knight's moves
            for dx, dy in self.moves.get_moves():
                move_counter = move_counter + 1
                new_x, new_y = knight_x + dx, knight_y + dy
                if 0 <= new_x < self.data['col'] and 0 <= new_y < self.data['row']:
                    self.draw_knight(new_x, new_y)
                    pygame.display.flip()
                    time.sleep(0.3)  # Pause for animation effect
                    knight_x, knight_y = new_x, new_y

            pygame.display.flip()
            self.print_chess_board()

        pygame.quit()
        sys.exit()
