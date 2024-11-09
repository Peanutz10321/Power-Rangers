import pygame as pg
from settings import *
import random
import math

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self._layer = 10
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.player2_img
        self.original = self.image
        self.rect = self.image.get_rect()
        self.vx ,self.vy = 0,0
        self.position = pg.Vector2(x,y)
        self.x = x
        self.y = y
        self.facing_right = True
        
    
        
    def get_keys(self):
        self.vx , self.vy = 0,0
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.vx = -PLAYER_SPEED
            if self.facing_right:
                self.image = pg.transform.flip(self.original,True,False)
                self.facing_right = False

        if keys[pg.K_UP] or keys[pg.K_w]:
            self.vy = -PLAYER_SPEED

        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.vx = PLAYER_SPEED
            if not self.facing_right:
                self.image = pg.transform.flip(self.image,True,False)
                self.facing_right = True           

        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vy = PLAYER_SPEED

        if self.vx != 0 and self.vy != 0:
            self.vx *= 0.7071
            self.vy *= 0.7071    
        
        
    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy
        
        current_position = pg.Vector2(self.rect.x,self.rect.y)
        distance = self.position.distance_to(current_position)
        self.position = current_position
        return distance        
        
                
    def collision(self,prompt):
        if prompt == 'x':
            hit = pg.sprite.spritecollide(self,self.game.obstacles, False)
            if hit:
                if self.vx > 0:
                    self.rect.right = hit[0].rect.left
                if self.vx < 0:
                    self.rect.left = hit[0].rect.right
                self.vx = 0
                self.x = self.rect.x
                
        elif prompt == 'y':
            hit = pg.sprite.spritecollide(self,self.game.obstacles, False)
            if hit:
                if self.vy > 0:
                    self.rect.bottom = hit[0].rect.top
                if self.vy < 0:
                    self.rect.top = hit[0].rect.bottom
                self.vy = 0
                self.y = self.rect.y        
    def update_character(self,score):
        self.score = score
        
        if self.score < 0 :
            self.original = self.game.player4_img
        elif self.score < 50 : 
            self.original = self.game.player3_img
        elif self.score < 150:
            self.original = self.game.player2_img
        elif self.score >= 250:
            self.original = self.game.player_img
        
        self.image = self.original
        if not self.facing_right:
            self.image = pg.transform.flip(self.image,True,False)

    def update(self):
        self.get_keys()
        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt
        self.rect.x = self.x
        self.collision('x')
        self.rect.y = self.y
        self.collision('y')
    
