# This code is primarily based on my JS pacman game from highschool and https://python-forum.io/Thread-PyGame-Basic-Snake-game-using-OOP (mainly for implementation of snake/segment classes)
import time
import random
import csv

import tkinter as tk
from tkinter import *
import pygame
pygame.init()

pygame.display.set_caption('Python Nibbles')

options = []
run = True
cellSize = 24
bestFont = pygame.font.SysFont('Comic Sans MS', cellSize)
bestFont2 = pygame.font.SysFont('Comic Sans MS', int(cellSize*0.9))
bestFont3 = pygame.font.SysFont('Comic Sans MS', int(cellSize*0.7))
scoreHeight = int(cellSize*1.5)
screenDim = [0, 0]
size = (screenDim[0]*cellSize, screenDim[1]*cellSize+scoreHeight)
carryOn = True
direction = 3 # left
clock = pygame.time.Clock()
points = 0
theBoard = []

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
        self.pause = 250
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
        global run

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
                run = False

            if self.segments[0].x == apple.x and self.segments[0].y == apple.y:
                moveFruit(self)
                self.ateFruit()

    def ateFruit(self):
        global points
        lastSegment = len(self.segments)-1
        self.segments.append(Square(self.segments[lastSegment].x, self.segments[lastSegment].y, self.colour))
        points += 1

        # inc speed slightly
        if points <= 8:
            self.pause -= 5
        elif points <= 16:
            self.pause -= 4
        elif points <= 24:
            self.pause -= 3
        elif points <= 48:
            self.pause -= 2
        elif points <= 72:
            self.pause -= 1
        elif points%2 == 0:
            self.pause -= 1

class getHighscore():
    def __init__(self):
        self.tkWin = Tk()
        self.tkWin.geometry('250x60')
        self.tkWin.title('Highscore!')
        self.nameLabel = Label(self.tkWin, text="Your Name").grid(row=0, column=0)
        self.name = StringVar()
        self.nameEntry = Entry(self.tkWin, textvariable=self.name).grid(row=0, column=1)
        self.sendButton = Button(self.tkWin, text="Done", command=self.doThing).grid(row=2, column=0)
        self.warning = StringVar()
        #self.warning.set("")
        self.warningLabel = Label(self.tkWin, textvariable=self.warning).grid(row=2, column=1)
        self.tkWin.lift()
        self.tkWin.bind('<Return>', self.doThing)
        self.tkWin.mainloop()

    def doThing(self, event=None):
        global theName
        thisName = self.name.get().lower()
        length = len(thisName)
        if 2 <= length <= 9:
            theName = thisName
            self.tkWin.destroy()
        else:
            self.warning.set("Name must be 2-10 chars")
        return


def moveFruit(self):
    pos = [apple.x, apple.y]
    done = False
    hasRandomised = False

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
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and direction != 2:
        direction = 0
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and direction != 3:
        direction = 1
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and direction != 0:
        direction = 2
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and direction != 1:
        direction = 3

def mainLoop():
    global run
    global outer
    global inner
    global direction
    global points
    global player
    player = Snake(4, (90, 0, 90))
    global apple
    apple = Square(-1, -1, (0, 150, 0))
    moveFruit(player)
    direction = 3
    run = True
    points = 0
    while run:
        checkKeys()
        player.movePlayer()
        renderScreen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                outer = False
                inner = False
                pygame.quit()
        clock.tick(60)

