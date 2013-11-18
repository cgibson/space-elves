from _event import *

class Ship (Event):
    pass

class ShipDamage (Ship):

    def __init__(self, lane, card):
        super(ShipDamage, self).__init__("Ship Damaged")


class ShipHullBreached (Ship):
    pass