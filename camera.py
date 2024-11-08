import pygame as pg
from settings import *

class Camera:
    def __init__(self,width,height):
        self.camera = pg.Rect(0,0,width,height)
        self.width = width
        self.height = height
        
    def apply(self,entity):
        return entity.rect.move(self.camera.topleft)
    
    def update(self,target):
        x = -target.rect.x + int(WIDTH/2)
        y = -target.rect.y + int(HEIGHT/2)
        
        x = max(-(self.width - WIDTH),min(0,x))
        y = max(-(self.height - HEIGHT),min(0,y))
        self.camera = pg.Rect(x,y,self.width,self.height)
        