def renderScreen():
    global screen
    global bestFont
    global size
    size = (screenDim[0]*cellSize, screenDim[1]*cellSize+scoreHeight)
    screen = pygame.display.set_mode(size)
    #scoreText = ""
    screen.fill((0, 0, 0)) # base background colour of black

    # pygame.draw.circle(screen, apple.colour, (apple.x*cellSize+int(cellSize/2), apple.y*cellSize+scoreHeight+int(cellSize/2)), int(cellSize/2)) # draw the "apple"
    pygame.draw.ellipse(screen, apple.colour, (apple.x*cellSize, apple.y*cellSize+scoreHeight, cellSize, cellSize)) # draw the "apple"
    # pygame.draw.rect(screen, apple.colour, (apple.x*cellSize, apple.y*cellSize+scoreHeight, cellSize, cellSize)) # draw the "apple"

    for i, segment in enumerate(player.segments): # draw each part of the snake
        if i == 0:
            pygame.draw.rect(screen, (110, 0, 110), (segment.x*cellSize, segment.y*cellSize+scoreHeight, cellSize, cellSize))
        else:
            pygame.draw.rect(screen, segment.colour, (segment.x*cellSize, segment.y*cellSize+scoreHeight, cellSize, cellSize))

    pygame.draw.rect(screen, (40, 40, 40), (0, 0, screenDim[0]*cellSize, scoreHeight)) # Texts background colour
    scoreText = "Your Points: " + str(points) # Text itself
    scoring = bestFont.render(scoreText, True, (255, 255, 255)) # Visual transformation of text
    screen.blit(scoring, (10, 0)) # display the text

    pygame.display.update()

def colourOps(selected):
    global options
    global screen

    opNums = 3 # was 4 to include Custom
    options = []

    for num in range(opNums):
        if num == selected:
            colour = (0, 255, 0)
        else:
            colour = (255, 0, 0)
        s = Square(num*(4*cellSize)+int(cellSize*2.5), size2[1]-int(cellSize*1.5), colour)
        options.append(pygame.draw.rect(screen, s.colour, (s.x, s.y, cellSize, cellSize)))
    pygame.display.update()

def customOptions(): # this is very much a WIP
    print("Custom Option Activated")
    #Ask user for width and height in pixels or cells
    #if in pixels, translate to nearest cells rounded down, and let user know
    #return [width, height]#in terms of cells

def welcome():
    global run
    global options
    global screen
    global screenDim
    global outer
    global inner
    global size2
    global theBoard

    small = [16, 12]
    medium = [24, 18]
    large = [32, 24]

    go = True
    size2 = (28*cellSize, 16*cellSize)
    screen = pygame.display.set_mode(size2)
    screen.fill((0, 0, 0))

    # The "logo" of the program
    pygame.draw.rect(screen, (90, 0, 90), (cellSize*2, int(cellSize*4.5), cellSize*10, cellSize*4))
    pygame.draw.rect(screen, (0, 180, 0), (cellSize*3, int(cellSize*5.5), cellSize*2, cellSize*2))
    pygame.draw.rect(screen, (0, 180, 0), (cellSize*9, int(cellSize*5.5), cellSize*2, cellSize*2))

    introText = ["Nibble reboot!!", "Made in Python", "", "", "", "", 'Press "Enter" to begin...', "", "Choose Game Size:"]
    for i, t in enumerate(introText):
        intro = bestFont.render(t, True, (255, 255, 255)) # Visual transformation of text
        screen.blit(intro, (cellSize*2, cellSize+int(i*cellSize*1.3))) # display the text?

    for i in range(3): # was range 4 to include Custom
        if i == 0:
            sizeText = "Small"
        elif i == 1:
            sizeText = "Med."
        elif i == 2:
            sizeText = "Large"
        elif i == 3:
            sizeText = "Cust."
        sizes = bestFont.render(sizeText, True, (255, 255, 255)) # Visual transformation of text
        screen.blit(sizes, (i*(4*cellSize)+cellSize*2, cellSize*13)) # display the text

    #get leaderboard using: https://stackoverflow.com/a/11350095 and https://stackoverflow.com/a/24662707
    fname = "leaderboard.csv"
    theBoard = []
    try:
        with open(fname, newline='') as f:
            next(f)
            reader = csv.reader(f)
            theBoard = list(reader)
        f.close()
        # print(theBoard)
    except:
        print("no leaderboard")

    #actually display leaderboard
    if theBoard != []:
        lead = bestFont.render("Leaderboard:", True, (255, 255, 255))
        screen.blit(lead, (cellSize*15, int(cellSize*0.5)))
        for i, score in enumerate(theBoard):
            theScoreText = "%d | %s | %s pts" %(i+1, score[1], score[0])
            theScore = bestFont.render(theScoreText, True, (255, 255, 255))
            screen.blit(theScore, (cellSize*15, cellSize+int((i+1)*cellSize*1.3)))
    else:
        lead = bestFont.render("No Leaderboard Data", True, (255, 255, 255))
        screen.blit(lead, (cellSize*15, cellSize*4))

    colourOps(0)
    screenDim = small

    while go:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                clicked = -1
                for i, op in enumerate(options):
                    if op.collidepoint(pos):
                        clicked = i
                if clicked == 0:
                    colourOps(0)
                    screenDim = small
                if clicked == 1:
                    colourOps(1)
                    screenDim = medium
                if clicked == 2:
                    colourOps(2)
                    screenDim = large
                if clicked == 3: # custom dialog
                    colourOps(3)
                    #screenDim = customOptions()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    go = False
                    inner = True

            if event.type == pygame.QUIT:
                run = False
                go = False
                outer = False
                inner = False

