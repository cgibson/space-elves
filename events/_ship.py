from _event import *

class ShipDamage (Event):

    def __init__(self, lane, card):
        super(ShipDamage, self).__init__("Ship Damaged")