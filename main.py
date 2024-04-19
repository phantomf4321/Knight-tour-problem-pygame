import Solution
from illustration import *



n = 8
s = Solution.Solution()
# calculate move
chessboard = s.knightTour(n)

# illustration
ill = Illustrator(chessboard)
ill.illustrate()

