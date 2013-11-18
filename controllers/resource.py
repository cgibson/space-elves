import pygame
import weakref
import json
import random
random.seed()
from models.card import CardPrint
 
class ResourceController(object):
    def __init__(self, loader):
        self.__dict__.update(dict(
            names = {},
            cache = {},#weakref.WeakValueDictionary(),
            loader = loader
        ))
        
    def __setattr__(self, name, value):
        self.names[name] = value
        
    def __getattr__(self, name):
        try:
            dataObj = self.cache[name]
        except KeyError, e:
            dataObj = self.loader(self.names[name])
            self.cache[name] = dataObj
        return dataObj
    
    def __setitem__(self, name, value):
        self.__setattr__(name,value)
    
    def __getitem__(self, name):
        try:
            dataObj = self.cache[name]
        except KeyError, e:
            dataObj = self.loader(name)
            self.cache[name] = dataObj
        return dataObj
    
class ImageController(ResourceController):
    def __init__(self):
        super(ImageController, self).__init__(pygame.image.load)

class FontController(object):

    def __init__(self, font, size, bold=False, italic=False):
        self._font = pygame.font.SysFont(font, size, bold, italic)
        self.antialias = True
        self.color = (0,0,0)
        self.background = None
        self.cache = {}

    def __getitem__(self, text):
        label = self._font.render(text, self.antialias, self.color)
        return label

    def getCached(self, text):
        try:
            label = self.cache[text]
        except KeyError, e:
            label = self[text]
            self.cache[text] = label

        return label

class CardPrintsController(): # Unfortunately this needs to act a bit differentally than a ResourceController for loading
    def __init__(self):
        #super(CardPrintsController, self).__init__()
        self.loadedCardTypes = None
        self.cache = {}

    def loadCardPrints(self, filename):
        with open(filename) as cardPrintsFile:
            cardPrints = ConvertUnicodeJSONToByteStrings(json.loads(cardPrintsFile.read()))
        for cardPrint in cardPrints:
            self.cache[cardPrint["name"]] = cardPrint
        return cardPrints

    def __getitem__(self, name):
        cardData = self.cache[name]
        card = CardPrint()
        card.name = cardData["name"]
        card.power = cardData["power"]
        card.speed = cardData["speed"]
        return card
    
    def randomCard(self):
        return self.cache[random.randint(0,len(self.cache)-1)]
    
class DeckSeriesController(ResourceController):
    def __init__(self):
        super(DeckSeriesController, self).__init__(self.loadDeck)
        
    def loadDeck(self, name):
        with open(name) as deckFile:
            deck = ConvertUnicodeJSONToByteStrings(json.loads(deckFile.read()))
        return deck
    
def ConvertUnicodeJSONToByteStrings(input): #from http://stackoverflow.com/questions/956867/how-to-get-string-objects-instead-of-unicode-ones-from-json-in-python
    if isinstance(input, dict):
        return {ConvertUnicodeJSONToByteStrings(key): ConvertUnicodeJSONToByteStrings(value) for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [ConvertUnicodeJSONToByteStrings(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input