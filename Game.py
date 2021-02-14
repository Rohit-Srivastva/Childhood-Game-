import pygame

class Boxesgame():
    def __init__(self):
        pass
        
        width,height = 400,500

        self.screen = pygame.display.set_mode((width,height))

        #initilize pygame ckock

        self.clock = pygame.time.Clock()

        self.horizontalBoard = [[False for x in range(6)] for y in range(7)]
        self.verticalBoard = [[False for x in range(7)] for y in range(6)]
        self.initGraphics()


    
    def initGraphics(self):
        self.verticalNormalLine = pygame.image.load("normalline.png")
        self.horizontalNormalLine = pygame.transform.rotate(pygame.image.load("normalline.png"), -90)

        self.verticalBar = pygame.image.load("bar_done.png")
        self.horizontalBar = pygame.transform.rotate(pygame.image.load("bar_done.png"),-90)

        self.verticalHoverLine = pygame.image.load("hoverline.png")
        self.horizontalHoverLine = pygame.transform.rotate(pygame.image.load("hoverline.png"),-90)

    
    def drawBoard(self):
        self.horizontalBoard[5][3]=True

        for x in range(6):
            for y in range(7):
                if not self.horizontalBoard[y][x]:
                    self.screen.blit(self.horizontalNormalLine, [(x)*64+5,(y)*64])
                else:
                    self.screen.blit(self.horizontalBar, [(x)*64+5,(y)*64])

        for x in range(7):
            for y in range(6):
                if not self.verticalBoard[y][x]:
                    self.screen.blit(self.verticalNormalLine, [(x)*64,(y)*64+5])
                else:
                    self.screen.blit(self.verticalBar, [(x)*64,(y)*64+5])
                    
    
    def update(self):
        self.clock.tick(60)
        self.drawBoard()

        
        self.screen.fill  #to clear screen

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                exit()
        
        pygame.display.flip()   #to update the screen


bg = Boxesgame()
while 1:
    bg.update()

