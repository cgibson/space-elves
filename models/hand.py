from models.model import Model

class HandModel (Model):
    def __init__(self):
        super(HandModel, self).__init__()
        self.cards = []