import global_mod as g

class EventListener (object):

    def __init__(self):
        self._listening = False


    def notify(self, event):
        pass

    @property
    def listening(self):
        return self._listening

    @listening.setter
    def listening(self, listening):
        self._listening = listening

        if listening:
            print "setting %s to listen" % str(self)
            g.event_manager.registerListener(self)
        else:
            g.event_manager.unregisterListener(self)