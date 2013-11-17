from app import *

from controllers.game import *
from controllers.card import *

class TestSceneGraph (object):

    def __init__(self):
        pass

    def initControllers(self):

        gameController = GameController()
        cardController = CardController()


        cardController.view.position = Position(100,100)

        gameController.rect = pygame.Rect(0,0,500,500)
        gameController.view.children.append(cardController.view)

        self.root = gameController.view
        gameController.view.listening = True


app = App(sceneGraph=TestSceneGraph())
app.run()