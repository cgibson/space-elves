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

from util.math import *

class DefaultBoardSceneGraph (BoardModel):
    def __init__(self):
        #self.size = # The canvas size can be calculated from the board sprites perhaps
        self.initViews()
        
        # init controllers
        gameController = GameController()
        gameController.board = BoardController()
        player1 = PlayerController()
        gameController.players.append(player1)
        player2 = PlayerController()
        gameController.players.append(player2)
        player1

        # init views
        gameView = GameView()
        boardView = BoardView()
        boardView.children.append(LaneView()) # top
        boardView.children.append(LaneView()) # mid
        boardView.children.append(LaneView()) # bot
        #boardView.children.append(PlayerView())
        #gameView.children.append(boardView)

        #gameView.children.append(cardView)
        #gameView.setListening(True)

        self.root = gameView


        #boardView = BoardView(0,0)
        #boardView.lane.append(LaneController(5)) # top
        #boardView.lane.append(LaneController(5)) # mid
        #boardView.lane.append(LaneController(5)) # bot
        # NOT DONE YET, JUST A PLACEHOLDER
        #gameView.children.append(boardView)
        #return view
        pass

    def initControllers(self):
        pass
        
    def initModel(self):

        pass
        # NOT DONE YET, JUST A PLACEHOLDER
        
    ### No logic should be in this file. Just setting up positions/heirarchy/scene graph.