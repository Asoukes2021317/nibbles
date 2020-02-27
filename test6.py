# This code is primarily based on my JS pacman game from highschool and https://python-forum.io/Thread-PyGame-Basic-Snake-game-using-OOP (mainly for implementation of snake/segment classes)

import time
import random
import pygame
pygame.init()


cellSize = 30
scoreHeight = 60
screenDim = [10, 10]
size = (screenDim[0]*cellSize, screenDim[1]*cellSize+scoreHeight)
screen = pygame.display.set_mode(size)
scoreText = ""

carryOn = True
direction = 3 # left
clock = pygame.time.Clock()
points = 0

class Square:
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
        x = int(screenDim[0]/2)
        y = int(screenDim[1]/2)
        for seg in range(length):
            self.segments.append(Square(x, y, colour))
            x += 1 # add segments to the right of "head"

    def isValid(self, theX, theY):
        if theX >= 0 and theX < screenDim[0] and theY >= 0 and theY < screenDim[1]:
            for seggy in range(1, len(self.segments), 1):
                if theX == self.segments[seggy].x and theY == self.segments[seggy].y:
                    return False
            return True
        else:
            return False

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
                moveFruit(self)

    def ateFruit(self):
        global points
        global scoreText
        lastSegment = len(self.segments)-1
        self.segments.append(Square(self.segments[lastSegment].x, self.segments[lastSegment].y, self.colour))
        points += 1
        scoreText = "Your Points: " + str(points)
        #print("Your points:", points)

#class Player:
player = Snake(4, (160, 0, 160))
apple = Square(1, 1, (0, 200, 0))

def moveFruit(self):
    pos = [apple.x, apple.y]
    done = False
    while not done:
        for segment in self.segments:
            while pos[0] == segment.x and pos[1] == segment.y:
                pos = [random.randint(0, screenDim[0]-1), random.randint(0, screenDim[1]-1)]
                hasRandomised = True
        if hasRandomised:
            hasRandomised = False # reset to go through all the segments again
        else:
            done = True

    self.ateFruit()
    apple.x = pos[0]
    apple.y = pos[1]

def now():
    millis = int(round(time.time() * 1000))
    return millis

def renderScreen():
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, apple.colour, (apple.x*cellSize, apple.y*cellSize+scoreHeight, cellSize, cellSize))
    for segment in player.segments:
        pygame.draw.rect(screen, (200, 0, 200), (segment.x*cellSize, segment.y*cellSize+scoreHeight, cellSize, cellSize))


    bestFont = pygame.font.SysFont('Comic Sans MS', 30)
    scoring = bestFont.render(scoreText, True, (255, 255, 255))
    screen.blit(scoring, (20, 0))

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

def mainLoop():
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

#def end():
#stuff...

# - - - - - | Actually Start The Game | - - - - - #
# - - - | Intro Set Go | - - - #
# welcome() allow user to choose screen size, greeting pic
# - - - | While Go | - - - #
# while going:
# readyUp() # get user to press enter when ready, maybe not need this fxn
mainLoop()
# end() ask to if want try again or not

pygame.quit()