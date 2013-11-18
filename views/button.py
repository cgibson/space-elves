""" Includes all code for handling and drawing cards
"""

from sprite import *
from animation import *
import global_mod as g
import util
import pygame
class ButtonView (SpriteView):

    def __init__(self, pos, size, text="notext"):
        super(ButtonView, self).__init__( pygame.Rect(pos.x, pos.y, size.x, size.y) )

        self.text = text
        self.fontType = "helvetica"

    def draw(self):
        rect = self.getAbsoluteRect()
        g.screen.fill(self.fillcolor, rect)

        label = g.fonts[self.fontType].getCached(self.text)
        labelRect = label.get_rect()

        centerRect = util.centerRect(labelRect, rect)

        g.screen.blit(label,centerRect)