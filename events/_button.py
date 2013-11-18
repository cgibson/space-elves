from _event import *

class ButtonPress (Event):

    def __init__(self, label):
        super(ButtonPress, self).__init__("Pressed '%s'" % label)

class ButtonEndTurn (ButtonPress):
    pass

