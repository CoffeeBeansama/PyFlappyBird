import pygame as pg
import random
from Entities import Entity
from Settings import *

class Pipe(Entity):

    def __init__(self,game):

        self.x = 350
        self.y = random.randint(-350,-200)
        self.pipe_speed = 3
        self.game = game
        self.pipe_width = 45
        self.image1 = PIPE_UP
        self.image2 = PIPE_DOWN

        self.pipesActive = []

        self.pipe_up = pg.transform.scale(self.image1,(self.pipe_width,400))
        self.pipe_down = pg.transform.scale(self.image2, (self.pipe_width, 400))
        self.screen = game.screen



    def createPipes(self):
        pass



    def movement(self):

        self.x -= self.pipe_speed

        if self.game.spawnPipe:
            print("Haha")




        #if self.x <= -100:
            #self.x = 350

    def update(self):
        self.movement()