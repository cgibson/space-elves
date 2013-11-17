from controller import Controller
from controllers.board import BoardController
from controllers.player import PlayerController
from views.game import GameView
from models.game import GameModel

class GameController (Controller):

    def __init__(self):
        self.view = GameView()
        self.model = GameModel()
        self.board = BoardController()
        self.players = []
        
    #def win(player?):
    #    pass
    
    