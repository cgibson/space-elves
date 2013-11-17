import pygame
from events.event import *
from controller import Controller
import global_mod as g


class InputController (Controller):

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

        for event in events:
            g.event_manager.post(event)