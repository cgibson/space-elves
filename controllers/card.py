from controllers.controller import Controller
from views.card import CardView
import events
from models.card import CardModel
from util.math import *
import pygame
import global_mod as g
class CardController (Controller):

    def __init__(self, playerId, cardPrint=None):
        if not cardPrint:
            cardPrint = g.card_prints_manager["Space Core"]#g.card_prints_manager.randomCard()
            
        super(CardController, self).__init__()
        self.view = CardView(Position(0,0),cardPrint)
        self.model = CardModel(playerId, cardPrint)

    def notify(self, event):
        super(Controller, self).notify(event)

    def setVisible(self, visible):
        self.model.visible = visible
        self.view.visible = visible
        self.update()

    def setPlayed(self, slot):
        self.model.inSlot = True
        self.view.inSlot = True
        self.view.position = Position(0,0)
        self.update()

    def grab(self):
        print "CARD IS GRABBED"
        self.view.grabbed = True
        self.view.grabbedPos = Position(*pygame.mouse.get_pos())

    def release(self):
        self.view.grabbed = False

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