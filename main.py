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
        self.path_img = pg.image.load(path.join(img_folder, PATH_IMAGE)).convert_alpha()
        self.path_img = pg.transform.scale(self.path_img, (TILESIZE, TILESIZE))
        self.grass_img = pg.image.load(path.join(img_folder, GRASS_IMAGE)).convert_alpha()
        self.grass_img = pg.transform.scale(self.grass_img, (TILESIZE, TILESIZE))
        self.tree_img = pg.image.load(path.join(img_folder, TREE_IMAGE)).convert_alpha()
        self.tree_img = pg.transform.scale(self.tree_img, (TILESIZE*2,TILESIZE*3))
        self.pond_img = pg.image.load(path.join(img_folder, POND_IMAGE)).convert_alpha()
        self.pond_img = pg.transform.scale(self.pond_img, (TILESIZE*4,TILESIZE*2))  
        self.cloud_img = pg.image.load(path.join(img_folder, CLOUD_IMAGE)).convert_alpha()
        self.cloud_img = pg.transform.scale(self.cloud_img, (TILESIZE*4,TILESIZE))
        self.big_img = pg.image.load(path.join(img_folder, BIG_IMAGE)).convert_alpha()
        self.big_img = pg.transform.scale(self.big_img, (TILESIZE*4,TILESIZE*4))           
            
    def load_level(self,level):
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.all_sprites = pg.sprite.LayeredUpdates()
        levels = [[
'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
'W  C***           C***       W',
'W                    O***    W',
'W                    ****    W',
'W                            W',
'W                            W',
'W       P          P         W',
'W   T*  P   B***   P         W',
'W   **  P   ****   P         W',
'W   **  P   ****   P         W',
'W       P   ****   P T*  T*  W',
'W  O*** P          P **  **  W',
'W  **** P          P **  **  W',
'WPXPPPPPPPPPPPPPPPPPPPPPPPPP!W',
'W                            W',
'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWW']
            
]
        
        height = len(levels[level]) *TILESIZE
        width = len(levels[level][0]) *TILESIZE
        for y, row in enumerate(levels[level]):
            for x,col in enumerate(row):
                if col == "!":
                    Door(self,x,y)
                           
                if col == "W":
                    Wall(self,x,y)
                
                elif col == "P" or col == "X" or col =="!":
                    Path(self,x,y)
                                
                elif col == " " or col == "W":
                    Grass(self,x,y)
                
                elif col == "T":
                    Tree(self,x,y)
                
                elif col == "O":
                    Pond(self,x,y)
                    
                elif col == "C":
                    Cloud(self,x,y)
                
                elif col == "B":
                    Big(self,x,y)
                    
                if col == "X":
                    self.player = Player(self,x*TILESIZE,y*TILESIZE)                 
                
                
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
        
        door = pg.sprite.spritecollideany(self.player, self.all_sprites)
        if door and isinstance(door,Door):
            self.trigger_transaction()
        
    def draw(self):
        self.screen.fill(BGCOLOR)
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

    def draw_start_menu(self):
        font = pg.font.SysFont('arial', 40)
        titleBoxWidth = 300
        titleBoxHeight = 100
        titleBox = pg.Surface((titleBoxWidth,titleBoxHeight))
        title_box_x = (WIDTH - titleBoxWidth) // 2
        title_box_y = 50
        titleBox.fill((255,168,120))
        
        title = font.render('Power Rangers ', True, (255, 255, 255))
        title_rect = title.get_rect(center=(titleBoxWidth // 2, titleBoxHeight // 2))
        self.screen.blit(titleBox, (title_box_x, title_box_y))
        self.screen.blit(title, (title_box_x + title_rect.x, title_box_y + title_rect.y))
    
        start_button_text = font.render('Start', True , (DARKGREY))
        button_width = 100
        button_height = 50
        button_x = WIDTH / 2 - button_width /2
        button_y = HEIGHT / 2 + 50
        button_rect = pg.Rect(button_x,button_y,button_width,button_height)
        pg.draw.rect(self.screen, (WHITE),button_rect)
        self.screen.blit(start_button_text, (button_x + (button_width - start_button_text.get_width()) / 2 ,button_y + (button_height - start_button_text.get_height()) / 2))
        pg.display.flip()

        waiting = True
        
        while waiting:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.quit()
                    quit()
                elif event.type == pg.MOUSEBUTTONDOWN:
                    mouse_x,mouse_y = pg.mouse.get_pos()
                    
                    if button_rect.collidepoint(mouse_x,mouse_y):
                        waiting = False
    
    def trigger_transaction(self):
        self.show_transaction_screen()
    
    def show_transaction_screen(self):
        font = pg.font.SysFont('arial', 40)
        text = font.render('Level Completed!', True,(255,255,255))
        self.screen.fill((0,0,0))
        self.screen.blit(text,(WIDTH//2 - text.get_width() // 2 ,HEIGHT // 2))
        pg.display.flip()
        
        pg.time.delay(500)
        
        self.load_level(1)
        self.run()

g = Game()
g.draw_start_menu()
while True:
    g.load_level(0)
    g.run()