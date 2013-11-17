import sys, os, imp

import pygame

from controllers.event import *
from controllers.input import *
from controllers.resource import *

from data.game.defaultboard import * #HACK

# Initialization
import global_mod as g

g.event_manager = EventController()
g.input_manager = InputController()
g.image_manager = ImageController()

class App (object):

    def __init__(self, sceneGraph=DefaultBoardSceneGraph()):
        self.sceneGraph = sceneGraph

    def run(self):
        
        # Initalize pygame framework.
        pygame.init()

        # Initialize window
        size = width, height = 1280, 720 # should be pulled from screen resolution, but this is fine for now
        black = 0, 0, 0
        g.screen = pygame.display.set_mode(size)


        # Initialize Game Board from data directory.
        #boardsDirectory = "./data/game/"
        #boardDataFile = os.listdir(boardsDirectory)[0] # select the first board found for now
        #Can't get this to work: imp.load_source('data.game.defaultboard', boardsDirectory + boardDataFile)
        rootController = self.sceneGraph.initControllers()
        
        # Main game loop.
        while 1:

            g.input_manager.update()

            # Application event handling.
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
    
            # Rendering
            g.screen.fill(black)
            self.sceneGraph.root.draw()
            pygame.display.flip()
    
if __name__ == "__main__":
    App().run()