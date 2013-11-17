from model import *

class CardModel (Model):

    def __init__(self):
        super(CardModel, self).__init__()
        self.power = 0
        self.currentPower = 0
        self.movement = 0
        self.priority = 0 # high is better