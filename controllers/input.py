import pygame
from events.event import *


class InputController (object):

    def __init__(self):
        self.mouse_buttons = [0,0,0]

    def update(self):

        events = []
        buttons = pygame.mouse.get_pressed()

        for i in range(3):
            if self.mouse_buttons[i] != buttons[i]:

                if buttons[i]:
                    events.append( MouseButtonPressedEvent(1) )
                else:
                    events.append( MouseButtonReleasedEvent(1) )

                self.mouse_buttons[i] = buttons[i]