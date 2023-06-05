from pygame import *
#основной класс
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

class Player(GameSprite):
    def update_l(self): #движение ракетки
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height-80:
            self.rect.y += self.speed
#фон
back = (200, 255, 255)
win_width= 600
win_height= 500
window = display.set_mode((win_width, win_height))
window.fill(back)
#игровые функции
game = True
finish = False
clock = time.Clock()
FPS = 60
#экземпляры класса
racket1 = Player('racket2.png', 30, 200, 50, 150, 4)
racket2 = Player('racket1.png', 520, 200, 50, 150, 4)
ball = GameSprite('ball.png', 200, 200, 50, 50, 4)
#текст (поражение 1 и 2)
font.init()
font=font.SysFont(None, 35)
lose1=font.render('Player 1 lose', True,(100, 0, 0))
lose2=font.render('Player 2 lose', True,(100, 0, 0))
#переменные скорости
speed_x = 3
speed_y = 3

#игровой цикл
while game:
    #закрытие через крест
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill(back)
        racket1.update_r()
        racket2.update_l()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        #отталкивание мяча
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= -1
        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1,(200,200))
            finish = True
        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2,(200,200))
            finish = True

    racket1.reset()
    racket2.reset()
    ball.reset()
    display.update()
    clock.tick(FPS)
