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
    def __init__(self):
        return 0



# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((10, 10))
pygame.display.set_caption("Knight's Moves")

board1 = Board(8)
knight = Knight()
data = board1.get_data()
print(data)