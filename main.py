import pygame
import Board
import Solution
import sys

# initialize
pygame.init()
block_size = 40

n = 5

#size of blocks...
screen_width = block_size * n + 20
screen_height = block_size * n + 20
screen = pygame.display.set_mode((screen_width,screen_height))

s = Solution.Solution()
b = Board.Board(n,block_size)

# calculate move
result = s.knightTour(n)

print(result)

# find next move
def find(move):
    for i in range(n):
        for j in range(n):
            if move == result[i][j]:
                return (i,j)

def move_generator(n):
    index = 0
    while index < n*n:
        yield find(index)
        index += 1


# game loop
#running = True
#clock = pygame.time.Clock()

prev = None
solving = False
gen = move_generator(n)

"""while running:
    clock.tick(2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Start")
                solving = True

    if solving:
        try:
            move = next(gen)
            if move == False:
                move_generator.close()
            b.place_knight(prev,move)
            prev = move

        except:
            print("End")
            print(result)
            solving = False

    #screen.fill((0,0,0))
    #screen.blit(b.surface,(10,10))
    #pygame.display.update()
"""
