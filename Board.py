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


class Moves:
    def __init__(self):
        return 0



board1 = Board(8)
data = board1.get_data()
print(data)