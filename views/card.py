""" Includes all code for handling and drawing cards
"""

from sprite import *
from animation import *
import global_mod as g
from util.math import *
import util
from pygame.rect import Rect

class CardView (SpriteView):

    def __init__(self, pos, cardPrint):
        super(CardView, self).__init__( pygame.Rect(pos.x, pos.y, 136, 206) )

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
        g.image_manager.mana_icon  = g.image_dir + "card_mana.png"
        g.image_manager.move_icon  = g.image_dir + "card_move.png"
        g.image_manager.power_icon = g.image_dir + "card_attack.png"
        g.image_manager.move_icon_min  = g.image_dir + "card_move-minimised.png"
        g.image_manager.power_icon_min = g.image_dir + "card_attack-minimised.png"
        self.manaIcon = g.image_manager.mana_icon
        self.moveIcon = g.image_manager.move_icon
        self.powerIcon = g.image_manager.power_icon
        self.listening = True
        self.grabbed = False
        self.grabbedPos = Position(0,0)
        self.movementColor = (0,255,0)
        self.manaColor = (0,0,255)
        self.powerColor = (255,0,0)
        self.minimisedIconSize = Dimensions(35,35)
        self.iconSize = Dimensions(50,50)
        
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
            rect[2] = 150
            rect[3] = 50
            
            # Draw minimised version.
            g.screen.blit(g.image_manager.card_slot, rect)
            g.screen.blit(g.image_manager[self.cardMinimisedImageName], rect)
            
            # Power icon.
            g.screen.blit(g.image_manager.power_icon_min, Rect(rect.left - self.minimisedIconSize.x, rect.bottom, self.minimisedIconSize.x, self.minimisedIconSize.y))
            g.fonts[self.fontType].color = self.powerColor
            g.screen.blit(g.fonts[self.fontType].getCached(self.power), Rect(rect.left, rect.top, self.minimisedIconSize.x, self.minimisedIconSize.y))
            
            # Movement icon.
            g.screen.blit(g.image_manager.move_icon_min, Rect(rect.right, rect.bottom, self.minimisedIconSize.x, self.minimisedIconSize.y))
            g.fonts[self.fontType].color = self.movementColor
            g.screen.blit(g.fonts[self.fontType].getCached(self.movement), Rect(rect.right, rect.top, self.minimisedIconSize.x, self.minimisedIconSize.y))
            
            # Player color outline.
            #g.screen.fill( (255,255,255), rect)
            
        elif self.visible:
            # Draw large version
            g.screen.blit(g.image_manager.card_front, rect)
            g.screen.blit(g.image_manager[self.cardImageName], rect)
            g.screen.blit(g.fonts[self.fontType].getCached(self.title), rect)
            
            # Power icon.
            iconRect = Rect(rect.right - self.iconSize.x, rect.top + self.iconSize.y, self.iconSize.x, self.iconSize.y)
            g.screen.blit(self.powerIcon, iconRect)
            g.fonts[self.fontType].color = self.powerColor
            g.screen.blit(g.fonts[self.fontType].getCached(self.power), Rect(rect.right, rect.top + self.iconSize.y, self.iconSize.x, self.iconSize.y))
            
            # Move icon.
            iconRect = Rect(rect.right - self.iconSize.x, rect.top, self.iconSize.x, self.iconSize.y)
            g.screen.blit(self.moveIcon, iconRect)
            g.fonts[self.fontType].color = self.movementColor
            g.screen.blit(g.fonts[self.fontType].getCached(self.movement), Rect(rect.right, rect.top, self.iconSize.x, self.iconSize.y))
            
            # Mana icon.
            iconRect = Rect(rect.left, rect.top, self.iconSize.x, self.iconSize.y)
            g.screen.blit(self.manaIcon, iconRect)
            g.fonts[self.fontType].color = self.manaColor
            g.screen.blit(g.fonts[self.fontType].getCached(self.manaCost), Rect(rect.left, rect.top, self.iconSize.x, self.iconSize.y))
            
        else:
            g.screen.blit(g.image_manager.card_back, rect)

        super(CardView, self).draw()