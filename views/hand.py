from views.view import View
import global_mod as g
import pygame
from util.math import *

class HandView (View):

    def __init__(self):
        super(HandView,self).__init__()
        self.fillcolor = (255,0,0)
        self.cardSpacing = 0
        self.update()

    def draw(self):
        g.screen.fill(self.fillcolor, self.rect)

        super(HandView, self).draw()


    def update(self):
        super(HandView, self).update()

        if self._children:
            totalWidth = 0
            for card in self._children:
                totalWidth += card.size.x

            if totalWidth < self.size.x:
                widthDiff = self.size.x - totalWidth
                self.cardSpacing = widthDiff / len(self._children)
                curOffset = (self.cardSpacing * 0.5)
            else:
                widthDiff = self.size.x - totalWidth
                self.cardSpacing = 100
                if len(self._children) != 0:
                    self.cardSpacing = widthDiff / (len(self._children))
                curOffset = 0

            for card in self._children:
                card.position = Position(curOffset, 0)
                curOffset += card.size.x + self.cardSpacing
