import pygame
from random import randrange

MAX_STARS = 500

class Stars:
    def __init__(self, screen):
        self.screen = screen
        self.background = pygame.Surface(screen.get_size())
        self.background.fill((0, 0, 30))

    def update(self):
        stars = []
        for i in range(MAX_STARS):
            star = [randrange(0,self.screen.get_width()), randrange(0,self.screen.get_height()), randrange(100,255)]
            stars.append(star)

        for star in stars:
            self.background.set_at((star[0], star[1]), (star[2],star[2],star[2]))

