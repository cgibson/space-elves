from views.view import View
from pygame.rect import Rect
import global_mod as g
from util.math import *

class LaneView (View):
    def __init__(self):
        super(LaneView, self).__init__()
        self.fillcolor = (0,100,255)

    def draw(self):
        g.screen.fill(self.fillcolor, self.rect)

        super(LaneView, self).draw()


    def update(self):
        super(LaneView, self).update()

        if self._children:
            totalHeight = 0
            for slot in self._children:
                totalHeight += slot.size.y

            if totalHeight < self.size.y:
                heightDiff = self.size.y - totalHeight
                slotSpacing = heightDiff / len(self._children)
                curOffset = (slotSpacing * 0.5)
            elif len(self._children) == 1:
                heightDiff = self.size.y - totalHeight
                slotSpacing = 0
                curOffset = 0.5 * heightDiff
            else:
                heightDiff = self.size.y - totalHeight
                slotSpacing = heightDiff / (len(self._children) - 1)
                curOffset = 0

            for card in self._children:

                widthDiff = self.size.x - card.size.x

                card.position = Position(0.5 * widthDiff, curOffset)
                curOffset += card.size.y + slotSpacing