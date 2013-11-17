from views.sprite import SpriteView
from pygame.rect import Rect
import global_mod as g
class ShipView (SpriteView):
    def __init__(self):
        super(ShipView, self).__init__(Rect(0,0,1280,150), g.image_manager.ship_top)