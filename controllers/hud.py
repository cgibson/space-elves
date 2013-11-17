from controllers.controller import Controller
from views.hud import HUDView
from models.hud import HUDModel

class HUDController (Controller):
    def __init__(self):
        super(HUDController, self).__init__()
        self.model = HUDModel()
        self.view  = HUDView()
        self.endTurnButton = None