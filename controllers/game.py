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
        self.hud   = None
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
            for card in self.players[self.currentPlayer].hand.cards:
                if card.view.grabbed:
                    grabbedCard = card
                    break

            if grabbedCard:
                print "Confirmed a card is grabbed"
                for lane in self.board.lanes:
                    if lane.view.inBounds(event.mousePos):
                        if self.playersTurn == 0:
                            lane.placeCard(grabbedCard, 0)
                        else:
                            lane.placeCard(grabbedCard, -1)
                        self.players[self.currentPlayer].hand.removeCard(grabbedCard)
                        break
                else:
                    card.release()
            else:
                print "No card grabbed"

        if isinstance(event, events.StartTurn):
            print "Starting Turn"
            for lane in self.board.lanes:
                lane.startTurn(self.playersTurn)

        if isinstance(event, events.MouseDown):
            print "mousedown"
            if event.mouseButton == 2:
                print "right click"
                g.event_manager.post(events.StartTurn())

        # End turn is called
        if isinstance(event, events.ButtonEndTurn):
            print "Ending turn! YAAAY"
            self.playersTurn += 1
            self.playersTurn %= len(self.players)

            # Since we're not networked. derp
            self.currentPlayer = self.playersTurn

            self.updateCardVisibilities()

            self.view.updateAll()
            self.update()


    def updateCardVisibilities(self):
        for idx, player in enumerate(self.players):

            if idx == self.currentPlayer:
                player.setVisibility(True)
            else:
                player.setVisibility(False)