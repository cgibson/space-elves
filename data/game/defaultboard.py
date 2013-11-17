### We use python files as data files. This will instantiate a default set of views 
### for the game using constructors. This way we don't have to write any file format or parsers
### or even interpret standard formats.
from model.board import *
from views.board import *
from views.lane import *
from views.cardslot import *
from controllers.board import * 
from controllers.lane import * 
from controllers.cardslot import * 

class DefaultBoardSceneGraph (BoardModel):
    def __init__(self):
        #self.size = # The canvas size can be calculated from the board sprites perhaps
        pass
        
    def initViews(self):

        
        #boardView = BoardView(0,0)
        #boardView.lane.append(LaneController(5)) # top
        #boardView.lane.append(LaneController(5)) # mid
        #boardView.lane.append(LaneController(5)) # bot
        # NOT DONE YET, JUST A PLACEHOLDER
        #gameView.children.append(boardView)
        #return view
        pass

    def initControllers(self):
        pass
        
    def initModel(self):
        pass
        # NOT DONE YET, JUST A PLACEHOLDER
        
    ### No logic should be in this file. Just setting up positions/heirarchy/scene graph.