""" Base Event Class, including the EventManager
"""

class Event (object):
    """ Superclass for all events in the game
    """

    def __init__(self):
        self.name = "Generic Event"

    def __str__(self):
        return self.name
