from illustration import *
import Solution



# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((10, 10))
pygame.display.set_caption("Knight's Moves")

# Initialize structures and functions
n = 8
s = Solution.Solution()
board1 = Board(n)
knight = Knight()

# calculate move
chessboard = s.knightTour(n)

# illustration
ill = Illustrator(chessboard)
ill.illustrate()

