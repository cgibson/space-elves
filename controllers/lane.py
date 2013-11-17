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

    def placeCard(self, card, slotNum):
        self.cardSlots[slotNum].card = card
        self.cardSlots[slotNum].view.card = card

    def startTurn(self, player):
        for x in range(len(self.cardSlots)-1, 0, -1):
            if x != 0:
                self.cardSlots[x].card = self.cardSlots[x-1].card
                self.cardSlots[x].view.card = self.cardSlots[x-1].view.card
            else:
                self.cardSlots[x].card = None
                self.cardSlots[x].view.card = None
        print self.cardSlots
        #TODO Check Which Player It Is
        #TODO Advance all cards belonging to the player up or down depending on the player