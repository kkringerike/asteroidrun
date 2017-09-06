import pygame
import time

pygame.init()

display_width = 600
display_height = 800

# Farger
black = (0, 0, 0)
white = (255,255,255)
red = (255, 0, 0)

gameDisplay = pygame.display.set_mode((600,800))
pygame.display.set_caption('Asteroid Run')

clock = pygame.time.Clock()

shipImg = pygame.image.load("spaceship.png")
bgImg = pygame.image.load("background.png")

ship_width = shipImg.get_width()
ship_height = shipImg.get_height()

def drawShip(x, y):
    gameDisplay.blit(shipImg, (x - 0.5*ship_width,y - 0.5*ship_height))

def drawBackground():
    gameDisplay.blit(bgImg, (0, 0))

# Funksjon for å vise en stor tekst midt på skjermen
def message_display(text):
    largeFont = pygame.font.Font('elektra.otf',65)
    textImage = largeFont.render(text, True, red)
    textRect = textImage.get_rect()
    textRect.center = ((display_width/2),(display_height/2))

    gameDisplay.blit(textImage, textRect)

    pygame.display.update()

    time.sleep(2)
    
def crash():
    message_display("You Crashed!")


finished = False
x = display_width * 0.5
y = display_height * 0.8
x_change = 0

while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

        # En tast ble trykket ned
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
                
        # En tast ble sluppet
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0

    x = x + x_change

    if x < 0.5*ship_width:
        crash()
        x = display_width * 0.5

    if x < 0.5*ship_width:
        x = 0.5*ship_width

    if x > display_width - 0.5*ship_width:
        x = display_width - 0.5*ship_width

    drawBackground()
    drawShip(x, y)

    pygame.display.update()
    clock.tick(60)

quit()
