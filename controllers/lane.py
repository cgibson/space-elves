from models.lane import LaneModel
from views.lane import LaneView
from controllers.cardslot import *
from controllers.controller import Controller
import events

class LaneController (Controller):
    
    def __init__(self, numCardSlots):
        super(LaneController, self).__init__()
        self.model = LaneModel()
        self.view  = LaneView()
        self.cardSlots = []

        for i in range(numCardSlots):
            slot = CardSlotController()
            self.cardSlots.append(slot)
            self.view.addChild(slot.view)

    def placeCard(self, card):
        self.cardSlots[0].card = card
        self.cardSlots[0].view.card = card