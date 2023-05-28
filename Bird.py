import pygame as pg
from Entities import Entity
from Settings import *


class Bird(Entity):
    def __init__(self,game):

        self.gravity = 5
        self.y = 0
        self.flapForce = 20
        self.x = 150

        self.Flap_Wings = game.Pressing_Space
        self.image = BIRD_IMAGE
        self.bird = pg.transform.scale(self.image,(32,32))

        self.screen = game.screen

    def movement(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_SPACE]:
            self.y -= self.flapForce

        self.y += self.gravity

        self.screen.blit(self.bird, (self.x, self.y))








    def update(self):

        self.movement()







