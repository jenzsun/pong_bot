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
    # Title Font
    font = pygame.font.SysFont('monospace', 30)
    text = font.render('PONG', False, white)
    text_rect = text.get_rect()
    text_rect.center = (375, 25)
    window.blit(text, text_rect)

    # Player Score
    player_score = font.render(str(player_paddle.points), False, white)
    player_rect = player_score.get_rect()
    player_rect.center = (50, 50)

    # Bot Score
    player_score = font.render(str(player_paddle.points), False, white)
    player_rect = player_score.get_rect()
    player_rect.center = (50, 50)

    window.blit(player_score, player_rect)
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

    ball.rect.x += ball.speed * ball.dx
    ball.rect.y += ball.speed * ball.dy

    if ball.rect.x > 740:
        ball.rect.x, ball.rect.y = 375, 250
        ball.dx *= -1
        player_paddle.points += 1

    if ball.rect.x < 10:
        ball.rect.x, ball.rect.y = 375, 250
        ball.dx *= -1
        bot_paddle.points += 1

    if ball.rect.y > 490 or ball.rect.y < 10:
        ball.dy *= -1

    if player_paddle.rect.colliderect(ball.rect):
        ball.dx *= -1

    redraw()

pygame.quit()
