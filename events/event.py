""" Base Event Class, including the EventManager
"""

class Event (object):
    """ Superclass for all events in the game
    """

    def __init__(self, name="Generic Event"):
        self.name = name

    def __str__(self):
        return self.name


class MouseButtonPressedEvent (Event):

    def __init__(self, mouseButton):
        super(MouseButtonPressedEvent, self).__init__("Mouse Button %s Pressed" % mouseButton)
        self.mouseButton = mouseButton

class MouseButtonReleasedEvent (Event):

    def __init__(self, mouseButton):
        super(MouseButtonReleasedEvent, self).__init__("Mouse Button %s Released" % mouseButton)
        self.mouseButton = mouseButton