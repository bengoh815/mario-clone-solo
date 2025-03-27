from 'declaration.py' import *
import pygame
import sys

pygame.init()
# create a screen instance/object with 
# 1000px width and 448px height

screen = pygame.display.set_mode((1000, 448))

# I forgot to mention 'Clock'
clock = pygame.time.Clock()

# import images & animation here
# Tips: The bricks (floor) is 48px height


# import fonts here

while True:

    pygame.display.update()
    clock.tick(60) #limit our game to 60 fps no matter what