from math import *
import pygame

def centerRect(innerRect, outerRect):

    pos1 = Position(innerRect[0], innerRect[1])
    size1 = Dimensions(innerRect[2], innerRect[3])

    pos2 = Position(outerRect[0], outerRect[1])
    size2 = Dimensions(outerRect[2], outerRect[3])

    diff = size2 - size1
    end = pos2 + (diff * 0.5)

    return pygame.Rect(end.x, end.y, size1.x, size1.y)