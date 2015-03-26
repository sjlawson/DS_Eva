import pygame
import math

import pcShip
import Shell
import Planets
import Stars

"""
more of a prototype than a real game engine.
Has potential, though
"""
def main():
    currLocation = 0;
    screen = pygame.display.set_mode((1200, 700))
    pygame.display.set_caption("Star Cutter")

    starField = Stars.Stars(screen)
    starField.update()

    screen.blit(starField.background, (0,0))

    locations = [Planets.Earth(), Planets.Moon(), Planets.Mars(), Planets.Space()]

    ship = pcShip.Cutter(screen)
    shell = Shell.Shell(screen)
    currentPlanet = locations[ship.location]
    planetSprites = pygame.sprite.Group(currentPlanet)
    allSprites = pygame.sprite.Group(ship, shell)

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

        planetSprites.clear(screen, starField.background)
        allSprites.clear(screen, starField.background)

        planetSprites.remove(currentPlanet)

        currentPlanet = locations[ship.location]
        planetSprites.add(currentPlanet)
        planetSprites.update()
        planetSprites.draw(screen)

        allSprites.update()
        allSprites.draw(screen)

        pygame.display.flip()

if __name__ == "__main__":
    main()
