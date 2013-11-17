__author__ = 'jleaders'
from controllers.controller import Controller
from views import *

class CardSlotController (Controller):
    
    def __init__(self):
        super(CardSlotController, self).__init__()
        self.card = None # contains reference to a card or None
        self.view = CardSlotView()