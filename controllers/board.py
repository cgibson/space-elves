__author__ = 'cgibson'
from controllers.controller import Controller
from models.board import BoardModel
from views.board import BoardView

class BoardController (Controller):
    
    def __init__(self):
        self.model = BoardModel()
        self.view = BoardView()
        self.lanes = []