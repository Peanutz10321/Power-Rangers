import pygame as pg
from settings import *
import random

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self._layer = 10
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.player_img
        self.rect = self.image.get_rect()
        self.vx ,self.vy = 0,0
        self.x = x
        self.y = y
        
    def get_keys(self):
        self.vx , self.vy = 0,0
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.vx = -PLAYER_SPEED
        
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.vy = -PLAYER_SPEED
        
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.vx = PLAYER_SPEED
            
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vy = PLAYER_SPEED
        
        if self.vx != 0 and self.vy != 0:
            self.vx *= 0.7071
            self.vy *= 0.7071
        
        
    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy
                
    def collision(self,prompt):
        if prompt == 'x':
            hit = pg.sprite.spritecollide(self,self.game.walls, False)
            if hit:
                if self.vx > 0:
                    self.rect.right = hit[0].rect.left
                if self.vx < 0:
                    self.rect.left = hit[0].rect.right
                self.vx = 0
                self.x = self.rect.x
                
        elif prompt == 'y':
            hit = pg.sprite.spritecollide(self,self.game.walls, False)
            if hit:
                if self.vy > 0:
                    self.rect.bottom = hit[0].rect.top
                if self.vy < 0:
                    self.rect.top = hit[0].rect.bottom
                self.vy = 0
                self.y = self.rect.y        
            

    def update(self):
        self.get_keys()
        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt
        self.rect.x = self.x
        self.collision('x')
        self.rect.y = self.y
        self.collision('y')            

class Wall(pg.sprite.Sprite):
    def __init__ (self,game,x,y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE,TILESIZE))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
    
class Path(pg.sprite.Sprite):
    def __init__ (self,game,x,y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        self.image = game.path_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Grass(pg.sprite.Sprite):
    def __init__ (self,game,x,y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        self.image = game.grass_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        
class Tree(pg.sprite.Sprite):
    def __init__ (self,game,x,y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        self.image = game.tree_img
        self.rect = self.image.get_rect()
        self.rect.width = 2 * TILESIZE
        self.rect.height = 4 *TILESIZE
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE 
        self.rect.y = y * TILESIZE

class Big(pg.sprite.Sprite):
    def __init__ (self,game,x,y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        self.image = game.big_img
        self.rect = self.image.get_rect()
        self.rect.width = 4 * TILESIZE
        self.rect.height = 4 *TILESIZE
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE 
        self.rect.y = y * TILESIZE

class Cloud(pg.sprite.Sprite):
    def __init__ (self,game,x,y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        self.image = game.cloud_img
        self.rect = self.image.get_rect()
        self.rect.width = 4 * TILESIZE
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE 
        self.rect.y = y * TILESIZE

class Pond(pg.sprite.Sprite):
    def __init__ (self,game,x,y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        self.image = game.pond_img
        self.rect = self.image.get_rect()
        self.rect.width = 4 * TILESIZE
        self.rect.height = 2 * TILESIZE
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Door(pg.sprite.Sprite):
    def __init__ (self,game,x,y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE,TILESIZE))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE 
        self.rect.y = y * TILESIZE
        

        