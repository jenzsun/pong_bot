"""Pong vs. bot (single player)"""

import pygame

pygame.init()

window = pygame.display.set_mode((750, 500))

pygame.display.set_caption('Pong')

run = True

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
