# --------------------------------------------------- #
#   * * *   *   *  * * *      *     **    **  * * *   #
#   *   *    * *   *   *     * *    * *  * *  *       #
#   * * *    **    *         * *    *  *   *  * * *   #
#   *        *     *  **    * * *   *  *   *  *       #
#   *       *      * * *   *     *  *      *  * * *   #
# --------------------------------------------------- #

import pygame
import sys

pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Бомба діровка')

clock = pygame.time.Clock()
clock_tick = 60

spyder_image = pygame.image.load('images/spyder.png')
spyder_image_position= {'x': 0, 'y': 0}

backround_surface = pygame.Surface((screen_width, screen_height))
backround_surface.fill('Black')
while True:
    # Слідкуємо за подіями
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        spyder_image_position['y'] -= 0
    if keys[pygame.K_s]:
           spyder_image_position['y'] += 1

    screen.blit(backround_surface,(0,0))
    screen.blit(spyder_image,(spyder_image_position['x'] , spyder_image_position['y']))


    pygame.display.update()