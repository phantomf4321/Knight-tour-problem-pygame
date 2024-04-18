import pygame
class Board:
    def __init__(self, n):
        print("{}*{} board is created!".format(n, n))
        self.n = n # create n*n board

        # Constants
        self.WIDTH, self.HEIGHT = 500, 500
        self.ROWS, self.COLS = n, n
        self.SQ_SIZE = self.WIDTH // self.COLS

        # Colors
        self.WHITE = (200, 200, 200)
        self.BLACK = (50, 50, 50)

    def get_data(self):
        data = {
            "size": self.n,
            "width": self.WIDTH,
            "height": self.HEIGHT,
            "row": self.ROWS,
            "col": self.COLS,
            "sq_size": self.SQ_SIZE,
            "black": self.BLACK,
            "white": self.WHITE
        }

        return data

class Knight:
    def __init__(self):
        # Load the image (do this outside the draw_knight function)
        self.knight_image = pygame.image.load('knight.png').convert()
        self.knight_image = pygame.transform.smoothscale(self.knight_image, (62, 62))

        print("Knight constructore is called!")



class Moves:
    def __init__(self, chessboard_matrix):
        print("Moves are ready to strat operations on {}".format(chessboard_matrix))
        self.chessboard_matrix = chessboard_matrix

    def index_2d(self, v):
        for i, x in enumerate(self.chessboard_matrix):
            if v in x:
                return (i, x.index(v))

    def create_positions(self):
        moves = []
        for i in range(0, 64):
            index = self.index_2d(i)
            moves.append(index)
        return moves

    def create_moves(self):
        positions = self.create_positions()
        moves = [(0, 0)]
        for i, p in enumerate(positions):
            if i > 0:
                pre_x = positions[i - 1][0]
                pre_y = positions[i - 1][1]

                new_move = (p[0] - pre_x, p[1] - pre_y)

                moves.append(new_move)
        return moves

    def get_positions(self):
        data = self.create_positions()
        return data

    def get_moves(self):
        data = self.create_moves()
        return data




# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((10, 10))
pygame.display.set_caption("Knight's Moves")

board1 = Board(8)
knight = Knight()
data = board1.get_data()
print(data)

chessboard = [[0, 59, 38, 33, 30, 17, 8, 63], [37, 34, 31, 60, 9, 62, 29, 16], [58, 1, 36, 39, 32, 27, 18, 7], [35, 48, 41, 26, 61, 10, 15, 28], [42, 57, 2, 49, 40, 23, 6, 19], [47, 50, 45, 54, 25, 20, 11, 14], [56, 43, 52, 3, 22, 13, 24, 5], [51, 46, 55, 44, 53, 4, 21, 12]]
moves = Moves(chessboard)
print(moves.get_positions())
print(moves.get_moves())
