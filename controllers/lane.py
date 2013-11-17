from models.lane import LaneModel
from views.lane import LaneView
from controllers.controller import Controller

class LaneController (Controller):
    
    def __init__(self, numCardSlots):
        self.model = LaneModel()
        self.view  = LaneView()
        self.cardSlots = []