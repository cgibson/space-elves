
from controllers.controller import Controller
from views import *
from models.healthbar import *
from views.healthbar import *
import events

class HealthBarController (Controller):

    def __init__(self, pos, size, maxHealth):
        super(HealthBarController, self).__init__()
        self.model = HealthBarModel(maxHealth)
        self.view = HealthBarView(pos, size, maxHealth)

    def setHealth(self, curHealth, maxHealth=None):
        self.model.curHealth = curHealth
        self.view.curHealth = curHealth

        if maxHealth != None:
            self.model.maxHealth = maxHealth
            self.view.maxHealth = maxHealth

        self.update()
        self.view.update()

    def setEventType(self, eventType):
        self.eventType = eventType

    def setFontType(self, font):
        self.view.fontType = font

    def takeDamage(self, damage):
        if damage >= self.model.curHealth:
            self.model.curHealth = 0
            self.view.curHealth = 0

            # Game over man, Game over!
            g.event_manager.post(events.ShipHullBreached())
        else:
            self.model.curHealth -= damage
            self.view.curHealth -= damage