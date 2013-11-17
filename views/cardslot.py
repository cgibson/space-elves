from views.sprite import SpriteView

import global_mod as g

class CardSlotView (SpriteView):
    def __init__(self):
        super(CardSlotView, self).__init__(g.image_manager.card_slot)