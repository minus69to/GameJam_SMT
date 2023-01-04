import pygame
from pygame import mixer
import random
import math

#initialize pygame
pygame.init()

#creating screen
screen = pygame.display.set_mode((800,600))

#background
background = pygame.image.load("backgroundSMT.jpg")
background = pygame.transform.scale(background, (800, 600)).convert_alpha()

#caption & icon
pygame.display.set_caption("Welcome to new adventure!")
icon = pygame.image.load("iconSMT.png")
pygame.display.set_icon(icon)


#gameloop
while True:
    screen.fill((0,0,0))
    #backgrounf image
    screen.blit(background,(0,0))
    pygame.display.update()
