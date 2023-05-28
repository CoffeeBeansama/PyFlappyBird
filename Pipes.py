import pygame as pg
import random
from Entities import Entity
from Settings import *

class Pipe(Entity):

    def __init__(self,game):

        self.x = 100
        self.y = random.randint(-350,-200)


        self.pipe_width = 45
        self.image1 = PIPE_UP
        self.image2 = PIPE_DOWN

        self.pipe_up = pg.transform.scale(self.image1,(self.pipe_width,400))
        self.pipe_down = pg.transform.scale(self.image2, (self.pipe_width, 400))
        self.screen = game.screen

    def movement(self):



        self.screen.blit(self.pipe_up,(self.x,self.y))
        self.screen.blit(self.pipe_down, (self.x, self.y + 550))

    def update(self):
        self.movement()