import pygame as pg
import  sys

class Game:

    def __init__(self):

        pg.init()

        self.width = 200
        self.height = 100
        self.FPS = 60
        self.screen = pg.display.set_mode((self.width,self.height))

        pg.display.set_caption("2D Shooter")
        self.clock = pg.time.Clock()

    def run(self):
        while True:

            for event in pg.event.get():
                    if event.type == pg.QUIT:
                        pg.quit()
                        sys.exit()
            pg.display.update()
            self.clock.tick(60)


game = Game()
game.run()