from event.listener import EventListener


class Controller (EventListener):

    def __init__(self):
        self.model = None
        self.view = None