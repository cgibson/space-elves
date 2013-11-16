from event.listener import EventListener

class View (EventListener):

    def __init__(self):
        self.children = []
        self.parent = None

    def draw(self):
        pass