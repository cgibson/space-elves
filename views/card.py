""" Includes all code for handling and drawing cards
"""

from sprite import *
from animation import *
import global_mod as g

class CardView (SpriteView):

    def __init__(self, pos):
        super(CardView, self).__init__( (pos.x, pos.y, 100, 100) )

        g.image_manager.card_front = "data/img/card_front.jpg"
        g.image_manager.card_back = "data/img/card_back.jpg"


        self.visible = False
        self.status = STATIC
        self.effects = {
            "hover" : False,
            "highlight" : False,
            "Disabled" : False,
        }

    def draw(self):
        if self.visible:
            g.screen.blit(g.image_manager.card_front, (100,100,50,50))
        else:
            g.screen.blit(g.image_manager.card_back, (100,100,50,50))

        #super(Card, self).draw()

    def notify(self, event):
        print "Card received event: %s" % event