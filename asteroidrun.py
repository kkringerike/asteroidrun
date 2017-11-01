import pygame
import random
import time

pygame.init()

display_width = 600
display_height = 800

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("spaceship.png")

        self.rect = self.image.get_rect()

        self.rect.centerx = x
        self.rect.centery = y

    def updatePosition(self, x_speed):
        self.rect.centerx += x_speed

        if self.rect.right > display_width:
            self.rect.right = display_width

        if self.rect.left < 0:
            self.rect.left = 0
        


class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("asteroid.png")

        self.rect = self.image.get_rect()

        self.rect.centerx = random.randrange(0, display_width)
        self.rect.centery = -200

    def updatePosition(self, y_speed):
        self.rect.centery += y_speed


gameDisplay = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption("Asteroid run")

clock = pygame.time.Clock()
bgImg = pygame.image.load("background.png")

def drawBackground():
    gameDisplay.blit(bgImg, (0, 0))

red = (255, 0, 0)

def crash():
    font = pygame.font.Font("elektra.otf", 65)
    textImage = font.render("You Died!", True, red)
    textRect = textImage.get_rect()
    textRect.center = (display_width/2, 100)

    gameDisplay.blit(textImage, textRect)
    pygame.display.update()

    time.sleep(2)
    

player = Player(display_width*0.5, display_height*0.8)

sprites_list = pygame.sprite.Group()
sprites_list.add(player)

asteroid = Asteroid()
sprites_list.add(asteroid)

x_change = 0
y_speed = 5

finished = False

while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            if event.key == pygame.K_RIGHT:
                x_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
        
    player.updatePosition(x_change)
    asteroid.updatePosition(y_speed)
    
    drawBackground()

    if asteroid.rect.top > display_height:
        sprites_list.remove(asteroid)

        asteroid = Asteroid()
        sprites_list.add(asteroid)


    if pygame.sprite.collide_mask(player, asteroid):
        crash()
        
        sprites_list.remove(asteroid)

        asteroid = Asteroid()
        sprites_list.add(asteroid)

        sprites_list.remove(player)
        player = Player(display_width*0.5, display_height*0.8)
        sprites_list.add(player)

        
    sprites_list.draw(gameDisplay)

    pygame.display.update()
    clock.tick(60)

pygame.quit()

    
