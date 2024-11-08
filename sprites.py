import pygame as pg
from settings import *
import random

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.player_img
        self.original = game.player_img
        self.rect = self.image.get_rect()
        self.vs ,self.vy = 0,0
        self.x = x
        self.y = y
        self.direction = 'right'
        
    '''def get_keys(self):
        self.vx , self.vy = 0,0
        keys = pg.key.get_pressed()
        if keys[pg.K_Left] or keys[pg.K_a]:
            self.vx = -PLAYER_SPEED
        
        elif keys[pg.K_UP] or keys[pg.K_w]:
            self.vy = -PLAYER_SPEED
        
        elif keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.vx = PLAYER_SPEED
            
        elif keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vy = PLAYER_SPEED'''
        
        
    def move(self, dx=0, dy=0):
        if not self.collision(dx,dy):
            self.x += dx
            self.y += dy
            
            if dx > 0:
                self.direction = 'right'
            elif dx < 0:
                self.direction = 'left'
            elif dy > 0:
                self.direction = 'down'
            elif dy < 0:
                self.direction = 'up'        
    
    def collision(self,dx=0,dy=0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        return False

    def update(self):
        if self.direction == 'up':
            self.image = self.original
        elif self.direction == 'down':
            self.image = self.original
        elif self.direction == 'left':
            self.image = pg.transform.flip(self.original,True,False)                
        elif self.direction == 'right':
            self.image = self.original
        
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

class Enemy(pg.sprite.Sprite):
    def __init__(self,game,x,y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        self.image = game.enemy_img
        self.original = game.enemy_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.moving_direction = 'right'
        self.direction = random.randint(0,3)
        self.steps = random.randint(1,3)
        self.move_delay = 1000
        self.last_move = pg.time.get_ticks() 
    
    def update(self):
        self.move()
        if self.moving_direction == 'up':
            self.image = pg.transform.rotate(self.original,90)
        elif self.moving_direction == 'down':
            self.image = pg.transform.rotate(self.original,-90)
        elif self.moving_direction == 'left':
            self.image = pg.transform.rotate(self.original,180)                
        elif self.moving_direction == 'right':
            self.image = self.original        
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE
    
    def collision(self,dx=0,dy=0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        return False    
        
        
    def move(self):
        directions = ((-1,0),(1,0),(0,-1),(0,1))
        dx , dy = directions[self.direction]
        
        if dx == -1:
            self.moving_direction = "left"
        elif dx == 1:
            self.moving_direction = "right"
        elif dy == -1:
            self.moving_direction = "up"
        elif dy == 1:
            self.moving_direction = "down"                    
        
        now = pg.time.get_ticks()
        
        if now - self.last_move > self.move_delay:
            if not self.collision(dx,dy):
                self.x += dx
                self.y += dy
            
            else:
                self.direction = random.randint(0,3)
                
            self.last_move = now
            
        
            self.steps -= 1
            if self.steps <= 0:
                self.direction = random.randint(0,3)
                self.steps = random.randint(1,2)  

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