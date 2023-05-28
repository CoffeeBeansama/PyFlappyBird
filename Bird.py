import pygame as pg
from Entities import Entity
from Settings import *


class Bird(Entity):
    def __init__(self,game):

        self.game = game

        self.gravity = 5
        self.y = 0
        self.flapForce = 15
        self.x = 150

        self.flapSound = SOUNDS["fly"]
        self.image = BIRD_IMAGE
        self.bird = pg.transform.scale(self.image,(32,32))

        self.rect = self.bird.get_rect(center=(width/2,height/2))

        self.screen = game.screen

    def resetPosition(self):

        self.rect.centery = 200
        self.screen.blit(self.bird, (self.x, self.rect.centery))

    def checkBounds(self):
        if self.rect.centery >= 400 or self.rect.centery <= 0:
            self.game.GameRunning = False
            self.resetPosition()

    def movement(self):
        keys = pg.key.get_pressed()

        flysound = pg.mixer.Sound(self.flapSound)
        if keys[pg.K_SPACE]:
            self.rect.centery -= self.flapForce

            #if not pg.mixer.Sound.play(flysound):
                #pg.mixer.Sound.playOnce(flysound)





        if self.game.GameRunning:
            self.rect.centery += self.gravity
            self.screen.blit(self.bird, (self.x, self.rect.centery))










    def update(self):
        self.movement()
        self.checkBounds()







