import pygame
#создание главного класса
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Racket(GameSprite):
    def update(): #движение ракетки
        pass

class Ball(GameSprite):
    def update(): #движение мяча
        pass

        def touch_racket(self): #соприкасание мяча и ракетки
            pass

#найти фон
background = transform.scale(image.load(""), (700, 500))
#создание экземпляров классов
racket1 = Racket()
racket2 = Racket()
ball = Ball()

#создание главного окна
win_height = 500
win_width = 700 
window = display.set_mode((win_width, win_height))

#отобразить ракетки

#игровой цикл
gameover = False
while not gameover:

    #задать движение мяча
    for e in event.get():
        if e.type == QUIT:
            gameover = True
    #управление ракетками

    #поражение

    display.update()
time.delay(50)