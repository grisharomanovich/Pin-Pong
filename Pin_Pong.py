from pygame import *
import sys
from random import randint
from time import time as timer

window = display.set_mode((700, 500), RESIZABLE)
display.set_caption('Pin Pong')
background = transform.scale(image.load('background.jpeg'), (700, 500))
clock = time.Clock()
FPS = 60
lost = 0
score = 0
font.init()
font2 = font.SysFont('Arial', 36)
font1 = font.SysFont('Arial', 80)
Lose = font1.render('You lose!', True, (255, 255, 0))
Victory = font1.render('You win!', True, (255, 255, 0))

class GameSprite(sprite.Sprite):
    def __init__(self, painting, x, y, size_x, size_y, speed):
        super().__init__()
        self.image = transform.scale(image.load(painting), (size_x, size_y))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 420:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 420:
            self.rect.y += self.speed
Player_1 = Player('Racket.webp', 30, 200, 50, 150, 4)
Player_2 = Player('Racket.webp', 520, 200, 50, 150, 4)
ball = GameSprite('ball.png', 200, 200, 100, 100, 4)
game = True
finish = False

while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
       
        
    if not finish:
        window.blit(background, (0, 0))
        Player_1.update_l()
        Player_2.update_r()
        Player_1.reset()
        Player_2.reset()
        ball.reset()
        
        display.update()

    time.delay(FPS)
