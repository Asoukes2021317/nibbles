# Import the pygame library and initialise the game engine
import pygame
pygame.init()

# Define some colors
# Base
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 180, 0)
GREY = (160, 160, 160)

# Open a new window
size = (700, 500)
screen = pygame.display.set_mode(size)

# The loop will carry on until the user exit the game (e.g. clicks the close button).
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while carryOn:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            carryOn = False # Flag that we are done so we exit this loop

    # --- Game logic should go here

    # --- Drawing code should go here
    # First, clear the screen to white.
    #screen.fill(WHITE)
    #The you can draw different shapes and lines or add text to your background stage.
    pygame.draw.rect(screen, GREEN, [0, 0, 700, 500], 0)
    pygame.draw.rect(screen, WHITE, [140, 0, 420, 500], 0)
    for i in range(4):
        num = (104*(i+1))+40
        pygame.draw.rect(screen, GREY, [num, 0, 100, 500], 0)
    pygame.draw.rect(screen, BLACK, [0, 0, 700, 500], 5)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

#Once we have exited the main program loop we can stop the game engine:
pygame.quit()