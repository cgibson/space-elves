""" Includes all code for handling and drawing cards
"""

from sprite import *
from animation import *

class Card (Sprite):

    def __init__(self):
        super(Card, self).__init__("data/img/card_back.jpg")

        self.visible = True
        self.status = STATIC
        self.effects = {
            "hover" : False,
            "highlight" : False,
            "Disabled" : False,
        }

    def draw(self):
        super(Card, self).draw()