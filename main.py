import pygame as pg
from bird import *
from ground import *
from pipes import *
import sys

class Game:
    def __init__(self):
        pg.init()

        self.screen = pg.display.set_mode((width,height))

        self.background_image = BACKGROUND_IMAGE
        self.gameOverImage = GAMEOVER
        self.replayImage = REPLAY

        self.background = pg.transform.scale(self.background_image,(width,height))
        self.gameOverFrame = pg.transform.scale2x(self.gameOverImage)
        self.replayButton = pg.transform.scale2x(self.replayImage)

        pg.display.set_caption("Flappy Bird")
        self.clock = pg.time.Clock()

        self.spawnPipe = pg.USEREVENT
        pg.time.set_timer(self.spawnPipe, 1200)

        self.bird = Bird(self)
        self.ground = Ground(self)
        self.pipes = Pipe(self)

        self.GameRunning = True

    def resetGame(self):
        self.pipes.clearPipes()
        self.bird.resetPosition()
        self.GameRunning = True

    def run(self):
        pos = pg.mouse.get_pos()
        while True:

            for event in pg.event.get():

                keys = pg.key.get_pressed()

                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

                if event.type == self.spawnPipe:
                    self.pipes.addPipe()

                if keys[pg.K_SPACE] and not self.GameRunning:
                    self.resetGame()

            self.screen.blit(self.background,(0,0))

            if self.GameRunning:
                self.bird.update()
                self.ground.update()
                self.pipes.update()
            else:
                self.screen.blit(self.gameOverFrame,(80,100))
                self.screen.blit(self.replayButton,(120,200))

            pg.display.update()
            self.clock.tick(FPS)


game = Game()
game.run()
