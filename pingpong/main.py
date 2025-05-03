import pygame as pg

from random import randint

win_size = (900, 700)

pg.init()

class Base_sprite(pg.sprite.Sprite):
    def __init__(self, pic, x, y, w, h, speed_x=0, speed_y=0):
        super().__init__()
        self.picture = pg.transform.scale(
            pg.image.load(pic).convert_alpha(), (w, h)
        )
        self.image = self.picture
        self.rect = self.picture.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y
        
                
    def draw(self):
        mw.blit(self.picture, (self.rect.x, self.rect.y))

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

class Ball(Base_sprite):
    def __init__(self, pic, x, y, w, h, speed_x=0, speed_y=0):
        self.picture = pg.transform.scale(
            pg.image.load(pic).convert_alpha(), (w, h)
        )
        self.image = self.picture
        self.rect = self.picture.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y
        
                
    def draw(self):
        mw.blit(self.picture, (self.rect.x, self.rect.y))

    def update(self):
        global count1
        global count2
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.y <= 0:
            self.speed_y*= -1
        elif self.rect.y >= 650:
            self.speed_y *= -1

        if self.rect.x <= -65:
            self.rect.x = 500
            self.rect.y = 400
            count2 += 1

        if self.rect.x >= win_size[0]:
            self.rect.x = 500
            self.rect.y = 400
            count1 += 1

class Rocket(Base_sprite):
    def __init__(self, pic, x, y, w, h, speed_y=0):
        self.picture = pg.transform.scale(
            pg.image.load(pic).convert_alpha(), (w, h)
        )
        self.image = self.picture
        self.rect = self.picture.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_y = speed_y

    def draw(self):
            mw.blit(self.picture, (self.rect.x, self.rect.y))

    def r_update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_UP] and self.rect.y >= -5:
            self.rect.y -= self.speed_y 
               
        if keys[pg.K_DOWN] and self.rect.y <= win_size[1] - 205:            
            self.rect.y += self.speed_y

    def l_update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w] and self.rect.y >= -5:
            self.rect.y -= self.speed_y 
               
        if keys[pg.K_s] and self.rect.y <= win_size[1] - 205:            
            self.rect.y += self.speed_y

def set_text(text, x, y, color=(255,255,200)):
    mw.blit(
        font1.render(text, True, color),(x,y)
    )

play = True
win = False
game = True
font1 = pg.font.Font(None, 36)
count1 = 0
count2 = 0

mw = pg.display.set_mode(win_size)
pg.display.set_caption("Пинг-понг")
clock = pg.time.Clock()

background = pg.transform.scale(pg.image.load("background.png"), win_size)

ball = Ball('ball2.png', 400, 300, 70, 70, 3, -5)

rocket1 = Rocket('ping_rocket1.png', 50, 300, 50, 200, 3)
rocket2 = Rocket('ping_rocket2.png', 800, 300, 50, 200, 3)

fon = pg.transform.scale(
    pg.image.load("win.png"), win_size)
fon_go = pg.transform.scale(
    pg.image.load("defeat.png"), win_size)

while play:

    for e in pg.event.get():
        if e.type == pg.QUIT or \
                    (e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE):
                play  = False

    if game:
        mw.blit(background, (0, 0))

    rocket1.draw()
    rocket1.l_update()
    rocket2.draw()
    rocket2.r_update()
    ball.draw()
    ball.update()

    if ball.rect.colliderect(rocket1.rect):
        ball.speed_x *= -1
    if ball.rect.colliderect(rocket2.rect):
        ball.speed_x *= -1

    set_text(f"{count1}:{count2}", 400, 20)

    pg.display.update()
    clock.tick(60)