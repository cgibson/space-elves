""" Includes all code for handling and drawing cards
"""

from sprite import *
from animation import *
import global_mod as g
from util.math import *
import pygame
class ButtonView (SpriteView):

    def __init__(self, pos, size, text="notext"):
        super(ButtonView, self).__init__( pygame.Rect(pos.x, pos.y, size.x, size.y) )

        self.text = text

    def draw(self):
        rect = self.getAbsoluteRect()
        g.screen.fill(self.fillcolor, rect)