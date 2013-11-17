
from controllers.controller import Controller
from views import *
from models.button import ButtonModel
from views.button import *
import events

class ButtonController (Controller):

    def __init__(self, pos, size, eventType=events.ButtonPress, text="notext"):
        super(ButtonController, self).__init__()
        self.model = ButtonModel(text)
        self.view = ButtonView(pos, size, text)
        self.eventType = eventType

    def setText(self, text):
        self.model.text = text
        self.view.text = text

        self.update()


    def notify(self, event):

        if (isinstance(event, events.MouseReleased) and
            self.view.inBounds(event.mousePos)):

            event = self.eventType(self.model.text)

            g.event_manager.post(event)