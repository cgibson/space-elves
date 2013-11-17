import sys, os, imp

import pygame

from events.manager import EventManager
from input.manager import InputManager

from data.game.defaultboard import * #HACK

# Initialization
import global_mod as g

class App (object):
    def run(self):
        
        # Initalize pygame framework.
        pygame.init()

        # Initialize window
        size = width, height = 500, 500 # should be pulled from screen resolution, but this is fine for now
        black = 0, 0, 0
        g.screen = pygame.display.set_mode(size)
        g.event_manager = EventManager()
        g.input_manager = InputManager()

        # Initialize Game Board from data directory.
        #boardsDirectory = "./data/game/"
        #boardDataFile = os.listdir(boardsDirectory)[0] # select the first board found for now
        #Can't get this to work: imp.load_source('data.game.defaultboard', boardsDirectory + boardDataFile)
        sceneGraph = DefaultBoardSceneGraph() #HACk, load as if it's a module. =/
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