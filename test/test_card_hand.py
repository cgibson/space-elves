from app import *

from controllers import *
import global_mod as g

class TestSceneGraph (SceneGraph):

    def __init__(self):
        self.root = None

    def initControllers(self):

        g.image_manager.card_back = "data/img/card_back.jpg"
        g.image_manager.card_front = "data/img/card_front.jpg"

        c = Controller()
        c.view = View(pygame.Rect(0,0,500,500))

        hand = HandController()
        hand.position = Position(50,50)
        hand.size = Dimensions(500, 270)
        c.view.children.append(hand.view)

        for i in range(3):
            card = CardController()
            hand.cards.append(card.view)

        #cardSlotController = CardSlotController()
        #gameController.view.children.append(cardSlotController.view)
        #cardSlotController.view.position = Position(300,100)

        self.root = c.view


app = App(sceneGraphClass=TestSceneGraph)
app.run()