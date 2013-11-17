from views.sprite import SpriteView
from pygame.rect import Rect
import global_mod as g

class CardSlotView (SpriteView):
    def __init__(self):
        super(CardSlotView, self).__init__(Rect(0,0,150,30), g.image_manager.card_slot)
        self.card = None

    def draw(self):
        if self.card:
            g.screen.fill((255,255,255), self.rect)
        else:
            super(CardSlotView, self).draw()