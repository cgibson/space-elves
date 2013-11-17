from model import *

class ButtonModel (Model):

    def __init__(self, text="notext"):
        super(ButtonModel, self).__init__()
        self.text = text