from controllers.controller import Controller
from views.card import CardView
import events
from models.card import CardModel
from util.math import *
import pygame

class CardController (Controller):

    def __init__(self, playerId):
        super(CardController, self).__init__()
        self.view = CardView(Position(0,0))
        self.model = CardModel(playerId)

    def notify(self, event):
        super(Controller, self).notify(event)

        if isinstance(event, events.MouseReleased):
            if self.view.grabbed:
                self.view.grabbed = False

    def setVisible(self, visible):
        self.model.visible = visible
        self.view.visible = visible
        self.update()

    def playToSlot(self, slot):
        slot.addCard(self)
        self.model.inSlot = True
        self.view.inSlot = True
        self.update()

    def grab(self):
        self.view.grabbed = True
        self.view.grabbedPos = Position(*pygame.mouse.get_pos())