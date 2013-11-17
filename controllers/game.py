from controller import Controller
from views.game import GameView

class GameController (Controller):

    def __init__(self):
        self.view = GameView()