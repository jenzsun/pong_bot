"""Pong vs. bot (single player)"""

import pygame

pygame.init()

window = pygame.display.set_mode((750, 500))

pygame.display.set_caption('Pong')

white = (255, 255, 255)
black = (0, 0, 0)

class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([10, 75])
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.points = 0

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.speed = 10
        self.dx = 1
        self.dy = 1

player_paddle = Paddle()
player_paddle.rect.x = 25
player_paddle.rect.y = 225

bot_paddle = Paddle()
bot_paddle.rect.x = 715
bot_paddle.rect.y = 225

paddle_speed = 20

ball = Ball()
ball.rect.x = 375
ball.rect.y = 250

all_sprites = pygame.sprite.Group()
all_sprites.add(player_paddle, bot_paddle, ball)

def redraw():
    window.fill(black)
    all_sprites.draw(window)
    pygame.display.update()

run = True

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            continue
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
                continue

    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        player_paddle.rect.y -= paddle_speed
    if key[pygame.K_s]:
        player_paddle.rect.y += paddle_speed

    ball.rect.x += ball.speed
    ball.rect.y += ball.speed

    redraw()

pygame.quit()
