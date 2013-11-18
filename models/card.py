from model import *
import global_mod as g

class CardModel (Model):

    def __init__(self, ownerId, cardPrint):
        super(CardModel, self).__init__()
        self.power = cardPrint.power
        self.currentPower = self.power
        self.attackBonus = 0
        self.movement = cardPrint.speed
        self.priority = 0 # lower is better

        self.visible = False # whether the card is visible to the player
        self.ownerId = ownerId # Current owner
        self.inSlot = False
        self.currentMovement = self.movement
        self.priority = 0 # lower is better
        self.manaCost = cardPrint.manaCost
        
        
class CardPrint(object): #instantiated by the CardPrintManager
    def __init__(self, name=None):
        self.name = None
        self.power = None
        self.manaCost = None
        self.helpText = None
        self.triviaText = None
        if (name):
            self = g.card_prints_manager[name] # is this a bad idea in python?