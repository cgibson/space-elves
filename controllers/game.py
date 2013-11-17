from controller import Controller
from controllers.board import BoardController
from controllers.player import PlayerController
from views.game import GameView
from models.game import GameModel
import events
import global_mod as g

class GameController (Controller):

    def __init__(self):
        super(GameController, self).__init__()
        self.view = GameView()
        self.model = GameModel()
        self.board = None
        self.players = []
        self.currentPlayer = 0 # Who do we see in the views?
        self.playersTurn = 0   # Who's turn is it?
        
    #def win(player?):
    #    pass


    def notify(self, event):

        if isinstance(event, events.MouseReleased):
            print "Got mouse released event"
            grabbedCard = None
            for card in self.players[0].hand.cards:
                if card.view.grabbed:
                    grabbedCard = card
                    break

            if grabbedCard:
                print "Confirmed a card is grabbed"
                for lane in self.board.lanes:
                    if lane.view.inBounds(event.mousePos):
                        lane.placeCard(grabbedCard)
                        self.players[0].hand.removeCard(grabbedCard)
                        break
            else:
                print "No card grabbed"

        if isinstance(event, events.MouseDown):
            print "mousedown"
            if event.mouseButton == 2:
                print "right click"
                g.event_manager.post(events.StartTurn)
