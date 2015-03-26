import math
import pygame

class Cutter(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.loadImages()

        self.image = self.imgList[0]
        self.rect = self.image.get_rect()

        self.x = self.rect.centerx
        self.y = self.rect.centery
        self.dir = 0
        self.speed = 0
        self.dx = 0
        self.dy = 0
        self.currentImage = 0


    def loadImages(self):
        # imgMaster = pygame.image.load("starCutter.png").convert_alpha()
        # imgMaster = imgMaster.convert_alpha()
        # imgMaster = pygame.transform.scale(imgMaster, (100, 200))

        self.imgList = []

        # imageSizes = ((165,212),(160,198),(239,157),(193,161),(167,203),(194,164),(239,157),(156,195))
        # imageOffset = ((0,0),(185,6),(355,21),(603,10),(0,264),(178,264),(379,263),(633,257))

        for i in range(8):
            # tmpImg = pygame.Surface(imageSizes[i]).convert()
            tmpImg = pygame.image.load("starCutter-" + str(i) + ".png").convert_alpha()
            # tmpImg.blit(imgMaster, (0, 0), (imageOffset[i], imageSizes[i]))
            tmpImg = pygame.transform.scale(tmpImg, ((int)(tmpImg.get_width() * .5), (int)(tmpImg.get_height() * .5) ))
            self.imgList.append(tmpImg)

    def update(self):
        oldCenter = self.rect.center
        # self.image = pygame.transform.rotate(self.imageMaster, self.dir)
        self.calcVector()

        self.image = self.imgList[self.currentImage].convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = oldCenter
        self.x += self.dx
        self.y += self.dy
        self.checkBounds()
        self.rect.centerx = self.x
        self.rect.centery = self.y

    def calcVector(self):
        if self.dir == 0:
            self.dx = 1
            self.dy = 0
            self.currentImage = 2
        elif self.dir == 45:
            self.dx = .7
            self.dy = -.7
            self.currentImage = 1
        elif self.dir == 90:
            self.dx = 0
            self.dy = -1
            self.currentImage = 0
        elif self.dir == 135:
            self.dx = -.7
            self.dy = -.7
            self.currentImage = 7
        elif self.dir == 180:
            self.dx = -1
            self.dy = 0
            self.currentImage = 6
        elif self.dir == 225:
            self.dx = -.7
            self.dy = .7
            self.currentImage = 5
        elif self.dir == 270:
            self.dx = 0
            self.dy = 1
            self.currentImage = 4
        elif self.dir == 315:
            self.dx = .7
            self.dy = .7
            self.currentImage = 3
        else:
            print "something went wrong here"

        self.dx *= self.speed
        self.dy *= self.speed

    def turnLeft(self):
        self.dir += 45
        if self.dir == 360:
            self.dir = 0

    def turnRight(self):
        self.dir -= 45
        if self.dir < 0:
            self.dir = 315

    def speedUp(self):
        self.speed += 1
        if self.speed > 8:
            self.speed = 8

    def slowDown(self):
        self.speed -= 1
        if self.speed < -3:
            self.speed = -3


    def checkBounds(self):
        screen = self.screen
        if self.y > screen.get_height():
            self.y = 0
        if self.y < 0:
            self.y = screen.get_height()
        if self.x > screen.get_width():
            self.x = 0
        if self.x < 0:
            self.x = screen.get_width()

