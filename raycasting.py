import pygame as pg
import math
from settings import *

class RayCasting:
    def __init__(self, game):
        self.game = game

    def ray_cast(self):
        ox, oy = self.game.player.pos
        x_map, y_map = self.game.player.map_pos

        ray_angle = self.game.player.angle - HALF_FOV + 0.0001
        for ray in range(NUM_RAYS):
            sin_a = math.sin(ray_angle)
            cos_a = math.cos(ray_angle)

            # _____________Horizontais_____________
            y_hor, dy = (y_map + 1, 1) if sin_a > 0 else (y_map - 1e-6, -1)

            depth_hor = (y_hor - oy) / sin_a
            x_hor = ox + depth_hor * cos_a

            delta_depth = dy / sin_a
            dx = delta_depth * cos_a

            for i in range(MAX_DEPTH):
                tile_hor = int(x_hor), int(y_hor)
                if tile_hor in self.game.map.world_map:
                    break
                x_hor += dx
                y_hor += dy
                depth_hor += delta_depth

            # _____________Verticais_____________
            x_vert, dx = (x_map + 1, 1) if cos_a > 0 else (x_map - 1e-6, -1)

            depth_vert = (x_vert - ox) / cos_a
            y_vert = oy + depth_vert * sin_a

            delta_depth = dx / cos_a
            dy = delta_depth * sin_a

            for i in range(MAX_DEPTH):
                tile_vert = int(x_vert), int(y_vert)
                if tile_vert in self.game.map.world_map:
                    break
                x_vert += dx
                y_vert += dy
                depth_vert += delta_depth

            # _____________Profundidade_____________
            if depth_vert < depth_hor:
                depth = depth_vert
            else:
                depth = depth_hor

            # Pra debug: mostra os raios na tela
        #    pg.draw.line(self.game.screen, 'yellow', (100 * ox, 100 * oy),
        #                 (100 * ox + 100 * depth * cos_a, 100 * oy + 100 * depth * sin_a), 2)


            # _____________Remove olho de peixe_____________
            # Testar com e sem depois para a aplicacao da textura de tv antiga.

            depth *= math.cos(self.game.player.angle - ray_angle)

            # _____________Projeçao_____________
            proj_heigth = SCREEN_DIST / (depth + 0.0001)

            # _____________Desenha os muros_____________

            color = [255 / (1 + depth ** 5 * 0.00002)] * 3 #adiciona o fog effect
            pg.draw.rect(self.game.screen, color,
                         (ray * SCALE, HALF_HEIGTH - proj_heigth // 2, SCALE, proj_heigth))

            ray_angle += DELTA_ANGLE

    def update(self):
        self.ray_cast()
