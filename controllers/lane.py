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

    def notify(self, event):
        super(Controller, self).notify(event)

        if isinstance(event, events.StartTurn):
            print "Start Turn Received"
            for x in range(len(self.cardSlots), 0, -1):
                if x != 0:
                    self.cardSlots[x] = self.cardSlots[x-1]
                else:
                    self.cardSlots[x] = None
        #TODO Check Which Player It Is
        #TODO Advance all cards belonging to the player up or down depending on the player