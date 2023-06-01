from pygame import *
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
    def update_left(self): #движение ракетки
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < win_height - 100:
            self.rect.y += self.speed
    def update_right(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y < win_height - 40:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y > win_width - 100:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > win_height:
            self.rect.y = 0
            self.rect.x = 0


#найти фон
#background = transform.scale(image.load('galaxy.jpg'), (700, 500))
background = (200, 255, 255)
window = background.fill()
#создание главного окна
win_height = 500
win_width = 700 
window = display.set_mode((win_width, win_height))

#создание экземпляров классов
racket1 = Racket("racket1.png", 1, 200, 40, 100, 1)
racket2 = Racket("racket2.png", 650, 200, 40, 100, 1)
#ball = Ball()


#отобразить ракетки

#игровой цикл
finish = True
gameover = False
while not gameover:


    #задать движение мяча
    for e in event.get():
        if e.type == QUIT:
            gameover = True
    #управление ракетками
    if finish:
        window.blit(background(0, 0))

    racket2.update_left()
    racket1.update_right()
    
    racket1.reset()
    
    racket2.reset()
    
    #поражение

    display.update()
time.delay(50)
