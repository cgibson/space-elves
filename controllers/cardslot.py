__author__ = 'jleaders'
from controllers.controller import Controller
from views import *

class CardSlotController (Controller):
    
    def __init__(self):
        super(CardSlotController, self).__init__()
        self.card = None # contains reference to a card or None
        self.view = CardSlotView()

    def addCard(self, card):

        # TODO: Check to see if there are other cards in the slot already

        self.card = card
        self.card.release()
        self.card.setPlayed(True)
        self.view.setChildren([card.view])
        
    def isOccupied(self):
        return (self.card != None)