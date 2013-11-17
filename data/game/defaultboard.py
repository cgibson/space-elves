### We use python files as data files. This will instantiate a default set of views 
### for the game using constructors. This way we don't have to write any file format or parsers
### or even interpret standard formats.

def initViews():
    from views.board import *
    from views.lane import *
    from views.cardslot import *
    gameView.children.append(boardView)
    boardView = BoardView(0,0)
    boardView.lane.append(LaneController(5)) # top
    boardView.lane.append(LaneController(5)) # mid
    boardView.lane.append(LaneController(5)) # bot
    # NOT DONE YET, JUST A PLACEHOLDER
    return view

def initControllers():
    from controllers.board import * 
    from controllers.lane import * 
    from controllers.cardslot import * 
    
    # NOT DONE YET, JUST A PLACEHOLDER