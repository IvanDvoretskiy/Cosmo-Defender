import math
import pygame as pg


class Bullet:
    def __init__(self, startX, startY, targetX, targetY, speedBulletX, speedBulletY, xMeteor):
        self.targetX, self.targetY = targetX, targetY
        self.speedBulletX, self.speedBulletY = speedBulletX, speedBulletY
        self.bullet = pg.transform.scale(pg.image.load('./images/Space/bullet.png').convert_alpha(), (25, 50))
        self.rect = self.bullet.get_rect()
        self.rect.center = (startX, startY)
        self.xMeteor = xMeteor
        self.startX = startX

    def move(self):
        print(self.xMeteor, self.startX)
        if self.xMeteor <= self.startX:
            self.rect.x -= self.speedBulletX  # Move left
        else:
            self.rect.x += self.speedBulletX  # Move right
        self.rect.y -= self.speedBulletY  # Always move up



    def draw(self, screen):
        screen.blit(self.bullet, self.rect)

