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

        if isinstance(event, MouseButtonPressedEvent):
            if self.view.inBounds(event.mousePos):
                self.view.played = not self.view.played