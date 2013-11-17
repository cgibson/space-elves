import global_mod as g

class EventListener (object):

    def __init__(self):
        self._listening = False


    def notify(self, event):
        pass

    def listening(self):
        return self._listening

    def setListening(self, listening):
        self._listening = listening

        if listening:
            g.event_manager.registerListener(self)
        else:
            g.event_manager.unregisterListener(self)