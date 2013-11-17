from views.sprite import SpriteView
from pygame.rect import Rect
import global_mod as g

class CardSlotView (SpriteView):
    def __init__(self):
        super(CardSlotView, self).__init__(Rect(0,0,150,30), g.image_manager.card_slot)
        self.cardView = None

    def draw(self):

        rect = self.getAbsoluteRect()

        if self.cardView:
            print "DRAWING IN %s" % rect
            g.screen.fill((255,255,255), rect)
        else:
            super(CardSlotView, self).draw()