import pygame as pg

from random import randint

win_size = (1000, 800)

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

class Ball(pg.sprite.Sprite):
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
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.y <= 0:
            self.speed_y*= -1
        elif self.rect.y >= 750:
            self.speed_y *= -1

play = True
win = False
game = True

mw = pg.display.set_mode(win_size)
pg.display.set_caption("Пинг-понг")
clock = pg.time.Clock()

background = pg.transform.scale(pg.image.load("background.png"), win_size)

ball = Ball('ball2.png', 400, 300, 70, 70, 0, -3)

rocket1 = Base_sprite('ping_rocket1.png',50,300,50,200)
rocket2 = Base_sprite('ping_rocket2.png',900,300,50,200)

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
    rocket2.draw()
    ball.draw()
    ball.update()

    pg.display.update()
    clock.tick(60)