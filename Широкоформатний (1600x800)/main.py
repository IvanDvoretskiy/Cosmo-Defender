import pygame as pg
from cogs.TextInput import InputBox
import cogs.Meteors as Meteors
from cogs.Buttons import button1
from cogs.Bullets import Bullet
import config as cfg
from pygame import mixer


pg.init()

WIDTH = cfg.WINDOW_WIDTH
HEIGHT = cfg.WINDOW_HEIGHT

SCREEN = pg.display.set_mode((WIDTH, HEIGHT))

#Створюємо поля для вводу
speedBox = InputBox(20, 620, 250, 30, max_length= 10, placeholder="Швидкість метеориту")
coordinatesBox = InputBox(20, 660, 250, 30, placeholder="Координати появи")
sizeBox = InputBox(20, 700, 250, 30, max_length= 3, placeholder="Розмір метеориту")
speedBBox = InputBox(20, 780, 250, 30, max_length= 3, placeholder="Швидкість кулі")

inputBoxes = [speedBox, coordinatesBox, sizeBox, speedBBox]

speed, size, coordinates = "","",""

def main():
    global inputBoxes

    # Завантажуєм необхідні нам файли {

    mixer.music.load("./sounds/music.mp3")
    mixer.music.play(-1)


    meteors = []
    buttons = [button1]

    bg = pg.transform.scale(pg.image.load('./images/Space/background.png').convert_alpha(), (WIDTH, HEIGHT))
    bgRect = bg.get_rect()

    earth = pg.image.load('./images/Space/Earth.png')

    hud =  pg.transform.scale(pg.image.load('./images/Space/hud.png').convert_alpha(), (WIDTH, 400))
    hudRect = (0, 500, 0, 0)

    ship = pg.transform.scale(pg.image.load('./images/Space/ship.png').convert_alpha(), (400, 300))
    shipRect = pg.Rect(600, 500, 400, 300)

    # }


    #Інше
    clock = pg.time.Clock()
    run = True

    speed, size, coordinates, speed_b = "","","", ""

    bullets = []

    angle = 0

    translator = {
        "Координати появи": coordinates, 
        "Швидкість метеориту": speed, 
        "Розмір метеориту": size,
        "Швидкість кулі": speed_b
    }
    while run:
        try:
            #Відображаєм елементи на екран
            earthRect = pg.Rect(1400, 20, 100, 100)
            SCREEN.blit(bg, bgRect)
            SCREEN.blit(hud, hudRect)
            SCREEN.blit(earth, earthRect)
            SCREEN.blit(ship, shipRect)

            for event in pg.event.get():

                if event.type == pg.QUIT:
                    run = False
                
                #Записуєм введені в поле показники
                for box in inputBoxes:
                    value, key = box.handle_event(event)
                    if value and key:
                        translator[key] = value
                for button in buttons:
                    button.draw(SCREEN)
                    #Перевіряєм чи нажато
                    if button.is_clicked():
                    # Спавнимо метеорити та кулі {

                        speedMeteor = int(translator["Швидкість метеориту"])
                        xMeteor, yMeteor = map(int, translator["Координати появи"].split())
                        sizeMeteor = translator["Розмір метеориту"]
                        
                        speedBulletY = float(translator["Швидкість кулі"])
                        speedBulletX = 0
                        xBullet, yBullet = shipRect.centerx, shipRect.centery

                        meteor = Meteors.create_enemy(translator["Координати появи"], speedMeteor, sizeMeteor)
                        meteors.append(meteor)

                        dil = 0
                        mnoz = 0

                        if xMeteor <= 100:
                            dil = 4
                            angle = 50
                        elif xMeteor <= 200:
                            dil = 4
                            angle = 40
                        elif xMeteor <= 300:
                            dil = 2
                            angle = 30
                        elif xMeteor <= 400:
                            dil = 1
                            angle = 20
                        elif xMeteor <= 500:
                            mnoz = 1
                            angle = 0
                        elif xMeteor <= 600:
                            mnoz = 2
                            angle = -15
                        elif xMeteor <= 700:
                            mnoz = 3
                            angle = -30
                        elif xMeteor <= 800:
                            mnoz = 4
                            angle = -45
                        else:
                            mnoz = 4
                            angle = -60

                        distanceBMY = yBullet - yMeteor
                        distanceBMX = xBullet - xMeteor

                        ticks = distanceBMY/speedBulletY
                        if xMeteor <= 450:
                            speedBulletX = (distanceBMX/ticks)/speedBulletY
                        else:
                            speedBulletX = (distanceBMX/ticks)*speedBulletY

                        targetX = ticks*speedMeteor
                        targetY = yMeteor

                        
                        ship = pg.transform.rotate(pg.transform.scale(pg.image.load('./images/Space/ship.png').convert_alpha(), (400, 300)), angle)

                        bullet = Bullet(shipRect.centerx, shipRect.centery, targetX, targetY, speedBulletX, speedBulletY, xMeteor)
                        bullets.append(bullet)

                    # }



            for box in inputBoxes:
                box.draw(SCREEN)
            for button in buttons:
                button.draw(SCREEN)

            earthRect = earth.get_rect()
            earthRect.left = WIDTH - 160
            
            #Відображення метеорита
            for meteor in meteors:
                meteor[1] = meteor[1].move(meteor[2])
                SCREEN.blit(meteor[0], meteor[1])

                # Перевірка на зіткнення між ворогом і землею
                if meteor[1].colliderect(earthRect):
                    meteors.remove(meteor) # Видаляємо ворога, який зіткнувся з землею
                    print('BOOM')

            #рухаєм кулі
            for bullet in bullets:
                bullet.move()
                bullet.draw(SCREEN)

            for meteor in meteors:
                # Перевірка зіткнень метеорита зі снарядом
                for bullet in bullets:
                    if bullet.rect.colliderect(meteor[1]):
                        meteors.remove(meteor)
                        bullets.remove(bullet)



            pg.display.flip()
            clock.tick(60)
        except: 
            pass


if __name__ == '__main__':
    main()
    pg.quit()