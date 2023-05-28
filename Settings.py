import pygame as pg

width = 350
height = 500
FPS = 60

SOUNDS = {"score":"SFX/sfx_point.wav","fly":"SFX/sfx_wing.wav","hit":"SFX/sfx_hit.wav"}

BIRD_IMAGE = pg.image.load("Images/bird1.png")
BACKGROUND_IMAGE = pg.image.load("Images/background.png")
GROUND_IMAGE = pg.image.load("Images/ground.png")

GAMEOVER = pg.image.load("Images/gameover.png")
REPLAY = pg.image.load("Images/replay.png")

PIPE_UP = pg.image.load("Images/pipe2.png")
PIPE_DOWN = pg.image.load("Images/pipe.png")