class Player2(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self._layer = 10
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        
        self.right_frames = [game.running1_img, game.running2_img,game.running3_img,game.running4_img,game.running5_img,game.running6_img,game.running7_img,game.running8_img]
        self.left_frames = [pg.transform.flip(frame,True,False) for frame in self.right_frames]
        
        self.current = 0
        self.image = self.right_frames[self.current]
        
        self.rect = self.image.get_rect()
        self.vx ,self.vy = 0,0
        self.x = x
        self.y = y
        self.facing_right = True
        self.position = pg.Vector2(x,y)
        
        self.last_update = pg.time.get_ticks()
        self.delay = 100
    
    def animation(self):
        time_now = pg.time.get_ticks()
        if time_now - self.last_update > self.delay:
            self.last_update = time_now
            self.current = (self.current + 1) % len(self.right_frames)
        
            if self.facing_right:
                self.image = self.right_frames[self.current]
            
            else:
                self.image = self.left_frames[self.current]
            
    def get_keys(self):
        self.vx , self.vy = 0,0
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.vx = -PLAYER_SPEED
            if self.facing_right:
                self.facing_right = False

        if keys[pg.K_UP] or keys[pg.K_w]:
            self.vy = -PLAYER_SPEED

        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.vx = PLAYER_SPEED
            if not self.facing_right:
                self.facing_right = True           

        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vy = PLAYER_SPEED

        if self.vx != 0 and self.vy != 0:
            self.vx *= 0.7071
            self.vy *= 0.7071
    
    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy
        
        current_position = pg.Vector2(self.rect.x,self.rect.y)
        distance = self.position.distance_to(current_position)
        self.position = current_position
        return round(distance/32)
        
    def collision(self,prompt):
        if prompt == 'x':
            hit = pg.sprite.spritecollide(self,self.game.obstacles, False)
            if hit:
                if self.vx > 0:
                    self.rect.right = hit[0].rect.left
                if self.vx < 0:
                    self.rect.left = hit[0].rect.right
                self.vx = 0
                self.x = self.rect.x
                
        elif prompt == 'y':
            hit = pg.sprite.spritecollide(self,self.game.obstacles, False)
            if hit:
                if self.vy > 0:
                    self.rect.bottom = hit[0].rect.top
                if self.vy < 0:
                    self.rect.top = hit[0].rect.bottom
                self.vy = 0
                self.y = self.rect.y    
            
    def update(self):
        self.get_keys()
        self.animation()
        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt
        self.rect.x = self.x
        self.collision('x')
        self.rect.y = self.y
        self.collision('y')    

class Player3(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self._layer = 10
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        
        self.right_frames = [game.frame1_img, game.frame2_img, game.frame3_img, game.frame4_img]
        self.left_frames = [pg.transform.flip(frame,True,False) for frame in self.right_frames]
        
        self.current = 0
        self.image = self.right_frames[self.current]
        
        self.rect = self.image.get_rect()
        self.vx ,self.vy = 0,0
        self.x = x
        self.y = y
        self.facing_right = True
        self.position = pg.Vector2(x,y)
        
        self.last_update = pg.time.get_ticks()
        self.delay = 100
    
    def animation(self):
        time_now = pg.time.get_ticks()
        if time_now - self.last_update > self.delay:
            self.last_update = time_now
            self.current = (self.current + 1) % len(self.right_frames)
        
            if self.facing_right:
                self.image = self.right_frames[self.current]
            
            else:
                self.image = self.left_frames[self.current]
            
    def get_keys(self):
        self.vx , self.vy = 0,0
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.vx = -PLAYER_SPEED
            if self.facing_right:
                self.facing_right = False

        if keys[pg.K_UP] or keys[pg.K_w]:
            self.vy = -PLAYER_SPEED

        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.vx = PLAYER_SPEED
            if not self.facing_right:
                self.facing_right = True           

        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vy = PLAYER_SPEED

        if self.vx != 0 and self.vy != 0:
            self.vx *= 0.7071
            self.vy *= 0.7071
    
    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy
        
        current_position = pg.Vector2(self.rect.x,self.rect.y)
        distance = self.position.distance_to(current_position)
        self.position = current_position
        return round(distance/32)
        
    def collision(self,prompt):
        if prompt == 'x':
            hit = pg.sprite.spritecollide(self,self.game.obstacles, False)
            if hit:
                if self.vx > 0:
                    self.rect.right = hit[0].rect.left
                if self.vx < 0:
                    self.rect.left = hit[0].rect.right
                self.vx = 0
                self.x = self.rect.x
                
        elif prompt == 'y':
            hit = pg.sprite.spritecollide(self,self.game.obstacles, False)
            if hit:
                if self.vy > 0:
                    self.rect.bottom = hit[0].rect.top
                if self.vy < 0:
                    self.rect.top = hit[0].rect.bottom
                self.vy = 0
                self.y = self.rect.y    
            
    def update(self):
        self.get_keys()
        self.animation()
        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt
        self.rect.x = self.x
        self.collision('x')
        self.rect.y = self.y
        self.collision('y')  
    
class Item(pg.sprite.Sprite):
    def __init__(self,game,x,y,points):
        self._layer = 11
        self.groups = game.all_sprites, game.items
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        self.points = points
        if self.points == 10:
            self.image = random.choice(self.game.item_images)
        elif self.points == 25:
            self.image = random.choice(self.game.better_item_images)
        elif self.points < 0:
            self.image = random.choice(self.game.bad_item_images)
        
        self.image = pg.transform.scale(self.image, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y  
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        
        self.creation_time = pg.time.get_ticks()
    
    def update(self):
        if pg.time.get_ticks() - self.creation_time > 3000:
            self.kill()

class Wall(pg.sprite.Sprite):
    def __init__ (self,game,x,y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE,TILESIZE))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        
class Ocean(pg.sprite.Sprite):
    def __init__ (self,game,x,y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        self.image = game.ocean_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        
class Shark(pg.sprite.Sprite):
    def __init__ (self,game,x,y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        self.image = game.shark_img
        self.rect = self.image.get_rect()
        self.rect.width = 2 * TILESIZE
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

class Path2(pg.sprite.Sprite):
    def __init__ (self,game,x,y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        self.image = game.path2_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
    
class Path3(pg.sprite.Sprite):
    def __init__ (self,game,x,y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        self.image = game.path3_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Path4(pg.sprite.Sprite):
    def __init__ (self,game,x,y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        self.image = game.path4_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
    
    
class Sand(pg.sprite.Sprite):
    def __init__ (self,game,x,y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        self.image = game.sand_img
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
        self.rect.height = 3 *TILESIZE
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE 
        self.rect.y = y * TILESIZE

class Tree2(pg.sprite.Sprite):
    def __init__ (self,game,x,y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        self.image = game.tree2_img
        self.rect = self.image.get_rect()
        self.rect.width = 2 * TILESIZE
        self.rect.height = 2 *TILESIZE
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

class House1(pg.sprite.Sprite):
    def __init__ (self,game,x,y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        self.image = game.house1_img
        self.rect = self.image.get_rect()
        self.rect.width = 4 * TILESIZE
        self.rect.height = 4 *TILESIZE
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE 
        self.rect.y = y * TILESIZE
        
class House2(pg.sprite.Sprite):
    def __init__ (self,game,x,y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        self.image = game.house2_img
        self.rect = self.image.get_rect()
        self.rect.width = 6 * TILESIZE
        self.rect.height = 5 *TILESIZE
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE 
        self.rect.y = y * TILESIZE

class House4(pg.sprite.Sprite):
    def __init__ (self,game,x,y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        self.image = game.house4_img
        self.rect = self.image.get_rect()
        self.rect.width = 3 * TILESIZE
        self.rect.height = 3 *TILESIZE
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE 
        self.rect.y = y * TILESIZE
       
class Farm(pg.sprite.Sprite):
    def __init__ (self,game,x,y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        self.image = game.farm_img
        self.rect = self.image.get_rect()
        self.rect.width = 5 * TILESIZE
        self.rect.height = 5 *TILESIZE
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
    
class Rock(pg.sprite.Sprite):
    def __init__ (self,game,x,y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        self.image = game.rock_img
        self.rect = self.image.get_rect()
        self.rect.width = 3 * TILESIZE
        self.rect.height = 2 * TILESIZE
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        
class Squid(pg.sprite.Sprite):
    def __init__ (self,game,x,y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        self.image = game.squid_img
        self.rect = self.image.get_rect()
        self.rect.width = 2 * TILESIZE
        self.rect.height = 3 * TILESIZE
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        
class Sponge(pg.sprite.Sprite):
    def __init__ (self,game,x,y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        self.image = game.sponge_img
        self.rect = self.image.get_rect()
        self.rect.width = 2 * TILESIZE
        self.rect.height = 3 * TILESIZE
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Gym(pg.sprite.Sprite):
    def __init__ (self,game,x,y):
        self.groups = game.all_sprites, game.gyms
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        self.image = game.gym_img
        self.rect = self.image.get_rect()
        self.rect.width = 9 * TILESIZE
        self.rect.height = 4 * TILESIZE
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
        

        