from _event import *

class Ship (Event):
    pass

class ShipDamage (Ship):

    def __init__(self, lane, card):
        super(ShipDamage, self).__init__("Ship Damaged")
        self.lane = lane
        self.card = card


class ShipHullBreached (Ship):
    pass