from controllers.controller import Controller
from views.card import CardView
from models.card import CardModel
import events
from util.math import *
import pygame

class CardController (Controller):

    def __init__(self):
        super(CardController, self).__init__()
        self.view = CardView(Position(0,0))
        self.model = CardModel()


    def notify(self, event):
        super(Controller, self).notify(event)

        if isinstance(event, events.MouseReleased):
            if self.view.grabbed:
                self.view.grabbed = False

    def grab(self):
        self.view.grabbed = True
        self.view.grabbedPos = Position(*pygame.mouse.get_pos())

    #self.card is attacking the passed card
    #apply damage and return the winning object
    def attack(self, card):
        if self.model.currentPower + self.model.attackBonus >= card.model.currentPower:
            if self.model.currentPower - card.model.currentPower <= 0:
                card.explode()
                return None
            card.explode()
            return self
        else:
            card.model.currentPower = card.model.currentPower - (self.model.currentPower + self.model.attackBonus)
            self.explode()
            return card

    def explode(self):
        self.model.currentPower = 0
        print "this card has exploded"