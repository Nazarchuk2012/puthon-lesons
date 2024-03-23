import pygame
import sys
import random
import time

pygame.init()
# Colors
white = (255, 255, 255)
yellow = (255, 255, 100)
black = (0, 0, 0)
red = (213,50,80)
green = (0,255, 0)
blue = (30, 56, 186)
#Window
dis_width = 600
dis_height = 400

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by Nazar')
clock = pygame.time.Clock()

def our_snake():
    pygame.draw.rect(dis, red, [10, 10, 50, 50])



def game_loop():
    game_over = False
    snake_list = []
    length_of_shake = 1

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pass
                if event.key == pygame.K_RIGHT:
                    pass
                if event.key == pygame.K_UP:
                    pass
                if event.key == pygame.K_DOWN:
                     pass

            our_snake()

            pygame.display.flip()
            clock.tick(60)

    pygame.quit()
    sys.exit()




game_loop()












































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































