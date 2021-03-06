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
        if isinstance(image, basestring):
            self.image = pygame.image.load(image)
        else:
            self.image = image
        self.rect = self.image.get_rect()

    def draw(self):

        rect = self.getAbsoluteRect()
        
        if self.image:
            g.screen.blit(self.image, rect)
        
        super(SpriteView, self).draw()