from controllers.controller import Controller
from views.card import CardView
from util.math import *

class CardController (Controller):
    def __init__(self):
        self.view = CardView(Position(0,0))