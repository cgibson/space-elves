""" Includes base classes for drawing sprites
"""
import pygame
import global_mod as g
from view import View


class SpriteView (View):

    def __init__(self, rect, image=None):
        super(SpriteView, self).__init__(rect)
        self.image = None

        if image:
            self.setImage(image)

    def setImage(self, image):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()

    def draw(self):
        if self.image:
            g.screen.blit(self.image, self.rect)
        else:
            super(SpriteView, self).draw()