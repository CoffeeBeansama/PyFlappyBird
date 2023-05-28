import pygame as pg
from Entities import Entity
from Settings import *

class Ground(Entity):
    def __init__(self,game):

        self.image = GROUND_IMAGE
        self.rect = self.image.get_rect()
        self.ground = pg.transform.scale(self.image,(width,100))

        self.x = 0
        self.y = 400
        self.movementSpeed = 1

        self.screen = game.screen

    def movement(self):
        self.x -= self.movementSpeed

        self.screen.blit(self.ground, (self.x, self.y))
        self.screen.blit(self.ground, (self.x + width, self.y))

        if self.x <= -width:
            self.x = 0

    def update(self):
        self.movement()








