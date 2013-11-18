import pygame
import weakref
import json
from models.card import CardModel
 
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
        self.__getattr__(name)
    
class ImageController(ResourceController):
    def __init__(self):
        super(ImageController, self).__init__(pygame.image.load)
        
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
        card = CardModel(-1)
        card.name = cardData["name"]
        card.power = cardData["power"]
        card.speed = cardData["speed"]
        return card
    
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