import pygame

pygame.init()

display_width = 600
display_height = 800

gameDisplay = pygame.display.set_mode((600,800))
pygame.display.set_caption('Asteroid Run')

clock = pygame.time.Clock()

finished = False
shipImg = pygame.image.load("spaceship.png")
bgImg = pygame.image.load("background.png")

def drawShip(x, y):
    gameDisplay.blit(shipImg, (x - 0.5*shipImg.get_width(),y - 0.5*shipImg.get_height()))

def drawBackground():
    gameDisplay.blit(bgImg, (0, 0))
    
x = display_width * 0.5
y = display_height * 0.8

while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

        drawBackground()
        drawShip(x, y)

        pygame.display.update()
        clock.tick(60)

pygame.quit()
