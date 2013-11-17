from events.listener import EventListener

import pygame
import global_mod as g
from util.math import Position

class View (EventListener):
    
    def __init__(self, rect=pygame.Rect(0,0,10,10)):
        super(View, self).__init__()

        self.children = []
        self.parent = None
        self.fillcolor = (255,255,0)
        self.rect = rect

    def getAbsolutePosition(self):

        if self.parent:
            return self.position + self.parent.getAbsolutePosition()

        return self.position


    def draw(self):
        # For Debugging
        #print("Drawing " + str(self))
        #r = self.rect
        #r.move(self.getAbsolutePosition())
        #g.screen.fill(self.fillcolor, self.rect)

        for child in self.children:
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

    def inBounds(self, pos):
        return ((pos.x > self.rect[0]) and
               (pos.y > self.rect[1]) and
               (pos.x < self.rect[0] + self.rect[2]) and
               (pos.y < self.rect[1] + self.rect[3]))
