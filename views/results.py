""" Includes all code for handling and drawing cards
"""

from sprite import *
from animation import *
import global_mod as g
import util
import pygame
class ResultsView (SpriteView):

    def __init__(self, pos, size, visible=False, winner=-1):
        super(ResultsView, self).__init__( pygame.Rect(pos.x, pos.y, size.x, size.y) )

        self.fontType = "helvetica72"
        self.visible = visible
        self.winner = winner

    def draw(self):

        if not self.visible:
            return
        rect = self.getAbsoluteRect()

        text = "Player %s Wins!" % (self.winner+1)
        color = (16,178,64)

        g.screen.fill(color, rect)

        label = g.fonts[self.fontType].dropShadow(text,borderColor=(0,87,26), cached=True)
        labelRect = label.get_rect()

        centerRect = util.centerRect(labelRect, rect)

        g.screen.blit(label,centerRect)