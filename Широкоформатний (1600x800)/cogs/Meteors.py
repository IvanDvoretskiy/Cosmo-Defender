import config as cfg
import random
import pygame as pg

CREATE_ENEMY = pg.USEREVENT + 1
pg.time.set_timer(CREATE_ENEMY, 1000)

def create_enemy(coordinates, speed, size) -> list:
    enemyCfg = {
        "1": ['./images/Meteors/big.png', 100, 120],
        "2": ['./images/Meteors/medium.png', 50, 70],
        "3": ['./images/Meteors/medium.png', 25, 40]
    }
    speed = float(speed)

    x, y = map(int, coordinates.split())

    enemy_size = (enemyCfg[size][1], enemyCfg[size][2])
    enemy = pg.transform.scale(pg.image.load(enemyCfg[size][0]).convert_alpha(), enemy_size)
    enemy_rect = pg.Rect(x, y, *enemy_size)
    enemy_move = [speed, 0]

    return [enemy, enemy_rect, enemy_move]

