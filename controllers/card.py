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