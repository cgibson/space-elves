""" Includes base classes for drawing sprites
"""
import pygame
import global_mod as g


class Sprite (object):

    def __init__(self, image):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()

    def draw(self):
        g.screen.blit(self.image, self.rect)