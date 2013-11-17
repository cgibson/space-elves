from controllers.controller import Controller
from views.card import CardView
from events.event import CardClicked
from util.math import *

class CardController (Controller):

    def __init__(self):
        super(CardController, self).__init__()
        self.view = CardView(Position(0,0))


    def notify(self, event):
        super(Controller, self).notify(event)

        print "I got something..."

        if isinstance(event, CardClicked):
            print "I HAVE RECEIVED CARD CLICKED!"