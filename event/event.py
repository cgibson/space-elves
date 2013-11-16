""" Base Event Class, including the EventManager
"""

class Event (object):
    """ Superclass for all events in the game
    """

    def __init__(self):
        self.name = "Generic Event"

    def __str__(self):
        return self.name


class EventManager (object):
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
        for listener in self.listeners.keys():
            listener.notify(event)