import pygame as pg
from Bird import *
from Ground import *
from Pipes import *
import sys


class Game:

    def __init__(self):
        pg.init()

        self.screen = pg.display.set_mode((width,height))

        self.background_image = BACKGROUND_IMAGE
        self.background = pg.transform.scale(self.background_image,(width,height))

        pg.display.set_caption("2D Shooter")
        self.clock = pg.time.Clock()


        self.spawnPipe = pg.USEREVENT
        pg.time.set_timer(self.spawnPipe, 1200)

        self.bird = Bird(self)
        self.ground = Ground(self)
        self.pipes = Pipe(self)


    def run(self):
        while True:

            for event in pg.event.get():

                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

                if event.type == self.spawnPipe:
                    self.SpawnPipe = True


            self.screen.blit(self.background,(0,0))

            self.bird.update()
            self.ground.update()
            self.pipes.update()

            pg.display.update()
            self.clock.tick(FPS)




game = Game()
game.run()