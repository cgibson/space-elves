
from controllers.controller import Controller
from views import *
from models.button import ButtonModel
from views.button import *

class ButtonController (Controller):

    def __init__(self, pos, size, text="notext"):
        super(ButtonController, self).__init__()
        self.model = ButtonModel(text)
        self.view = ButtonView(pos, size, text)

    def setText(self, text):
        self.model.text = text
        self.view.text = text

        self.update()