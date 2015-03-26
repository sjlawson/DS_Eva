import pygame
import math
import pcShip
import Shell

class Moon(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("moon-1.png")
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (600, 350)
    def update(self):
        self.rect.center = (600, 350)

def main():
    screen = pygame.display.set_mode((1200, 700))
    pygame.display.set_caption("Star Cutter")

    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))

    ship = pcShip.Cutter(screen)
    shell = Shell.Shell(screen)
    moon = Moon()
    allSprites = pygame.sprite.Group(moon, ship, shell)


    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    ship.turnLeft()
                elif event.key == pygame.K_RIGHT:
                    ship.turnRight()
                elif event.key == pygame.K_UP:
                    ship.speedUp()
                elif event.key == pygame.K_DOWN:
                    ship.slowDown()
                elif event.key == pygame.K_SPACE:
                    shell.fire( ship )

        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)


        pygame.display.flip()

if __name__ == "__main__":
    main()
