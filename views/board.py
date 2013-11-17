from views.sprite import SpriteView
from pygame.rect import Rect
from controllers.resource import ResourceController 
import global_mod as g

class BoardView(SpriteView):
    def __init__(self):
        super(BoardView, self).__init__(Rect(0,0,1280,720), g.image_manager.board_back)
        