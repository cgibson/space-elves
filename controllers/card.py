from controllers.controller import Controller
from views.card import CardView
import events
from util.math import *
import pygame

class CardController (Controller):

    def __init__(self):
        super(CardController, self).__init__()
        self.view = CardView(Position(0,0))


    def notify(self, event):
        super(Controller, self).notify(event)

        if isinstance(event, events.MouseReleased):
            if self.view.grabbed:
                self.view.grabbed = False

    def grab(self):
        self.view.grabbed = True
        self.view.grabbedPos = Position(*pygame.mouse.get_pos())