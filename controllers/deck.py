from controllers.controller import Controller
from models.deck import DeckModel
from views.deck import DeckView

class DeckController (Controller):
    def __init__(self):
        super(DeckController, self).__init__()
        self.model = DeckModel()
        self.view  = DeckView()
        self.cards = [] # CardControllers