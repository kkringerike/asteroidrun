import pygame
import time
import random

class Player (pygame.sprite.Sprite):
   def __init__(self, x, y):
      pygame.sprite.Sprite.__init__(self)
      
      # Les inn bildet som skal brukes til romskip
      self.image = pygame.image.load("spaceship.png")

      # Sett opp en boks rundt bildet
      self.rect = self.image.get_rect()

      # Sett startposisjon til bildet
      self.rect.left = x - self.rect.width*0.5
      self.rect.top = y - self.rect.height*0.5


   def updatePosition(self, x_speed, width):
      self.rect.left += x_speed

      if self.rect.left < 0:
         self.rect.left = 0

      if self.rect.right > width:
         self.rect.right = width
         
   def setPosition(self, x, y):
      self.rect.left = x - self.rect.width*0.5
      self.rect.top = y - self.rect.height*0.5


pygame.init()

display_width = 600
display_height = 800

# Farger
red = (255, 0, 0)
white = (255, 255, 255)

gameDisplay = pygame.display.set_mode((600,800))
pygame.display.set_caption('Asteroid Run')

all_sprites_list = pygame.sprite.Group()

clock = pygame.time.Clock()

bgImg = pygame.image.load("background.png")
asterImg = pygame.image.load("asteroid.png")

aster_width = asterImg.get_width()
aster_height = asterImg.get_height()

def drawAsteroid(x, y):
    gameDisplay.blit(asterImg, (x - 0.5*aster_width,y - 0.5*aster_height))

def drawBackground():
    gameDisplay.blit(bgImg, (0, 0))

# Funksjon for å vise en stor tekst midt på skjermen
def messageDisplay(text):
    largeFont = pygame.font.Font('elektra.otf',65)
    textImage = largeFont.render(text, True, red)
    textRect = textImage.get_rect()
    textRect.center = (display_width/2, 100)

    gameDisplay.blit(textImage, textRect)

    pygame.display.update()

    time.sleep(2)


def drawScore():
    text = "Score: " + str(score)
    font = pygame.font.Font('elektra.otf',20)
    textImage = font.render(text, True, white)
    textRect = textImage.get_rect()
    textRect.center = (display_width/2, 10)
    gameDisplay.blit(textImage, textRect)

    
def crash():
    messageDisplay("You Crashed!")


finished = False
x_change = 0

player = Player(display_width * 0.5, display_height * 0.8)
all_sprites_list.add(player)

aster_x = random.randrange(0, display_width)
aster_y = -200
aster_speed = 7

score = 0

def checkCollision():
    return False


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


    aster_y += aster_speed

    player.updatePosition(x_change, display_width)

    all_sprites_list.update()
 
    drawBackground()
    drawAsteroid(aster_x, aster_y)
    drawScore()
    
    if aster_y > display_height + 0.5*aster_height:
        aster_x = random.randrange(0, display_width)
        aster_y = -200
        score += 100
        aster_speed += 1
        
    if checkCollision():        
        crash()
        player.setPosition(isplay_width * 0.5, display_height * 0.8)
        aster_x = random.randrange(0, display_width)
        aster_y = -200
        score = 0
        aster_speed = 7

    all_sprites_list.draw(gameDisplay)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
