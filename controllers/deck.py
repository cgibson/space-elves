from controllers.controller import Controller

class DeckController (Controller):
    def __init__(self):
        super(DeckController, self).__init__()
        self.cards = [] # CardControllers