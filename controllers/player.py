from controllers.controller import Controller
from models.player import PlayerModel
from views.player import PlayerView

class PlayerController (Controller):
    def __init__(self):
        self.model = PlayerModel()
        self.view  = PlayerView()