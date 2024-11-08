import pygame as pg
import sys
from os import path
from settings import *
from sprites import *
from camera import *




class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.load_data()

    def load_data(self):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'Images')
        self.player_img = pg.image.load(path.join(img_folder, PLAYER_IMAGE)).convert_alpha()
        self.player_img = pg.transform.scale(self.player_img, (TILESIZE, TILESIZE))
        self.enemy_img = pg.image.load(path.join(img_folder, ENEMY_IMAGE)).convert_alpha()
        self.enemy_img = pg.transform.scale(self.enemy_img, (TILESIZE, TILESIZE))

    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        level = [
'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
'W0P000000W0000000000000E00000W00000000000W',
'W00000000W0000000000000000000W00000000000W',
'W00000000W0000000000000000000W00000E00000W',
'W00000000W0000000000000000000W00000000000W',
'W00000000W0000000000000E00000W00000000000W',
'W00000000W0000000000000000000000000000000W',
'W000000000000W000000000000000000000000000W',
'W000000000000W00000000000000000000W000000W',
'W000000000000W00000000000000000000W000000W',
'W000000000000W00000000000000000000W000000W',
'W0000000000000W0000000000000000000W000000W',
'W000E000000000W0000000000000000000W000000W',
'W00000000E000W000000000000000000000000000W',
'W000000000000W0000000000000E0000000000000W',
'W00000000000000000WW000000000000000000000W',
'W0000000000000000WW000000000000000W000000W',
'W000000000000000000W0000000000000WW000000W',
'W000000000000000000W0000000000000W0000000W',
'W000000000000000000W0000000000000W0000000W',
'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW']
        height = len(level) *TILESIZE
        width = len(level[0]) *TILESIZE
        for y, row in enumerate(level):
            for x,col in enumerate(row):
                if col == "W":
                    Wall(self,x,y)
                elif col == "E":
                    Enemy(self,x,y)
                elif col == "P":
                    self.player = Player(self,x,y)
        self.camera = Camera(width,height)

    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()
        self.camera.update(self.player)

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image,self.camera.apply(sprite))
        pg.display.flip()

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_LEFT or event.key == pg.K_a:
                    self.player.move(dx=-1)
                if event.key == pg.K_RIGHT or event.key == pg.K_d:
                    self.player.move(dx=1)
                if event.key == pg.K_UP or event.key == pg.K_w:
                    self.player.move(dy=-1)
                if event.key == pg.K_DOWN or event.key == pg.K_s:
                    self.player.move(dy=1)

    def show_start_screen(self):
        pass

g = Game()
while True:
    g.new()
    g.run()