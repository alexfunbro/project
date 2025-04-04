import pygame
import os
import math
import datetime

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Moving Ball")
clock = pygame.time.Clock()

ball_color = (255, 0, 0)
ball_radius = 25
ball_x = 175
ball_y = 125
ball_speed = 2

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_UP]:
        if ball_y - ball_radius > 0:
            ball_y -= ball_speed
    if pressed[pygame.K_DOWN]:
        if ball_y + ball_radius < 300:
            ball_y += ball_speed
    if pressed[pygame.K_LEFT]:
        if ball_x - ball_radius > 0:
            ball_x -= ball_speed
    if pressed[pygame.K_RIGHT]:
        if ball_x + ball_radius < 400:
            ball_x += ball_speed

    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()