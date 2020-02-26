import pygame
pygame.init()

cellSize = 30
winWidthCells = 15
winHeightCells = 15
win = pygame.display.set_mode((winWidthCells*cellSize, winHeightCells*cellSize))

pygame.display.set_caption("Test 3")

x = 0
y = 0
# width = 40
# height = 60
# velocity = 10

run = True
while run:
    pygame.time.delay(500)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if x-cellSize >= 0:
            x -= cellSize
    if keys[pygame.K_RIGHT]:
        if x+cellSize <= (winWidthCells-1)*cellSize:
            x += cellSize
    if keys[pygame.K_UP]:
        if y-cellSize >= 0:
            y -= cellSize
    if keys[pygame.K_DOWN]:
        if y+cellSize <= (winHeightCells-1)*cellSize:
            y += cellSize
    
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (200, 0, 200), (x, y, cellSize, cellSize))
    pygame.display.update()



pygame.quit()