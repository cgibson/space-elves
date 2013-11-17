### We use python files as data files. This will instantiate a default set of views 
### for the game using constructors. This way we don't have to write any file format or parsers
### or even interpret standard formats.
from controllers.board import BoardController
from controllers.lane import LaneController
from controllers.cardslot import CardSlotController
from controllers.game import GameController
from controllers.player import PlayerController

from models.board import BoardModel
from models.player import PlayerModel

from views.board import BoardView
from views.lane import LaneView
from views.cardslot import CardSlotView
from views.game import GameView
from views.card import CardView
from views.player import PlayerView
from views.deck import DeckView

from util.math import *
import global_mod as g
class DefaultBoardSceneGraph (BoardModel):
    def __init__(self):
        #self.size = # The canvas size can be calculated from the board sprites perhaps
        
        # load images
        g.image_manager.card_back    = "data/img/card_back.jpg"
        g.image_manager.board_back   = "data/img/board_background.png"
        g.image_manager.card_front   = "data/img/card_front.jpg"
        g.image_manager.ship_top     = "data/img/board_top.jpg"
        g.image_manager.ship_bottom  = "data/img/board_bottom.jpg"
        
        # init controllers
        gameController = GameController()
        gameController.board = BoardController()
        player1 = PlayerController()
        gameController.players.append(player1)
        player2 = PlayerController()
        gameController.players.append(player2)
        for player in gameController.players:
            player
        
        # init model
        gameController.model.players.append(PlayerModel())
        gameController.model.players.append(PlayerModel())
        
        # init views
        gameView = GameView()
        boardView = BoardView()
        boardView.children.append(LaneView()) # left
        boardView.children.append(LaneView()) # middle
        boardView.children.append(LaneView()) # right
        for playerModel in gameController.model.players:
            playerView = PlayerView()
            boardView.children.append(playerView)
            playerView.children.append(DeckView())
        playerView
        gameView.children.append(boardView)

        self.root = gameView
    
    def initControllers(self):
        pass
        
    def initModel(self):
        
        pass
        # NOT DONE YET, JUST A PLACEHOLDER
        
    ### No logic should be in this file. Just setting up positions/heirarchy/scene graph.