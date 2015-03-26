import math
import pygame

class Shell(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen

        self.image = pygame.Surface((10, 10))
        self.image.fill((0xff, 0xff, 0xff))
        self.image.set_colorkey((0xff, 0xff, 0xff))
        pygame.draw.circle(self.image, (0,200,200), (5, 5), 5)
        #self.image = pygame.transform.scale(self.image, (5, 5))
        self.rect = self.image.get_rect()
        self.rect.center = (-100, -100)
        self.x = self.rect.centerx
        self.y = self.rect.centery
        self.dx = 0
        self.dy = 0
        self.speed = 0
        self.dir = 0
        self.reset()

    def fire(self, ship):
        self.dir = ship.dir
        self.dx = ship.dx
        self.dy = ship.dy
        self.x = ship.x
        self.y = ship.y
        self.speed = 15 + ship.speed

    def update(self):
        self.calcVector()
        self.calcPos()
        self.checkBounds()
        self.rect.center = (self.x, self.y)

    def calcVector(self):
        radians = self.dir * math.pi / 180

        self.dx = self.speed * math.cos(radians)
        self.dy = self.speed * math.sin(radians)
        self.dy *= -1

    def calcPos(self):
        self.x += self.dx
        self.y += self.dy

    def checkBounds(self):
        screen = self.screen
        if self.x > screen.get_width():
            self.reset()
        if self.x < 0:
            self.reset()
        if self.y > screen.get_height():
            self.reset()
        if self.y < 0:
            self.reset()

    def reset(self):
        """ move off stage and stop"""
        self.x = -100
        self.y = -100
        self.speed = 0
