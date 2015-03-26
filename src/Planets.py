import pygame

from abc import ABCMeta, abstractmethod

class AbstractPlanet(pygame.sprite.Sprite):
    __metaclass__ = ABCMeta
    currentPlanet = 0

    def update(self):
        self.rect.center = (600, 350)

class Space(AbstractPlanet):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.setImage()

    def setImage(self):
        self.image = pygame.Surface((1,1))
        self.rect = pygame.Rect((0,0),(1,1))
        self.rect.center = (600, 350)


class Moon(AbstractPlanet):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.setImage()

    def setImage(self):
        self.image = pygame.image.load("planet-1.png")
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (600, 350)

class Earth(AbstractPlanet):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.setImage()

    def setImage(self):
        self.image = pygame.image.load("planet-0.png")
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (600, 350)

class Mars(AbstractPlanet):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.setImage()

    def setImage(self):
        self.image = pygame.image.load("planet-2.png")
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (600, 350)

