from _event import Event
from util.math import *
import pygame

class Mouse (Event):

    def __init__(self):
        super(Mouse, self).__init__("Mouse Event")
        self.mousePos = Position(*pygame.mouse.get_pos())


class MouseDown (Mouse):

    def __init__(self, mouseButton):
        super(MouseDown, self).__init__()
        self.mouseButton = mouseButton


class MouseReleased (Mouse):

    def __init__(self, mouseButton):
        super(MouseReleased, self).__init__()
        self.mouseButton = mouseButton
