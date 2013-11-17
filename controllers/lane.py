from models.lane import LaneModel
from controllers.controller import Controller

class LaneController (Controller):
    
    def __init__(self, numCardSlots):
        self.model = LaneModel