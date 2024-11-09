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
        self.items = pg.sprite.Group()
        self.score = 0
        self.steps = 0
        self.show_pop_up = False
        self.timer = 5000
        self.strength = 0
        self.pressed_count = 0
        self.time = 0
        self.spawn_timer = 0
        self.current_level = 0
        self.gym_triggered = False
        self.in_gym = False
        self.start_time = None
        self.font = pg.font.SysFont('arial', 40)
        self.cool_font = pg.font.Font('font/PublicPixel.ttf',20)

    def load_data(self):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'Images')
        item_img_folder = path.join(img_folder, 'Items')  
        
        self.text_box_img = pg.image.load(path.join(img_folder, BOX_IMAGE)).convert_alpha()
        
        self.end_box_img = pg.image.load(path.join(img_folder,END_BOX_IMAGE)).convert_alpha()
        
        self.cover_img = pg.image.load(path.join(img_folder, COVER_IMAGE)).convert_alpha()
        self.cover_img = pg.transform.scale(self.cover_img, (WIDTH, HEIGHT))
        
        self.running1_img = pg.image.load(path.join(img_folder, RUNNING1_IMAGE)).convert_alpha()
        self.running1_img = pg.transform.scale(self.running1_img,(TILESIZE,TILESIZE))
        
        self.running2_img = pg.image.load(path.join(img_folder, RUNNING2_IMAGE)).convert_alpha()
        self.running2_img = pg.transform.scale(self.running2_img,(TILESIZE,TILESIZE))
        
        self.running3_img = pg.image.load(path.join(img_folder, RUNNING3_IMAGE)).convert_alpha()
        self.running3_img = pg.transform.scale(self.running3_img,(TILESIZE,TILESIZE))
        
        self.running4_img = pg.image.load(path.join(img_folder, RUNNING4_IMAGE)).convert_alpha()
        self.running4_img = pg.transform.scale(self.running4_img,(TILESIZE,TILESIZE))
        
        self.running5_img = pg.image.load(path.join(img_folder, RUNNING5_IMAGE)).convert_alpha()
        self.running5_img = pg.transform.scale(self.running5_img,(TILESIZE,TILESIZE))
        
        self.running6_img = pg.image.load(path.join(img_folder, RUNNING6_IMAGE)).convert_alpha()
        self.running6_img = pg.transform.scale(self.running6_img,(TILESIZE,TILESIZE))
        
        self.running7_img = pg.image.load(path.join(img_folder, RUNNING7_IMAGE)).convert_alpha()
        self.running7_img = pg.transform.scale(self.running7_img,(TILESIZE,TILESIZE))
        
        self.running8_img = pg.image.load(path.join(img_folder, RUNNING8_IMAGE)).convert_alpha()
        self.running8_img = pg.transform.scale(self.running8_img,(TILESIZE,TILESIZE))        
        
        self.player4_img = pg.image.load(path.join(img_folder, PLAYER4_IMAGE)).convert_alpha()
        self.player4_img = pg.transform.scale(self.player4_img, (TILESIZE, TILESIZE))
        
        self.player3_img = pg.image.load(path.join(img_folder, PLAYER3_IMAGE)).convert_alpha()
        self.player3_img = pg.transform.scale(self.player3_img, (TILESIZE, TILESIZE))
        
        self.player2_img = pg.image.load(path.join(img_folder, PLAYER2_IMAGE)).convert_alpha()
        self.player2_img = pg.transform.scale(self.player2_img, (TILESIZE, TILESIZE))
        
        self.player_img = pg.image.load(path.join(img_folder, PLAYER_IMAGE)).convert_alpha()
        self.player_img = pg.transform.scale(self.player_img, (TILESIZE, TILESIZE))
        
        self.frame1_img = pg.image.load(path.join(img_folder, FRAME1_IMAGE)).convert_alpha()
        self.frame1_img = pg.transform.scale(self.frame1_img,(TILESIZE,TILESIZE))
        
        self.frame2_img = pg.image.load(path.join(img_folder, FRAME2_IMAGE)).convert_alpha()
        self.frame2_img = pg.transform.scale(self.frame2_img,(TILESIZE,TILESIZE))
        
        self.frame3_img = pg.image.load(path.join(img_folder, FRAME3_IMAGE)).convert_alpha()
        self.frame3_img = pg.transform.scale(self.frame3_img,(TILESIZE,TILESIZE))
        
        self.frame4_img = pg.image.load(path.join(img_folder, FRAME4_IMAGE)).convert_alpha()
        self.frame4_img = pg.transform.scale(self.frame4_img,(TILESIZE,TILESIZE))        
        
        self.ocean_img = pg.image.load(path.join(img_folder, OCEAN_IMAGE)).convert_alpha()
        self.ocean_img = pg.transform.scale(self.ocean_img, (TILESIZE, TILESIZE))
        
        self.shark_img = pg.image.load(path.join(img_folder, SHARK_IMAGE)).convert_alpha()
        self.shark_img = pg.transform.scale(self.shark_img, (2*TILESIZE, TILESIZE))        
        
        self.path_img = pg.image.load(path.join(img_folder, PATH_IMAGE)).convert_alpha()
        self.path_img = pg.transform.scale(self.path_img, (TILESIZE, TILESIZE))
        
        self.path2_img = pg.image.load(path.join(img_folder, PATH2_IMAGE)).convert_alpha()
        self.path2_img = pg.transform.scale(self.path2_img, (TILESIZE, TILESIZE))
        
        self.path3_img = pg.image.load(path.join(img_folder, PATH3_IMAGE)).convert_alpha()
        self.path3_img = pg.transform.scale(self.path3_img, (TILESIZE, TILESIZE))
        
        self.path4_img = pg.image.load(path.join(img_folder, PATH4_IMAGE)).convert_alpha()
        self.path4_img = pg.transform.scale(self.path4_img, (TILESIZE, TILESIZE))
        
        self.sand_img = pg.image.load(path.join(img_folder, SAND_IMAGE)).convert_alpha()
        self.sand_img = pg.transform.scale(self.sand_img, (TILESIZE, TILESIZE))        
        
        self.grass_img = pg.image.load(path.join(img_folder, GRASS_IMAGE)).convert_alpha()
        self.grass_img = pg.transform.scale(self.grass_img, (TILESIZE, TILESIZE))
        
        self.tree_img = pg.image.load(path.join(img_folder, TREE_IMAGE)).convert_alpha()
        self.tree_img = pg.transform.scale(self.tree_img, (TILESIZE*2,TILESIZE*3))
        
        self.tree2_img = pg.image.load(path.join(img_folder, TREE2_IMAGE)).convert_alpha()
        self.tree2_img = pg.transform.scale(self.tree2_img, (TILESIZE*2,TILESIZE*2))        
        
        self.pond_img = pg.image.load(path.join(img_folder, POND_IMAGE)).convert_alpha()
        self.pond_img = pg.transform.scale(self.pond_img, (TILESIZE*4,TILESIZE*3))         
        
        self.cloud_img = pg.image.load(path.join(img_folder, CLOUD_IMAGE)).convert_alpha()
        self.cloud_img = pg.transform.scale(self.cloud_img, (TILESIZE*4,TILESIZE))
        
        self.big_img = pg.image.load(path.join(img_folder, BIG_IMAGE)).convert_alpha()
        self.big_img = pg.transform.scale(self.big_img, (TILESIZE*4,TILESIZE*4))
        
        self.house1_img = pg.image.load(path.join(img_folder, HOUSE1_IMAGE)).convert_alpha()
        self.house1_img = pg.transform.scale(self.house1_img, (TILESIZE*4,TILESIZE*4))
        
        self.house2_img = pg.image.load(path.join(img_folder, HOUSE2_IMAGE)).convert_alpha()
        self.house2_img = pg.transform.scale(self.house2_img, (TILESIZE*6,TILESIZE*5))
        
        self.house4_img = pg.image.load(path.join(img_folder, HOUSE4_IMAGE)).convert_alpha()
        self.house4_img = pg.transform.scale(self.house4_img, (TILESIZE*3,TILESIZE*3))         
    
        self.farm_img = pg.image.load(path.join(img_folder, FARM_IMAGE)).convert_alpha()
        self.farm_img = pg.transform.scale(self.farm_img, (TILESIZE*5,TILESIZE*5))
        
        self.rock_img = pg.image.load(path.join(img_folder, ROCK_IMAGE)).convert_alpha()
        self.rock_img = pg.transform.scale(self.rock_img, (TILESIZE*3,TILESIZE*2))
        
        self.squid_img = pg.image.load(path.join(img_folder, SQUID_IMAGE)).convert_alpha()
        self.squid_img = pg.transform.scale(self.squid_img, (TILESIZE*2,TILESIZE*3)) 
        
        self.sponge_img = pg.image.load(path.join(img_folder, SPONGE_IMAGE)).convert_alpha()
        self.sponge_img = pg.transform.scale(self.sponge_img, (TILESIZE*2,TILESIZE*3))
        
        self.gym_img = pg.image.load(path.join(img_folder, GYM_IMAGE)).convert_alpha()
        self.gym_img = pg.transform.scale(self.gym_img, (TILESIZE*9,TILESIZE*4))        
        
        self.item_images = [pg.image.load(path.join(item_img_folder,f'Normal_Item{i}.png')).convert_alpha()
                            for i in range(6)]
        self.better_item_images = [pg.image.load(path.join(item_img_folder,f'Better_Item{i}.png')).convert_alpha()
                                   for i in range(3)]
        self.bad_item_images = [pg.image.load(path.join(item_img_folder,f'Bad_Item{i}.png')).convert_alpha()
                                   for i in range(5)]        
    def load_level(self,level):
        self.all_sprites = pg.sprite.Group()
        self.all_sprites = pg.sprite.LayeredUpdates()
        self.obstacles = pg.sprite.Group()
        self.gyms = pg.sprite.Group()
        
        
        levels = [[
'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
'W  C***           C***       W',
'W                    O***    W',
'W                    ****    W',
'W                    ****    W',
'W                            W',
'W                            W',
'W   T*   P  B***  P          W',
'W   **   P  ****  P          W',
'W   **   P  ****  P          W',
'W        P  ****  P  T*  T*  W',
'W  O***  P        P  **  **  W',
'W  ****  P        P  **  **  W',
'W  ****  P        P          W',
'WPXPPPPPPPPPPPPPPPPPPPPPPPPP!W',
'W                            W',
'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWW'],

[
'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
'W      F****    G********   NEEEW',
'W1***  *****    *********   NEEEW',
'W****  *****    *********   NEEEW',
'W****  *****    *********   NEEEW',
'W****  *****       AA       NEEEW',
'WAAAAAAAAAAAAAAAAAAAAAAAA   NEEEW',
'W2*****AAAAAAAAAAAAAAAAAA   NEEEW',
'W******AA          AA       NEEEW',
'W******AA           AA      NEEEW',
'W******AA   O***     AA     NEEEW',
'W******AA   *D**      AA    NEEEW',
'W      AA   ****       AA   NEEEW',
'W      AA               AA  NEEEW',
'WAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA!W',
'WALAAAAAAAAAAAAAAAAAAAAAAAAAAAA!W',
'W                               W',
'W                               W',
'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',],
[
'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
'WSSS4**SSSSSSSSSSSSSSSSSSSSSSSSSW',
'WSSS***SSSSSSSSSSSSSSSSSSSSSSSSSW',
'WSSS***SSSSSSS;*SSSSS;*SSSSS;*SSW',
'WSSSS.SSSSSSSS**SSSSS**SSSSS**SSW',
'W..,...........................!W',
'WSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSW',
'WSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSW',
'WSSSSSSSSSSSSSSSSSSSSSQ*SSS9*SSSW',
'WSSSSSSSSSSSSSSSR**SSS**SSS**SSSW',
'WSS;*SSSSSSSSSSS***SSS**SSS**SSSW',
'WSS**SSSSSSSSSSSSSSSSSSSSSSSSSSSW',
'WSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSW',
'WEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEW',
'WEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEW',
'WEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEW',
'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW'],

]
        
        height = len(levels[level]) *TILESIZE
        width = len(levels[level][0]) *TILESIZE
        for y, row in enumerate(levels[level]):
            for x,col in enumerate(row):
                if col == "!":
                    Door(self,x,y)
                           
                if col == "W":
                    wall = Wall(self,x,y)
                    self.obstacles.add(wall)
                                
                elif col == " " or col == "W":
                    Grass(self,x,y)
                
                elif col == "T":
                    tree = Tree(self,x,y)
                    self.obstacles.add(tree)
                
                elif col == ";":
                    tree2 = Tree2(self,x,y)
                    self.obstacles.add(tree2)
                
                elif col == "O":
                    pond = Pond(self,x,y)
                    self.obstacles.add(pond)
                    
                elif col == "C":
                    Cloud(self,x,y)
                
                elif col == "B":
                    big = Big(self,x,y)
                    self.obstacles.add(big)
                    
                elif col == "1":
                    house1 = House1(self,x,y)
                    self.obstacles.add(house1)
                
                elif col == "2":
                    house2 = House2(self,x,y)
                    self.obstacles.add(house2)
                
                elif col == "4":
                    house4 = House4(self,x,y)
                    self.obstacles.add(house4)
                
                elif col == "F":
                    farm = Farm(self,x,y)
                    self.obstacles.add(farm)
                    
                elif col == "P" or col == "X" or col =="!":
                    Path(self,x,y)                
                
                elif col == "A" or col == "L":
                    Path2(self,x,y)
                
                elif col == "N":
                    Path3(self,x,y)
                
                elif col == "." or col == ",":
                    Path4(self,x,y)
                
                elif col == "E":
                    ocean = Ocean(self,x,y)
                    self.obstacles.add(ocean)
                
                elif col == "S":
                    Sand(self,x,y)
                
                elif col == "R":
                    rock = Rock(self,x,y)
                    self.obstacles.add(rock)
                
                elif col == "Q":
                    squid = Squid(self,x,y)
                    self.obstacles.add(squid)
                
                elif col == "9":
                    sponge = Sponge(self,x,y)
                    self.obstacles.add(sponge)
                
                elif col == "D":
                    Shark(self,x,y)
                
                elif col == "G":
                    gym = Gym(self,x,y)
                    self.gyms.add(gym)
                    
                
                    
                if col == "X":
                    self.player = Player(self,x*TILESIZE,y*TILESIZE)
                
                elif col == "L":
                    self.player = Player3(self,x*TILESIZE,y*TILESIZE)
                    
                elif col == ",":
                    self.player = Player2(self,x*TILESIZE,y*TILESIZE)
        self.camera = Camera(width,height)        
        if level == 0:
            self.display_text("Level 1 : Eat Healthy Food")
        
        elif level == 1:
            self.display_text("Level 2 : Working Out")
            
        elif level == 2:
            self.steps = 0
            self.display_text("Level 3 : Cardio")
        
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
       
        self.all_sprites.update()
        self.camera.update(self.player)
        if (self.current_level == 0):
            self.spawn_timer += self.dt
            if self.spawn_timer >= 5:
                self.spawn_items()
                self.spawn_timer = 0
        
            collected = pg.sprite.spritecollide(self.player,self.items,True)
            for items in collected:
                self.score += items.points
                self.player.update_character(self.score)
        
        if (self.current_level == 1):
            if self.pressed_count >= 20 :
                self.strength += 1
                self.pressed_count -= 20
                
        gym = pg.sprite.spritecollideany(self.player,self.gyms)
        if gym and isinstance(gym,Gym):
            self.in_gym = True
        else:
            self.in_gym = False
        
        door = pg.sprite.spritecollideany(self.player, self.all_sprites)
        if door and isinstance(door,Door):
            self.trigger_transaction()
        
        
    def draw(self):
                
        self.screen.fill(BGCOLOR)      
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image,self.camera.apply(sprite))
        if (self.current_level == 0):
            text = self.font.render(f"Score : {self.score}/250",True,(BLACK))
            textBoxRect = text.get_rect(topleft = (1,1))
            text_box_img = pg.transform.scale(self.text_box_img, (textBoxRect.width + 90,textBoxRect.height + 70))
            
            self.screen.blit(text_box_img,(textBoxRect.x,textBoxRect.y))
            self.screen.blit(text,(50,30))      
        
        if (self.current_level == 1):
            text = self.font.render(f"Strength : {self.strength}/10",True,(BLACK))
            textBoxRect = text.get_rect(topleft = (1,1))
            text_box_img = pg.transform.scale(self.text_box_img, (textBoxRect.width + 90,textBoxRect.height + 70))
            self.screen.blit(text_box_img,(textBoxRect.x,textBoxRect.y))
            self.screen.blit(text,(50,30))            
            text = self.font.render(f"Space Pressed: {self.pressed_count}/20",True,(BLACK))
            textBoxRect = text.get_rect(topleft = (300,1))
            text_box_img = pg.transform.scale(self.text_box_img, (textBoxRect.width + 130,textBoxRect.height + 70))            
            self.screen.blit(text_box_img,(textBoxRect.x,textBoxRect.y))
            self.screen.blit(text,(370,30))           
                        
        
        if(self.current_level == 2):
            text = self.font.render(f"Steps : {self.steps}/500",True,(BLACK))
            textBoxRect = text.get_rect(topleft = (1,1))
            text_box_img = pg.transform.scale(self.text_box_img, (textBoxRect.width + 90,textBoxRect.height + 70))
            
            self.screen.blit(text_box_img,(textBoxRect.x,textBoxRect.y))            
            self.screen.blit(text,(50,30))
        
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
                    self.steps += self.player.move(dx=-1)
                if event.key == pg.K_RIGHT or event.key == pg.K_d:
                    self.steps += self.player.move(dx=1)
                if event.key == pg.K_UP or event.key == pg.K_w:
                    self.steps += self.player.move(dy=-1)
                if event.key == pg.K_DOWN or event.key == pg.K_s:
                    self.steps += self.player.move(dy=1)
                if event.key == pg.K_SPACE and self.in_gym:
                    self.pressed_count += 1

    def draw_start_menu(self):
        
        self.screen.blit(self.cover_img,(0,0))
        start_button_text = self.cool_font.render('Start', True , (WHITE))
        button_width = 100
        button_height = 50
        button_x = WIDTH / 2 - button_width /2
        button_y = HEIGHT / 2 + 50
        button_rect = pg.Rect(button_x,button_y,button_width,button_height)
        pg.draw.rect(self.screen, (GREEN),button_rect)
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
    def draw_end_menu(self):
        text = self.cool_font.render('Thank you for Playing', True,(WHITE))
        text_rect = text.get_rect(center=(WIDTH//2,HEIGHT//2))
        text_box_img = pg.transform.scale(self.end_box_img,(text_rect.width+40,text_rect.height+200))
        text_box_rect = text_box_img.get_rect(center=(WIDTH//2,HEIGHT//2))
        self.screen.fill(BLACK)
        self.screen.blit(text_box_img,text_box_rect.topleft)
        self.screen.blit(text,text_rect.topleft)
        pg.display.flip()
        pg.time.delay(3000)
        self.quit()
    def trigger_transaction(self):
        if(self.current_level == 0):
            if(self.score >= 250):
                self.show_transaction_screen()
                self.draw()
            else:
                return
        
        elif(self.current_level == 1):
            if(self.strength >= 10):
                self.show_transaction_screen()
                self.draw()
            else:
                return
        
        elif(self.current_level == 2):
            if(self.steps >= 500):
                self.show_transaction_screen()
                self.draw()
            else:
                return
        self.show_transaction_screen()
        
    
    def show_transaction_screen(self):
        text = self.font.render('Level Completed!', True,(255,255,255))
        self.screen.fill((0,0,0))
        self.screen.blit(text,(WIDTH//2 - text.get_width() // 2 ,HEIGHT // 2))
        pg.display.flip()
        self.current_level += 1
        if self.current_level == 3:
            self.draw_end_menu()
            pg.time.delay(2000)
        pg.time.delay(500)
        
        self.load_level(self.current_level)
        self.run()
        
    def display_text(self,message):
        
        text = self.cool_font.render(message,True,(BLACK))
        text_rect = text.get_rect(center = (WIDTH//2,HEIGHT//2))
        
        alpha = 255
        text.set_alpha(alpha)
        
        frames_fading = 60 * 3
        
        for frame in range(frames_fading):
            alpha = max(0, 255-(255 * frame // frames_fading))
            text.set_alpha(alpha)
            self.draw()
            self.screen.blit(text,text_rect)
            
            pg.display.flip()
            pg.time.Clock().tick(60)
    
    
    def spawn_items(self):
        if self.current_level != 0:
            return
        
        for i in range(3):
            while True:
                x = random.randint(2,WIDTH//TILESIZE - 3) 
                y = random.randint(2,HEIGHT//TILESIZE - 3)
                item = Item(self,x,y,10)
                self.items.remove(item)
                if pg.sprite.spritecollideany(item,self.obstacles) or pg.sprite.spritecollideany(item,self.items):
                    item.kill()
                    continue
                self.items.add(item)
                break
        while True:
            x = random.randint(2,WIDTH//TILESIZE - 3) 
            y = random.randint(2,HEIGHT//TILESIZE - 3) 
            item = Item(self,x,y,25)
            self.items.remove(item)
            if pg.sprite.spritecollideany(item,self.obstacles) or pg.sprite.spritecollideany(item,self.items):
                item.kill()
                continue
            self.items.add(item)
            break
        while True:
            x = random.randint(2,WIDTH//TILESIZE - 3) 
            y = random.randint(2,HEIGHT//TILESIZE - 3) 
            item = Item(self,x,y,random.choice([-10,-15,-20]))
            self.items.remove(item)
            if pg.sprite.spritecollideany(item,self.obstacles) or pg.sprite.spritecollideany(item,self.items):
                item.kill()
                continue
            self.items.add(item)
            break
    
            
                
g = Game()
g.draw_start_menu()
while True:
    g.load_level(0)
    g.run()