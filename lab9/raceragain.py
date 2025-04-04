import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

# color definitions
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# new game variables
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
COIN_SPEED = 5
SCORE = 0
COIN_SCORE = 0 

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("as.png")

DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

# enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("en.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:  # reset if it goes off the screen
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("pl.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

# coin class (with random weight effect)
class Coin(pygame.sprite.Sprite): 
    def __init__(self): 
        super().__init__()
        self.image = pygame.image.load("cn.jpg")
        self.image = pygame.transform.scale(self.image, (50, 50)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        self.weight = random.randint(1, 3)  # assigning a random "weight" to the coin

    def move(self):
        self.rect.move_ip(0, COIN_SPEED + self.weight)  # speed depends on coin's weight
        if self.rect.top > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
            self.weight = random.randint(1, 3)  # reassign new weight when the coin respawns

    def respawn(self):
        self.rect.top = 0
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        self.weight = random.randint(1, 3)  # new random weight on respawn

# initialize player, enemy, and coin
P1 = Player()
E1 = Enemy()
C1 = Coin()

# groups for sprites
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)
coins = pygame.sprite.Group()
coins.add(C1)

# event to increase enemy speed
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# main game loop
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5  # increase enemy speed every second
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # fill the screen with background image
    DISPLAYSURF.blit(background, (0, 0))

    # display score and coin score
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))
    coin_score = font_small.render(str(COIN_SCORE), True, BLACK)
    DISPLAYSURF.blit(coin_score, (40, 10))

    # move and draw all sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # check collision between player and enemies
    if pygame.sprite.spritecollideany(P1, enemies):
        time.sleep(0.5)
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill() 
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # check collision between player and coins
    if pygame.sprite.spritecollideany(P1, coins):
        COIN_SCORE += 1
        if COIN_SCORE % 5 == 0:  # increase enemy speed every 5 coins collected
            SPEED += 1
        for entity in coins:
            entity.respawn()

    pygame.display.update()
    FramePerSec.tick(FPS)
