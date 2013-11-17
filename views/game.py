from view import View
import pygame

class GameView (View):

    def __init__(self):
        super(GameView, self).__init__(pygame.Rect(0,0,500,500))