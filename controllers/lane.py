from models.lane import LaneModel
from views.lane import LaneView
from controllers.cardslot import *
from controllers.controller import Controller
import events
import Queue

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
        if slotNum > len(self.cardSlots) - 1:
            #You've hit the enemy ship.
            int
        if slotNum == -1:
            #You've hit the hero ship
            int
        test = self.cardSlots[slotNum].isOccupied();
        if self.cardSlots[slotNum].isOccupied():
            print card.model
            print self.cardSlots[slotNum].card
            if card.model.ownerId == self.cardSlots[slotNum].card.model.ownerId:
                print "allied conflict occured, bounce!"
                return self.placeCard(card, slotNum + 1)
            else:
                print "enemy conflict occured, attack!"
                card = card.attack(self.cardSlots[slotNum])

        self.cardSlots[slotNum].card = card
        self.cardSlots[slotNum].view.card = card

    def removeCard(self, slotNum):
        returnCard = self.cardSlots[slotNum]
        self.cardSlots[slotNum].card = None
        self.cardSlots[slotNum].view.card = None
        return returnCard

    def startTurn(self, player):
        #create collection of cards in the current lane
        processQueue = Queue.PriorityQueue()
        for x in range(0, len(self.cardSlots), 1):
            if self.cardSlots[x].isOccupied():
                processQueue.put((self.cardSlots[x].card.model.priority, self.cardSlots[x].card, x)) #stores the priority, the card controller, and the index to the slot of the lane

        print processQueue
        while not processQueue.empty():
            i = processQueue.get()
            self.removeCard(i[2])
            self.placeCard(i[1], i[2]+1)
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