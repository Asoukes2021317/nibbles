import pygame
pygame.init()
winWidth = 500
winHeight = 500
win = pygame.display.set_mode((winWidth, winHeight))

pygame.display.set_caption("Test 3")

x = 50
y = 50
width = 40
height = 60
velocity = 10

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if x-velocity >= 0:
            x -= velocity
    if keys[pygame.K_RIGHT]:
        if x+velocity <= winWidth-width:
            x += velocity
    if keys[pygame.K_UP]:
        if y-velocity >= 0:
            y -= velocity
    if keys[pygame.K_DOWN]:
        if y+velocity <= winHeight-height:
            y += velocity
    
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (200, 0, 200), (x, y, width, height))
    pygame.display.update()



pygame.quit()