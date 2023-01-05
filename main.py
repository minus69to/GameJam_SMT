import pygame
from pygame import mixer
import random
import math

#initialize pygame
pygame.init()

#creating screen
screen = pygame.display.set_mode((800,600))

#background
# background = pygame.image.load("backgroundSMT.jpg")
# background = pygame.transform.scale(background, (800, 600)).convert_alpha()

#caption & icon
pygame.display.set_caption("Welcome to new adventure!")
icon = pygame.image.load("iconSMT.png")
pygame.display.set_icon(icon)

#game variables
exit_game = False
game_over = False
snake_x = 45
snake_y = 55
velocity_x = 0
velocity_y = 0
snake_size = 20

init_velocity = 10

clock = pygame.time.Clock()
fps = 30

#snake plot
def plot_snake(gameWindow, color, snake_list, snake_size):
    for x,y in snake_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

snake_list = []
snake_length = 1

#gameloop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_x = init_velocity
                velocity_y = 0

            if event.key == pygame.K_LEFT:
                velocity_x = -init_velocity
                velocity_y = 0

            if event.key == pygame.K_UP:
                velocity_y = -init_velocity
                velocity_x = 0

            if event.key == pygame.K_DOWN:
                velocity_y = init_velocity
                velocity_x = 0

        snake_x = snake_x + velocity_x
        snake_y = snake_y + velocity_y

    screen.fill((0,0,0))
    #backgrounf image
    #screen.blit(background,(0,0))
    # pygame.display.update()
    # screen.fill((0, 0, 0))


    head = []
    head.append(snake_x)
    head.append(snake_y)
    snake_list.append(head)

    if len(snake_list) > snake_length:
        del  snake_list[0]


    plot_snake(screen, (0,0,255), snake_list, snake_size)
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()
