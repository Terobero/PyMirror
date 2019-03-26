#!/usr/bin/python
# encoding: utf-8
import pygame
from colors import *
from sites import *


pygame.init()

size = (400, 500)
screen = pygame.display.set_mode(size)#, pygame.FULLSCREEN)

pygame.display.set_caption("Rotate Text")

done = False
clock = pygame.time.Clock()

text_rotate_degrees = 0

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
               if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                   done = True

    screen.fill(BLACK)

    font = pygame.font.SysFont('Calibri', 25, True, False)

    text = font.render("text", True, WHITE)
    screen.blit(text, [0, 0])

    text = font.render("more text", True, WHITE)
    screen.blit(text, [0, 100])

    pygame.display.flip()

    clock.tick(60)

pygame.quit()