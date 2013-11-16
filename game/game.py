import sys

import pygame

from views.card import Card


# Initialization
import global_mod as g

def run():
    pygame.init()


    size = width, height = 500, 500
    speed = [2, 2]
    black = 0, 0, 0

    g.screen = pygame.display.set_mode(size)


    card = Card()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        g.screen.fill(black)
        card.draw()
        pygame.display.flip()

if __name__ == "__main__":
    run()