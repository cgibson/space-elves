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
        self.over       = (255,255,0)

        self.fontType = "helvetica"

    def draw(self):
        rect = self.getAbsoluteRect()
        g.screen.fill(self.background, rect)

        percent = float(self.curHealth) / float(self.maxHealth)

        label = g.fonts[self.fontType].dropShadow("%s/%s" % (self.curHealth, self.maxHealth), offset=1, borderColor=(200,200,200))
        labelRect = label.get_rect()

        centerRect = util.centerRect(labelRect, rect)

        if percent < 1.0:
            healthRect = rect
            healthRect[2] *= percent
            g.screen.fill(self.foreground, healthRect)
        else:
            g.screen.fill(self.foreground, rect)

            overRect = rect.move(rect[2], 0)
            overRect[2] *= (percent - 1)

            g.screen.fill(self.over, overRect)


        g.screen.blit(label,centerRect)