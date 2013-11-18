from controllers.controller import Controller
import events
from models.player import PlayerModel
from views.player import PlayerView

class PlayerController (Controller):
    def __init__(self):
        super(PlayerController, self).__init__()
        self.model = PlayerModel()
        self.view  = PlayerView()
        self.deck = None
        self.hand = None
        self.sections = []
        self.mana = None
        self.resource = 0

    def notify(self, event):
        super(Controller, self).notify(event)

        if isinstance(event, events.StartTurn):
            self.resource += 2
            #TODO Check if it is the active player

    def setVisibility(self, visible):
        self.hand.setVisibility(visible)
        self.view.updateAll()

    def takeDamage(self, section, damage):
        self.sections[section].takeDamage(damage)

    def expendMana(self, amount):
        if amount > self.mana.model.curHealth:
            raise ValueError("Too little mana!")

        self.mana.takeDamage(amount)

    def hasEnoughMana(self, amountNeeded):
        return amountNeeded <= self.mana.model.curHealth

    def drawCard(self):
        card = self.deck.drawCard()
        self.hand.addCard(card)
        self.view.updateAll()