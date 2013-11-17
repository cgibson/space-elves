import sys, os, imp

import pygame

from controllers.event import *
from controllers.input import *

from data.game.defaultboard import * #HACK

# Initialization
import global_mod as g

class App (object):
    def run(self, sceneGraph=DefaultBoardSceneGraph()):
        
        # Initalize pygame framework.
        pygame.init()

        # Initialize window
        size = width, height = 500, 500 # should be pulled from screen resolution, but this is fine for now
        black = 0, 0, 0
        g.screen = pygame.display.set_mode(size)
        g.event_manager = EventController()
        g.input_manager = InputController()

        # Initialize Game Board from data directory.
        #boardsDirectory = "./data/game/"
        #boardDataFile = os.listdir(boardsDirectory)[0] # select the first board found for now
        #Can't get this to work: imp.load_source('data.game.defaultboard', boardsDirectory + boardDataFile)
        rootController = sceneGraph.initControllers()
        
        # Main game loop.
        while 1:

            g.input_manager.update()

            # Application event handling.
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
    
            # Rendering
            g.screen.fill(black)
            sceneGraph.root.draw()
            pygame.display.flip()
    
if __name__ == "__main__":
    App().run()