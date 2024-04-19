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

    def get_knight(self):
        return self.knight_image



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

    def get_chessboard_matrix(self):
        return self.chessboard_matrix

    def get_positions(self):
        data = self.create_positions()
        return data

    def get_moves(self):
        data = self.create_moves()
        return data
