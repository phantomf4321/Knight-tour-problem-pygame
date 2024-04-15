import pygame

class Board:
    def __init__(self,n,block_size):
        self.n = n
        self.block_size = block_size

        self.surface = pygame.Surface((block_size*n,block_size*n))
        self.board_rect = [[0 for _ in range(n)] for _ in range(n)]
        self.init_board()

        self.knight = Knight(block_size)
    
    def init_board(self):
        for i in range(self.n):
            for j in range(self.n):
                x = i * self.block_size
                y = j * self.block_size
                self.board_rect[i][j] = pygame.Rect(x,y,self.block_size,self.block_size)
                if (i + j) % 2 == 0:
                    pygame.draw.rect(self.surface,(255,255,255),self.board_rect[i][j],0)
                else:
                    pygame.draw.rect(self.surface,(125,125,125),self.board_rect[i][j],0)

    def place_knight(self,prev,cur):
        self.knight.place(self.board_rect[cur[1]][cur[0]].center)
        self.knight.draw(self.surface)
        if prev != None:
            if (prev[0]+prev[1])%2 == 0:
                pygame.draw.rect(self.surface,(255,255,255),self.board_rect[prev[1]][prev[0]],0)
            else:
                pygame.draw.rect(self.surface,(125,125,125),self.board_rect[prev[1]][prev[0]],0)

            pygame.draw.circle(self.surface,(125,0,0),self.board_rect[prev[1]][prev[0]].center,20,width=3)
            

        

class Knight:
    def __init__(self,size):
        self.image = pygame.image.load("knight.png")
        self.image = pygame.transform.smoothscale(self.image,(size,size))
        self.rect = self.image.get_rect()

    def place(self,position):
        self.rect.center = position

    def draw(self,surface):
        surface.blit(self.image,self.rect)