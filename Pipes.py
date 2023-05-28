import pygame as pg
import random
from Entities import Entity
from Settings import *

class Pipe(Entity):

    def __init__(self,game):

        self.x = 350
        self.y = 0
        self.pipe_speed = 3
        self.game = game
        self.pipe_width = 45
        self.image1 = PIPE_UP
        self.image2 = PIPE_DOWN

        self.pipesActive = []

        self.pipe_up = pg.transform.scale(self.image1,(self.pipe_width,450))
        self.pipe_down = pg.transform.scale(self.image2, (self.pipe_width, 400))
        self.screen = game.screen
        self.score_sfx = SOUNDS["score"]
        self.spawnPipe = pg.USEREVENT
        pg.time.set_timer(self.spawnPipe, 1200)

    def clearPipes(self):
        return self.pipesActive.clear()
    def checkCollisions(self,pipes):
        for pipe in pipes:
            if self.game.bird.rect.colliderect(pipe):
                self.game.GameRunning = False


    def addPipe(self):
        return self.pipesActive.extend(self.createPipes())

    def createPipes(self):
        self.y = random.randint(-50,100)

        top_pipe = self.pipe_up.get_rect(midbottom=(self.x,self.y + 100))
        bottom_pipe = self.pipe_up.get_rect(midtop=(self.x,self.y + 250))
        return top_pipe, bottom_pipe


    def movement(self,pipes):
        for pipe in pipes:
            pipe.x -= self.pipe_speed

        return pipes

    def draw_pipes(self,pipes):
        for pipe in pipes:
            self.screen.blit(self.pipe_up, pipe)
            self.screen.blit(self.pipe_down, pipe)

    def scoredPiped(self,pipes):

        playerScored = pg.mixer.Sound(self.score_sfx)
        for pipe in pipes:
            if pipe.x < self.game.bird.x:
                pass




    def update(self):
        self.pipesActive = self.movement(self.pipesActive)
        self.draw_pipes(self.pipesActive)
        self.checkCollisions(self.pipesActive)
        self.scoredPiped(self.pipesActive)