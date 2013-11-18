__author__ = 'cgibson'
from controllers.controller import Controller
from models.board import BoardModel
from views.board import BoardView

class BoardController (Controller):
    
    def __init__(self):
        super(BoardController, self).__init__()
        self.model = BoardModel()
        self.view = BoardView()
        self.lanes = []

    def getBestLane(self, player):
        bestLane = 0
        currentPower = 0
        bestPower = 0
        for x in range(0, len(self.lanes)-1, 1):
            currentPower = self.lanes[x].sumPower(player)
            if bestPower < currentPower:
                bestPower = currentPower
                bestLane = x
        return bestLane
