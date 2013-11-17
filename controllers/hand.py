from views.hand import HandView
from models.hand import HandModel
from controllers.controller import Controller

class HandController (Controller):
    def __init__(self):
        self.view = HandView()
        self.model = HandModel()
        self.cards = []