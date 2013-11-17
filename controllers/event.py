from controller import Controller

class EventController (Controller):
    """ Responsible for coordinating communication to any listeners
    """

    def __init__(self):
        from weakref import WeakKeyDictionary
        self.listeners = WeakKeyDictionary()

    def registerListener(self, listener):
        self.listeners[listener] = 1

    def unregisterListener(self, listener):
        if listener in self.listeners.keys():
            del self.listeners[listener]

    def post(self, event):
        print "POSTING [%s]" % str(event)
        for listener in self.listeners.keys():
            listener.notify(event)