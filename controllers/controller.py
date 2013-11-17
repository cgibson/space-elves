from events.listener import EventListener


class Controller (EventListener):

    _controllers = []

    def __init__(self):
        self.model = None
        self.view = None
        self.listening = True
        print "I am listening"

        Controller._controllers.append(self)

    def update(self):
        pass