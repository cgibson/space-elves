from cardslot import *

class LaneController (object):
    
    def __init__(self, numCardSlots):
        self.cardSlots = [CardSlot()]*3