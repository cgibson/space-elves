from controllers.controller import Controller
from models.player import PlayerModel
from views.player import PlayerView

class PlayerController (Controller):
    def __init__(self):
        super(PlayerController, self).__init__()
        self.model = PlayerModel()
        self.view  = PlayerView()
        self.hand = None