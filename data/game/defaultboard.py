### We use python files as data files. This will instantiate a default set of views 
### for the game using constructors. This way we don't have to write any file format or parsers
### or even interpret standard formats.
from controllers.board import BoardController
from controllers.lane import LaneController
from controllers.cardslot import CardSlotController
from controllers.game import GameController
from controllers.player import PlayerController
from controllers.deck import DeckController
from controllers.hand import HandController
from controllers.card import CardController
from controllers.ship import ShipController

from models.board import BoardModel
from models.player import PlayerModel

from views.board import BoardView
from views.lane import LaneView
from views.cardslot import CardSlotView
from views.game import GameView
from views.card import CardView
from views.player import PlayerView
from views.deck import DeckView
from util.scenegraph import SceneGraph
from util.math import *
import global_mod as g
class DefaultBoardSceneGraph (SceneGraph):
    def __init__(self):
        #self.size = # The canvas size can be calculated from the board sprites perhaps
        
        # load images
        g.image_manager.card_back    = "data/img/card_back.jpg"
        g.image_manager.card_front   = "data/img/card_front.jpg"
        g.image_manager.card_slot    = "data/img/card_slot.png"
        g.image_manager.ship_top     = "data/img/board_top.png"
        g.image_manager.ship_bottom  = "data/img/board_bottom.png"
        g.image_manager.board_back   = "data/img/board_background.png"
        
        # init controllers which init views/models
        gameController = GameController()
        gameController.board = BoardController()
        gameController.board.lanes.append(LaneController(5))
        gameController.board.lanes.append(LaneController(5))
        gameController.board.lanes.append(LaneController(5))
        for lane in gameController.board.lanes:
            for cardSlotNumber in range(0, 11):
                lane.cardSlots.append(CardSlotController())
        player1 = PlayerController()
        player2 = PlayerController()
        gameController.players.append(player1)
        gameController.players.append(player2)
        for player in gameController.players:
            player.deck = DeckController()
            player.hand = HandController()
            player.ship = ShipController()
            for cardNumber in range(0,30):
                player.deck.cards.append(CardController())
            for cardNumber in range(0,7):
                player.hand.cards.append(CardController())
        
        # assemble the views in a sensible heirarchy for this board
        for lane in gameController.board.lanes:
            for cardSlot in lane.cardSlots:
                lane.view.addChild(cardSlot.view)
            gameController.board.view.addChild(lane.view)
        gameController.view.addChild(gameController.board.view)
        for player in gameController.players:
            gameController.view.addChild(player.view)
            player.view.addChild(player.ship.view)
            #player.view.children.append(player.deck.view)
            player.view.addChild(player.hand.view)
            #for card in player.deck.cards:
            #    player.deck.view.append(card.view)
            for card in player.hand.cards:
                player.hand.view.addChild(card.view)
        #for lane in gameController.board.lanes:
        #    lane.view.append()
            
        self.root = gameController.view
    
    def initControllers(self):
        pass
        
    def initModel(self):
        
        pass
        # NOT DONE YET, JUST A PLACEHOLDER
        
    ### No logic should be in this file. Just setting up positions/heirarchy/scene graph.