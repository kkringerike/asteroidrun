import pygame
import time
import random

pygame.init()

display_width = 600
display_height = 800

class Player (pygame.sprite.Sprite):
   def __init__(self, x, y):
      pygame.sprite.Sprite.__init__(self)
      
      # Les inn bildet som skal brukes til romskip
      self.image = pygame.image.load("spaceship.png")

      # Sett størrelsen lik størrelsen på bildet
      self.rect = self.image.get_rect()

      # Sett startposisjon til bildet
      self.rect.centerx = x
      self.rect.centery = y


   def updatePosition(self, x_speed):
      self.rect.left += x_speed

      if self.rect.left < 0:
         self.rect.left = 0

      if self.rect.right > display_width:
         self.rect.right = display_width
         

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Asteroid Run')

clock = pygame.time.Clock()

bgImg = pygame.image.load("background.png")

def drawBackground():
    gameDisplay.blit(bgImg, (0, 0))

finished = False
x_change = 0

player = Player(display_width * 0.5, display_height * 0.8)

sprites_list = pygame.sprite.Group()
sprites_list.add(player)

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

    drawBackground()
    
    sprites_list.draw(gameDisplay)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
