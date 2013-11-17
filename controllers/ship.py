from controllers.controller import Controller
from views.ship import ShipView

class ShipController (Controller):
    def __init__(self):
        super(ShipController, self).__init__()
        self.view = ShipView()
        