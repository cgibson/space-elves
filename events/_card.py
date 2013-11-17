from _event import Event

class Card (Event):
    pass


class CardGrabbed (Card):

    def __init__(self, card):
        super(CardGrabbed, self).__init__("Card Grabbed")
        self.card = card


class CardMoved (Card):

    def __init__(self, card, lane):
        super(CardMoved, self).__init__("Card Moved")