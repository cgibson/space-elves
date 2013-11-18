""" Includes all code for handling and drawing cards
"""

from sprite import *
from animation import *
import global_mod as g
from util.math import *

class CardView (SpriteView):

    def __init__(self, pos, cardPrint):
        super(CardView, self).__init__( pygame.Rect(pos.x, pos.y, 200, 270) )

        self.visible = False
        self.inSlot = False
        self.status = STATIC
        self.fontType = "helvetica"
        self.effects = {
            "hover" : False,
            "highlight" : False,
            "Disabled" : False,
        }
        self.title = cardPrint.name
        self.power = str(cardPrint.power)
        self.manaCost = str(cardPrint.manaCost)
        self.movement = str(cardPrint.speed)
        safeFilename = cardPrint.name.replace(" ", "_").lower()
        self.cardImageName          = g.card_image_dir + safeFilename + ".png"
        self.cardMinimisedImageName = g.card_image_dir + safeFilename + '-minimised' + ".png"                
        self.listening = True
        self.grabbed = False
        self.grabbedPos = Position(0,0)
        
        # load images
        g.image_manager[self.cardImageName] = self.cardImageName
        g.image_manager[self.cardMinimisedImageName] = self.cardMinimisedImageName

    def draw(self):

        rect = self.getAbsoluteRect()

        if self.grabbed:
            newPos = Position(*pygame.mouse.get_pos())
            rect = rect.move(newPos.x - self.grabbedPos.x,
                             newPos.y - self.grabbedPos.y)

        if self.inSlot:
            g.screen.blit(g.image_manager.card_slot, rect)
            g.screen.blit(g.image_manager[self.cardMinimisedImageName], rect)
            g.screen.blit(g.fonts[self.fontType].getCached(self.power), rect)
            g.screen.blit(g.fonts[self.fontType].getCached(self.movement), rect)
            g.screen.blit(g.fonts[self.fontType].getCached(self.manaCost), rect)
        elif self.visible:
            g.screen.blit(g.image_manager.card_front, rect)
            g.screen.blit(g.fonts[self.fontType].getCached(self.title), rect)
            g.screen.blit(g.fonts[self.fontType].getCached(self.power), rect)
            g.screen.blit(g.fonts[self.fontType].getCached(self.movement), rect)
            g.screen.blit(g.fonts[self.fontType].getCached(self.manaCost), rect)
            g.screen.blit(g.image_manager[self.cardImageName], rect)
        else:
            g.screen.blit(g.image_manager.card_back, rect)

        super(CardView, self).draw()