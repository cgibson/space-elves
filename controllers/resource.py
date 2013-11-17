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


class FontController(ResourceController):
    pass
    #def __init__(self):
    #    ResourceController.__init__(self, pygame.font.SysF)

    
class ImageController(ResourceController):
    def __init__(self):
        ResourceController.__init__(self, pygame.image.load)