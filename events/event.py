""" Base Event Class, including the EventManager
"""

import pygame
from util.math import *


class Event (object):
    """ Superclass for all events in the game
    """

    def __init__(self, name="Generic Event"):
        self.name = name

    def __str__(self):
        return self.name


class MouseEvent (Event):

    def __init__(self):
        super(MouseEvent, self).__init__("Mouse Event")
        self.mousePos = Position(*pygame.mouse.get_pos())


class MouseButtonPressedEvent (MouseEvent):

    def __init__(self, mouseButton):
        super(MouseButtonPressedEvent, self).__init__()
        self.mouseButton = mouseButton


class MouseButtonReleasedEvent (MouseEvent):

    def __init__(self, mouseButton):
        super(MouseButtonReleasedEvent, self).__init__()
        self.mouseButton = mouseButton


class CardClicked (Event):

    def __init__(self, card):
        super(CardClicked, self).__init__("Card Clicked")
        self.card = card