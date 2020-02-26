import time
import pygame
pygame.init()

cellSize = 30

screenDim = [15, 15]
size = (screenDim[0]*cellSize, screenDim[1]*cellSize)
screen = pygame.display.set_mode(size)

carryOn = True
direction = 0 # up
clock = pygame.time.Clock()

# player vars
# playerPause = 500
# x = 0
# y = 14
# timeForPlayerTurn = 0
# colour = (160, 0, 160)

class Segment:
    def __init__(self, x, y, colour, pause, turn):
        self.pause = pause
        self.x = x
        self.y = y
        self.turn = turn
        self.colour = colour

    def isValid(self, theX, theY):
        return bool(theX >= 0 and theX < screenDim[0] and theY >= 0 and theY < screenDim[1])

    def movePlayer(self):
        # global timeForPlayerTurn
        # global y
        # global x
        if self.turn < now():
            self.turn = now()+self.pause
            if direction == 0 and self.isValid(self.x, self.y-1):
                self.y -= 1
            elif direction == 2 and self.isValid(self.x, self.y+1):
                self.y += 1
            elif direction == 1 and self.isValid(self.x+1, self.y):
                self.x += 1
            elif direction == 3 and self.isValid(self.x-1, self.y):
                self.x -= 1

        
#class Player:
player = Segment(7, 7, (160, 0, 160), 500, 0)

def now():
    millis = int(round(time.time() * 1000))
    return millis

def renderScreen():
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (200, 0, 200), (player.x*cellSize, player.y*cellSize, cellSize, cellSize))
    pygame.display.update()




run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        direction = 0
    if keys[pygame.K_RIGHT]:
        direction = 1
    if keys[pygame.K_DOWN]:
        direction = 2
    if keys[pygame.K_LEFT]:
        direction = 3
    
    player.movePlayer()
    renderScreen()

    clock.tick(60)