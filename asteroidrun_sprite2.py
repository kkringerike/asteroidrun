import pygame
import time
import random

display_width = 600
display_height = 800

# Farger
red = (255, 0, 0)
white = (255, 255, 255)


class GameObject(pygame.sprite.Sprite):
   def __init__(self, x, y, filename):
      pygame.sprite.Sprite.__init__(self)
      
      # Les inn bildet som skal brukes til romskip
      self.image = pygame.image.load(filename)

      # Sett størrelsen lik størrelsen på bildet
      self.rect = self.image.get_rect()

      # Sett startposisjon til bildet
      self.setPosition(x, y)
      
   def setPosition(self, x, y):
      self.rect.centerx = x
      self.rect.centery = y


class Player(GameObject):
   def __init__(self, x, y):
      GameObject.__init__(self, x, y, "spaceship.png")

   def updatePosition(self, x_speed):
      self.rect.left += x_speed

      if self.rect.left < 0:
         self.rect.left = 0

      if self.rect.right > display_width:
         self.rect.right = display_width

class Asteroid(GameObject):
   def __init__(self, speed):
      aster_x = random.randrange(0, display_width)
      GameObject.__init__(self, aster_x, -200, "asteroid.png")

      self.speed = speed

   def updatePosition(self):
      self.rect.top += self.speed
         
   
pygame.init()

gameDisplay = pygame.display.set_mode((600,800))
pygame.display.set_caption('Asteroid Run')

all_sprites_list = pygame.sprite.Group()

clock = pygame.time.Clock()

bgImg = pygame.image.load("background.png")

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

# Lag spillerromskipet
x_change = 0
player = Player(display_width * 0.5, display_height * 0.8)
all_sprites_list.add(player)

# Lag asteroiden
aster_speed = 7
aster = Asteroid(aster_speed)
all_sprites_list.add(aster)

score = 0

finished = False
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
   
    player.updatePosition(x_change)
    aster.updatePosition()
 
    drawBackground()
    drawScore()

    # Sjekk om asteroiden er ferdig
    if aster.rect.top > display_height:
        # Fjern gammel asteroide fra tegnelisten
        all_sprites_list.remove(aster)

        score += 100

        # Lag ny asteroide med høyere fart
        aster_speed += 1
        aster = Asteroid(aster_speed)
        all_sprites_list.add(aster)
       

    # Sjekk for kollisjon
    if pygame.sprite.collide_mask(player, aster):        
        crash()
        player.setPosition(display_width * 0.5, display_height * 0.8)
        score = 0

        # Fjern gammel asteroide
        all_sprites_list.remove(aster)

        # Lag ny asteroide med standard fart
        aster_speed = 7
        aster = Asteroid(aster_speed)
        all_sprites_list.add(aster)

    # Tegn alle sprites
    all_sprites_list.draw(gameDisplay)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
