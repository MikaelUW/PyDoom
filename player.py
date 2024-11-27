import pygame as pg
import math
from settings import *
from mapa import *

class Player:
    def __init__(self, game, width, height):
        self.game = game
        self.WIDTH = width
        self.HEIGHT = height
        self.x, self.y = PLAYER_START_POS
        self.angle = PLAYER_ANGLE

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = PLAYER_SPEED * self.game.delta_time

        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            dx += speed * cos_a
            dy += speed * sin_a
        if keys[pg.K_s]:
            dx -= speed * cos_a
            dy -= speed * sin_a

        # Permite a rotação apenas com 'A' e 'D'
        if keys[pg.K_a]:
            self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
        if keys[pg.K_d]:
            self.angle += PLAYER_ROT_SPEED * self.game.delta_time

        self.check_wall_collision(dx, dy)

        # Garante que o ângulo fique dentro de 0 a 2π
        self.angle %= math.tau
    #ve se tem muro
    def check_wall(self, x, y):
        return (x, y) not in self.game.map.world_map
    #da colisao se tem muro
    def check_wall_collision (self, dx, dy):
        scale = PLAYER_FAT / self.game.delta_time
        if self.check_wall(int(self.x + dx * scale), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy * scale)):
            self.y += dy

    def draw_player(self):
        pg.draw.line(self.game.screen, 'yellow', 
                    (self.x * 100, self.y * 100),
                    (self.x * 100 + self.WIDTH * math.cos(self.angle),
                     self.y * 100 + self.HEIGHT * math.sin(self.angle)), 2)
        pg.draw.circle(self.game.screen, 'green', (self.x * 100, self.y * 100), 15)

    def update(self):
        self.movement()

    @property
    def pos(self):
        return self.x, self.y

    @property
    def map_pos(self):
        return int(self.x), int(self.y)
