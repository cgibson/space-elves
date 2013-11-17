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

class StartTurn (object):

    def __init__(self, player):
        super(StartTurn, self).__init__("Start Turn")
        self.player = player
