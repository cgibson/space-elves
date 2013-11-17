from model import *

class CardModel (Model):

    def __init__(self):
        super(CardModel, self).__init__()
        self.power = 0
        self.currentPower = 0
        self.attackBonus = 0
        self.movement = 0
        self.priority = 0 # high is better

        self.visible = False # whether the card is visible to the player
        self.ownerId = ownerId # Current owner
        self.inSlot = False
        self.currentMovement = 0
        self.priority = 0 # high is better