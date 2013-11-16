from event.listener import EventListener


class Controller (EventListener):

    def __init__(self, model=None):
        self.model = model