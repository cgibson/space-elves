from controllers.controller import Controller
from models.player import PlayerModel

class PlayerController (Controller):
    def __init__(self):
        self.model = PlayerModel
        