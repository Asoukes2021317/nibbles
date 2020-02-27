# This code is primarily based on my JS pacman game from highschool and https://python-forum.io/Thread-PyGame-Basic-Snake-game-using-OOP (mainly for implementation of snake/segment classes)
import time
import random
#from tkinter import *
import tkinter as tk
import pygame
pygame.init()

options = []
bestFont = pygame.font.SysFont('Comic Sans MS', 30)
run = True
cellSize = 30
scoreHeight = 45
screenDim = [12, 10]
size = (screenDim[0]*cellSize, screenDim[1]*cellSize+scoreHeight)
#screen = pygame.display.set_mode(size)
#scoreText = ""

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
                self.ateFruit()

    def ateFruit(self):
        global points
        lastSegment = len(self.segments)-1
        self.segments.append(Square(self.segments[lastSegment].x, self.segments[lastSegment].y, self.colour))
        points += 1
        #print("Your points:", points)


def moveFruit(self):
    pos = [apple.x, apple.y]
    done = False
    while not done:
        for segment in self.segments:
            while (pos[0] == segment.x  and pos[1] == segment.y) or (pos[0] == -1  and pos[1] == -1):
                pos = [random.randint(0, screenDim[0]-1), random.randint(0, screenDim[1]-1)]
                hasRandomised = True
        if hasRandomised:
            hasRandomised = False # reset to go through all the segments again
        else:
            done = True

    apple.x = pos[0]
    apple.y = pos[1]

def now():
    millis = int(round(time.time() * 1000))
    return millis

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
    global run
    global player
    player = Snake(4, (160, 0, 160))
    global apple
    apple = Square(-1, -1, (0, 200, 0))
    moveFruit(player)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        checkKeys()
        player.movePlayer()
        renderScreen()
        clock.tick(60)

def renderScreen():
    global screen
    global bestFont
    global size
    size = (screenDim[0]*cellSize, screenDim[1]*cellSize+scoreHeight)
    screen = pygame.display.set_mode(size)
    #scoreText = ""
    screen.fill((0, 0, 0)) # base background colour of black

    pygame.draw.rect(screen, apple.colour, (apple.x*cellSize, apple.y*cellSize+scoreHeight, cellSize, cellSize)) # draw the "apple"

    for segment in player.segments: # draw each part of the snake
        pygame.draw.rect(screen, (200, 0, 200), (segment.x*cellSize, segment.y*cellSize+scoreHeight, cellSize, cellSize))

    pygame.draw.rect(screen, (40, 40, 40), (0, 0, screenDim[0]*cellSize, scoreHeight)) # Texts background colour
    scoreText = "Your Points: " + str(points) # Text itself
    scoring = bestFont.render(scoreText, True, (255, 255, 255)) # Visual transformation of text
    screen.blit(scoring, (10, 0)) # display the text

    pygame.display.update()

def colourOps(selected):
    global options
    global screen

    opNums = 4
    options = []

    for num in range(opNums):
        if num == selected:
            colour = (0, 255, 0)
        else:
            colour = (255, 0, 0)
        s = Square(num*35, 10, colour)
        options.append(pygame.draw.rect(screen, s.colour, (s.x, s.y, cellSize, cellSize)))
    pygame.display.update()

def customOptions(): # this is very much a WIP
    master = tk.Tk()
    tk.Label(master, text="First Name").grid(row=0)
    tk.Label(master, text="Last Name").grid(row=1)

    e1 = tk.Entry(master)
    e2 = tk.Entry(master)
    e1.insert(10, "Miller")
    e2.insert(10, "Jill")

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)

    tk.Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=tk.W, pady=4)
    # tk.Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=tk.W, pady=4)

    master.mainloop()

    tk.mainloop()

def welcome():
    global run
    global options
    global screen
    global screenDim

    go = True
    size = (500, 500)
    screen = pygame.display.set_mode(size)
    screen.fill((255, 255, 0))
    colourOps(0)

    while go:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                clicked = -1
                for i, op in enumerate(options):
                    if op.collidepoint(pos):
                        clicked = i
                if clicked == 0:
                    print("#load preset 1")
                    colourOps(0)
                    screenDim = [12, 10]
                if clicked == 1:
                    print("#load preset 2")
                    colourOps(1)
                    screenDim = [26, 18]
                if clicked == 2:
                    print("#load preset 3")
                    colourOps(2)
                    screenDim = [38, 28]
                if clicked == 3:
                    print("#load custom dialog")
                    colourOps(3)
                    #customOptions()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    go = False
                elif event.key == pygame.K_KP_ENTER:
                    go = False

            if event.type == pygame.QUIT:
                run = False
                go = False


#def end():
#stuff...

# - - - - - | Actually Start The Game | - - - - - #

welcome()

mainLoop()

# end() ask to if want try again or not

pygame.quit()