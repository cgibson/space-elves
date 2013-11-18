""" Includes all code for handling and drawing cards
"""

from sprite import *
from animation import *
import global_mod as g
import util
import pygame
class HealthBarView (SpriteView):

    def __init__(self, pos, size, maxHealth):
        super(HealthBarView, self).__init__( pygame.Rect(pos.x, pos.y, size.x, size.y) )

        self.maxHealth = maxHealth
        self.curHealth = maxHealth

        self.background = (255,0,0)
        self.foreground = (0, 255, 0)

        self.fontType = "helvetica"

    def draw(self):
        rect = self.getAbsoluteRect()
        g.screen.fill(self.background, rect)

        percent = float(self.curHealth) / float(self.maxHealth)

        healthRect = rect
        healthRect[2] *= percent

        g.screen.fill(self.foreground, rect)

        label = g.fonts[self.fontType].getCached("%s/%s" % (self.curHealth, self.maxHealth))
        labelRect = label.get_rect()

        centerRect = util.centerRect(labelRect, rect)

        g.screen.blit(label,centerRect)