def gameOver():
    global size
    global run
    global outer
    global inner
    global theBoard
    global theName
    added = False

    for i, scorer in enumerate(theBoard):
        if points > int(scorer[0]):
            getHighscore()
            playerName = theName
            theBoard.insert(i, [str(points), playerName])
            if len(theBoard) > 10:
                theBoard.pop()
            added = True
            break
    if not added and len(theBoard) < 10:
        getHighscore()
        playerName = theName
        theBoard.insert(len(theBoard), [str(points), playerName])
    if len(theBoard) == 0:
        getHighscore()
        playerName = theName
        theBoard.insert(0, [str(points), playerName])
    print(theBoard)

    # CSV Stuffs
    header = ["Score", "Name"]
    fname = "leaderboard.csv"
    #location = pathlib.Path(__file__).parent / fname
    with open(fname, 'wt', newline='\n') as f:#used to be location
        csv_writer = csv.writer(f)
        csv_writer.writerow(header)
        for score in theBoard:
            csv_writer.writerow(score)

    # lead = bestFont.render("Leaderboard:", True, (255, 255, 255))
    # screen.blit(lead, (cellSize*15, int(cellSize*0.5)))
    for i, score in enumerate(theBoard):
        theScoreText = "%d | %s | %s pts" %(i+1, score[1], score[0])
        if i % 2 == 0:
            theScore = bestFont3.render(theScoreText, True, (255, 255, 255))
            screen.blit(theScore, (int((size[0]-cellSize*15.5)/2), cellSize*7+int((i+1)*cellSize*0.5)))
        else:
            theScore = bestFont3.render(theScoreText, True, (255, 255, 255))
            screen.blit(theScore, (int((size[0])/2), cellSize*7+int((i)*cellSize*0.5)))

    exitText = ["Game Over, you got %d points!" %(points), '"X" to exit', '"Enter" to try again', '"R" to go to start']
    for i, t in enumerate(exitText):
        text = bestFont2.render(t, True, (255, 255, 255)) # Visual transformation of text
        screen.blit(text, (int((size[0]-cellSize*12)/2), int(cellSize*(2.5+i)))) # display the text?

    pygame.display.update()

    over = False
    while not over:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    over = True
                elif event.key == pygame.K_x:
                    over = True
                    inner = False
                    outer = False
                elif event.key == pygame.K_r:
                    over = True
                    inner = False
            if event.type == pygame.QUIT:
                over = True
                inner = False
                outer = False


# - - - - - | Actually Start The Game | - - - - - #

outer = True
inner = True
while outer:
    welcome()
    while inner:
        mainLoop()
        if inner:
            gameOver()

pygame.quit()