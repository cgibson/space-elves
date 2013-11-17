import pygame
import events
from controller import Controller
import global_mod as g


class InputController (Controller):

    def __init__(self):
        self.mouse_buttons = [0,0,0]

    def update(self):

        eventList = []
        buttons = pygame.mouse.get_pressed()

        for i in range(3):
            if self.mouse_buttons[i] != buttons[i]:

                if buttons[i]:
                    eventList.append( events.MouseDown(i) ) #0 for left, 1 for middle, 2 for right
                else:
                    eventList.append( events.MouseReleased(i) )

                self.mouse_buttons[i] = buttons[i]

        for event in eventList:
            g.event_manager.post(event)