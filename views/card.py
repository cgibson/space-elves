""" Includes all code for handling and drawing cards
"""

from sprite import *
from animation import *
from events.event import *
import global_mod as g

class CardView (SpriteView):

    def __init__(self, pos):
        super(CardView, self).__init__( (pos.x, pos.y, 200, 270) )

        self.visible = False
        self.played = False
        self.status = STATIC
        self.effects = {
            "hover" : False,
            "highlight" : False,
            "Disabled" : False,
        }

        self.listening = True

    def draw(self):
        if self.played:
            g.screen.blit(g.image_manager.card_slot, (100,100,50,50))
        elif self.visible:
            g.screen.blit(g.image_manager.card_front, (100,100,50,50))
        else:
            g.screen.blit(g.image_manager.card_back, (100,100,50,50))

        #super(Card, self).draw()

    #def notify(self, event):
    #    if(isinstance(event, MouseButtonPressedEvent#)):
    #        if self.inBounds(event.mousePos):
    #            g.event_manager.post(CardClicked(self))
