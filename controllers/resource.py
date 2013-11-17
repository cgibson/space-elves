import pygame
import weakref
 
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
            img = self.cache[name]
        except KeyError, e:
            img = self.loader(self.names[name])
            #img.convert_alpha()
            self.cache[name] = img
        return img


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

    
class ImageController(ResourceController):
    def __init__(self):
        ResourceController.__init__(self, pygame.image.load)