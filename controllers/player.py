from controllers.controller import Controller
import events
from models.player import PlayerModel
from views.player import PlayerView

class PlayerController (Controller):
    def __init__(self):
        super(PlayerController, self).__init__()
        self.model = PlayerModel()
        self.view  = PlayerView()
        self.hand = None
        self.resource = 0

    def notify(self, event):
        super(Controller, self).notify(event)

        if isinstance(event, events.StartTurn):
            self.resource += 2
            #TODO Check if it is the active player