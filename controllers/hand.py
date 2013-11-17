from views.hand import HandView
from models.hand import HandModel
from views.card import CardView
from controllers.controller import Controller
import events

class HandController (Controller):
    def __init__(self):
        super(HandController, self).__init__()
        self.view = HandView()
        self.model = HandModel()
        self.cards = []

    def notify(self, event):
        if (isinstance(event, events.MouseDown)):

            # Go for last drawn, reverse the list
            cards = self.cards
            cards.reverse()
            for idx, card in enumerate(cards, 0):
                if card.view.inBounds(event.mousePos):
                    card.grab()
                    break

    def removeCard(self, card):

        try:
            self.view.removeChild(card.view)
            idx = self.cards.index(card)
            del self.cards[idx]

        except Exception, e:
            raise ValueError("No such card in hand. %s" % str(e))