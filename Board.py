class Board:
    def __init__(self, n):
        self.n = n # create n*n board

        # Constants
        self.WIDTH, self.HEIGHT = 500, 500
        self.ROWS, self.COLS = n, n
        self.SQ_SIZE = self.WIDTH // self.COLS

        # Colors
        self.WHITE = (200, 200, 200)
        self.BLACK = (50, 50, 50)

