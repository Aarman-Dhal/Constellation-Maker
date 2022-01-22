import pygame
import math

pygame.init()


screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Constellation Maker")

white = (255, 255, 255)
black = (0, 0, 0)
circle_val = []

def get_position():
    position = pygame.mouse.get_pos()
    circle_val.append(position)

def pop_value():
    for i in range(len(circle_val)):
        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]

        x_squared = (x - circle_val[i][0]) ** 2
        y_squared = (y - circle_val[i][1]) ** 2

        if math.sqrt(x_squared + y_squared) < 10:
            circle_val.pop(i)
            break

def remove_last():
    if len(circle_val) - 1  >= 0:
        circle_val.pop()

def remove_all():
    for i in range(len(circle_val)):
        circle_val.pop(len(circle_val) -1)
    
run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                get_position()
            elif event.button == 3:
                pop_value()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                remove_last()
            if event.key == pygame.K_2:
                remove_all()


    screen.fill(black)
    for j in range(len(circle_val)):
        pygame.draw.circle(screen, white, circle_val[j], 5)
        if len(circle_val) > 1:
            pygame.draw.line(screen, white, circle_val[j-1], circle_val[j], 5)

    pygame.display.flip()

pygame.quit()