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
from controllers.hud import HUDController
from controllers.button import ButtonController

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
        
        # Dimensions taken from https://www.dropbox.com/s/kd4u1ee5orponpn/ui-mockup3.jpg
        handMargin = Dimensions(450,0)
        screenSize = Dimensions(1280,720)
        handSize = Dimensions(screenSize.x-handMargin.x*2, 270)
        laneSize = Dimensions(170, 420)
        shipSize = Dimensions(1280,150)
        buttonSize = Dimensions(170,50)
        
        # load images
        g.image_manager.card_back    = "data/img/card_back.jpg"
        g.image_manager.card_front   = "data/img/card_front.jpg"
        g.image_manager.card_slot    = "data/img/card_slot.png"
        g.image_manager.ship_top     = "data/img/board_top.png"
        g.image_manager.ship_bottom  = "data/img/board_bottom.png"
        g.image_manager.board_back   = "data/img/board_background.png"
        
        # Initialize controllers which will in turn initialize the views and models.      
        gameController = GameController()
        gameController.board = BoardController()
        gameController.board.lanes.append(LaneController(7))
        gameController.board.lanes.append(LaneController(7))
        gameController.board.lanes.append(LaneController(7))
        gameController.hud = HUDController()
        gameController.hud.endTurnButton = ButtonController(Dimensions(screenSize.x - buttonSize.x, screenSize.y/2), buttonSize)
            
        player1 = PlayerController()
        player2 = PlayerController()
        gameController.players.append(player1)
        gameController.players.append(player2)
        for playerNum,player in enumerate(gameController.players):
            player.deck = DeckController()
            player.hand = HandController(True if playerNum is 0 else False)
            player.ship = ShipController()
            #for cardNumber in range(0,30):
            #    player.deck.addCard(CardController(playerNum))
            for cardNumber in range(0,7):
                player.hand.addCard(CardController(playerNum))
        
        # Assemble the views in a sensible parent/child heirarchy for this board.        
        for lane in gameController.board.lanes:
            for cardSlot in lane.cardSlots:
                lane.view.addChild(cardSlot.view)
            gameController.board.view.addChild(lane.view)
        gameController.view.addChild(gameController.board.view)
        for player in gameController.players:
            gameController.view.addChild(player.view)
            player.view.addChild(player.ship.view)
            player.view.addChild(player.deck.view)
            player.view.addChild(player.hand.view)
            #for card in player.deck.cards:
            #    player.deck.view.addChild(card.view)
            #for card in player.hand.cards:
            #    player.hand.view.addChild(card.view)
        
        # Set the positions & sizes.
        gameController.view.size = screenSize
        gameController.players[0].hand.view.position = Position(handMargin.x, handMargin.y - handSize.y / 2)
        gameController.players[0].hand.view.size     = handSize
        gameController.players[0].ship.view.position = Position(0, 0)
        gameController.players[0].ship.view.size     = shipSize
        gameController.players[1].hand.view.size     = handSize
        gameController.players[1].hand.view.position = Position(handMargin.x, screenSize.y - handMargin.y - handSize.y/2)
        gameController.players[1].ship.view.position = Position(0, screenSize.y - shipSize.y)
        gameController.players[1].ship.view.size     = shipSize
        gameController.players[1].ship.view.image    = g.image_manager.ship_bottom
        gameController.board.lanes[0].view.size     = laneSize
        gameController.board.lanes[0].view.position = Position(230+laneSize.x*0, 150)
        gameController.board.lanes[1].view.size     = laneSize
        gameController.board.lanes[1].view.position = Position(230+laneSize.x*2, 150)
        gameController.board.lanes[2].view.size     = laneSize
        gameController.board.lanes[2].view.position = Position(230+laneSize.x*4, 150)
        self.root = gameController.view
    
    def initControllers(self):
        pass
        
    def initModel(self):
        
        pass
        # NOT DONE YET, JUST A PLACEHOLDER
        
    ### No logic should be in this file. Just setting up positions/heirarchy/scene graph.