from events.listener import EventListener

import pygame
import global_mod as g
from util.math import *



class View (object):

    num = 0

    def __init__(self, rect=pygame.Rect(0,0,10,10)):
        super(View, self).__init__()

        self._children = []

        self.parent = None
        self.fillcolor = (255,255,0)
        self.rect = rect
        self.cursorInteract = True

    def setParent(self, parent):
        self.parent = parent

    def getAbsolutePosition(self):

        if self.parent:
            return self.position + self.parent.getAbsolutePosition()

        return self.position

    def getAbsoluteRect(self):

        if self.parent:
            pos = self.getAbsolutePosition()
            return pygame.Rect(pos.x, pos.y, self.rect[2], self.rect[3])

        return self.rect

    def addChild(self, child):
        assert(child)
        self._children.append(child)
        child.setParent(self)
        self.updateAll()

    def setChildren(self, cards):
        self._children = []
        for card in cards:
            self.addChild(card)


    def removeChild(self, child):

        try:
            idx = self._children.index(child)
            del self._children[idx]

            self.updateAll()
        except Exception, e:
            raise ValueError("No such child view. %s" % str(e))



    def draw(self):
        # For Debugging
        #print("Drawing " + str(self))
        #r = self.rect
        #r.move(self.getAbsolutePosition())
        #g.screen.fill(self.fillcolor, self.rect)

        for child in self._children:
            child.draw()

    @property
    def position(self):
        return Position(self.rect[0],
                        self.rect[1])

    @position.setter
    def position(self, position):
        self.rect = pygame.Rect(position.x,
                                position.y,
                                self.rect[2],
                                self.rect[3])

    @property
    def size(self):
        return Dimensions(self.rect[2],
                          self.rect[3])

    @size.setter
    def size(self, size):
        print "SETTING SIZE"
        self.rect[2] = size.x
        self.rect[3] = size.y
        self.update()

    def inBounds(self, pos):

        rect = self.getAbsoluteRect()
        return ((pos.x > rect[0]) and
                (pos.y > rect[1]) and
                (pos.x < rect[0] + rect[2]) and
                (pos.y < rect[1] + rect[3]))

    def update(self):
        pass

    def updateAll(self):

        self.update()

        for child in self._children:
            child.updateAll()