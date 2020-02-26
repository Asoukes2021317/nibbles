import time
import random
import pygame
pygame.init()

cellSize = 30

screenDim = [20, 15]
size = (screenDim[0]*cellSize, screenDim[1]*cellSize)
screen = pygame.display.set_mode(size)

carryOn = True
direction = 0 # up
clock = pygame.time.Clock()
points = 0

class Segment:
    def __init__(self, x, y, colour):
        self.x = x
        self.y = y
        self.colour = colour


class Snake:
    def __init__(self, length, colour):
        self.segments = []
        self.length = length
        self.colour = colour
        self.pause = 300
        self.turn = 0
        x = 7
        y = 7
        for seg in range(length):
            self.segments.append(Segment(x, y, colour))
            x += 1

    def isValid(self, theX, theY):
        return bool(theX >= 0 and theX < screenDim[0] and theY >= 0 and theY < screenDim[1])

    def movePlayer(self):
        if self.turn < now():
            # checkKeys()
            self.turn = now()+self.pause
            for segment in range(len(self.segments)-1, 0, -1): # look at the segments in reverse order
                self.segments[segment].x = self.segments[segment-1].x
                self.segments[segment].y = self.segments[segment-1].y

            if direction == 0 and self.isValid(self.segments[0].x, self.segments[0].y-1):
                self.segments[0].y -= 1
            elif direction == 2 and self.isValid(self.segments[0].x, self.segments[0].y+1):
                self.segments[0].y += 1
            elif direction == 1 and self.isValid(self.segments[0].x+1, self.segments[0].y):
                self.segments[0].x += 1
            elif direction == 3 and self.isValid(self.segments[0].x-1, self.segments[0].y):
                self.segments[0].x -= 1
            else:
                print("Game OVER!!!")

            if self.segments[0].x == apple.x and self.segments[0].y == apple.y:
                moveFruit()

    def ateFruit(self):
        global points
        lastSegment = len(self.segments)-1
        self.segments.append(Segment(self.segments[lastSegment].x, self.segments[lastSegment].y, self.colour))
        points += 1
        print("Your points:", points)

#class Player:
player = Snake(4, (160, 0, 160))
apple = Segment(1, 1, (0, 200, 0))

def moveFruit():
    pos = [apple.x, apple.y]
    for segment in player.segments:
        while pos[0] == segment.x and pos[1] == segment.y:
            pos = [random.randint(0, screenDim[0]-1), random.randint(0, screenDim[1]-1)]
    player.ateFruit()
    apple.x = pos[0]
    apple.y = pos[1]

def now():
    millis = int(round(time.time() * 1000))
    return millis

def renderScreen():
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, apple.colour, (apple.x*cellSize, apple.y*cellSize, cellSize, cellSize))
    for segment in player.segments:
        pygame.draw.rect(screen, (200, 0, 200), (segment.x*cellSize, segment.y*cellSize, cellSize, cellSize))
    pygame.display.update()

def checkKeys():
    global direction
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        direction = 0
    if keys[pygame.K_RIGHT]:
        direction = 1
    if keys[pygame.K_DOWN]:
        direction = 2
    if keys[pygame.K_LEFT]:
        direction = 3


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    checkKeys()
    #moveFruit()
    player.movePlayer()
    renderScreen()

    clock.tick(60)

pygame.quit()