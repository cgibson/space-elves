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
            grabbedCard = None
            for card in self.players[self.currentPlayer].hand.cards:
                if card.view.grabbed:
                    grabbedCard = card
                    break

            if grabbedCard:
                for laneIdx, lane in enumerate(self.board.lanes, 0):
                    if lane.view.inBounds(event.mousePos):

                        if not self.players[self.playersTurn].hasEnoughMana(grabbedCard.model.manaCost):
                            grabbedCard.release()
                            break
                        self.players[self.playersTurn].expendMana(grabbedCard.model.manaCost)

                        if self.playersTurn == 0:
                            lane.placeCard(grabbedCard, 0)
                        else:
                            lane.placeCard(grabbedCard, lane.laneLength()-1)
                        self.players[self.currentPlayer].hand.removeCard(grabbedCard)
                        break
                else:
                    card.release()

        if isinstance(event, events.StartTurn):
            print "Starting Player %s Turn" %self.playersTurn
            for lane in self.board.lanes:
                lane.startTurn(self.playersTurn)

            # Now the player who's turn it is draws a card
            self.players[self.playersTurn].drawCard()
            self.players[self.playersTurn].gainMana()

            #AI Takes Over
            if self.playersTurn == 0:
                playLane = self.getSuggestedPlay()
                randomCard = self.players[self.playersTurn].hand.cards[0]
                if (self.players[self.currentPlayer].hasEnoughMana(randomCard.model.manaCost)):
                    self.players[self.currentPlayer].expendMana(randomCard.model.manaCost)   
                    self.board.lanes[playLane].placeCard(randomCard, 0)
                    self.players[self.currentPlayer].hand.removeCard(randomCard)
                
                g.event_manager.post(events.ButtonEndTurn(1))

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
            g.event_manager.post(events.StartTurn())

        if isinstance(event, events.ShipDamage):
            section = self.board.lanes.index(event.lane)
            if event.card.model.ownerId == 1:
                damagedPlayer = 0
            if event.card.model.ownerId == 0:
                damagedPlayer = 1
            self.players[damagedPlayer].takeDamage(section, event.card.model.power + event.card.model.attackBonus)

        if isinstance(event, events.GameOver):
            self.results.display(not self.players.index(event.player))

    def getSuggestedPlay(self):
        if self.playersTurn == 0:
            enemyPlayer = 1
        else:
            enemyPlayer = 0
        return self.board.getBestLane(enemyPlayer)

    def updateCardVisibilities(self):
        for idx, player in enumerate(self.players):

            if idx == self.currentPlayer:
                player.setVisibility(True)
            else:
                player.setVisibility(False)