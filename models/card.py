from model import *

class CardModel (Model):

    def __init__(self, ownerId):
        super(CardModel, self).__init__()
        self.power = 1
        self.currentPower = 0
        self.attackBonus = 0
        self.movement = 1
        self.priority = 0 # lower is better

        self.visible = False # whether the card is visible to the player
        self.ownerId = ownerId # Current owner
        self.inSlot = False
        self.currentMovement = 0
        self.priority = 0 # lower is better