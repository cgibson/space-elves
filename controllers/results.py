__author__ = 'jleaders'
from views.results import *
from controllers.controller import *

from views import *

class ResultsController (Controller):
    
    def __init__(self):
        super(ResultsController, self).__init__()
        self.card = None # contains reference to a card or None
        self.view = ResultsView(Position(0, 150), Dimensions(1280, 420))

    def display(self, result):
        self.view.winner = result
        self.view.visible = True