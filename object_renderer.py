import pygame as pg
from settings import *

class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_textures()
        self.sky_image = self.get_texture('RaycastingGame/resources/textures/1.png', (WIDTH, HALF_HEIGTH))
        self.sky_offsert = 0

    def draw(self):
        self.draw_background()
        self.render_game_objects()
        
    def draw_background(self):
       # self.skt_offsert = (self.sky_offsert + 4.0 * self.game.player.angle) % WIDTH
        #self.screen.blit(self.sky_image, (-self.skt_offsert, 0))
        #self.screen.blit(self.sky_image, (-self.skt_offsert + WIDTH, 0))
        #Chao
        pg.draw.rect(self.screen, FLOOR_COLOR, (0, HALF_HEIGTH, WIDTH, HEIGHT))

    def render_game_objects(self):
        list_objects = self.game.raycasting.object_to_render
        for depth, image, pos in list_objects:
            self.screen.blit(image, pos)

    @staticmethod
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)
        
    def load_wall_textures(self):
        return {
            1: self.get_texture('RaycastingGame/resources/textures/1.png'),
            2: self.get_texture('RaycastingGame/resources/textures/2.png'),
            3: self.get_texture('RaycastingGame/resources/textures/3.png'),
            4: self.get_texture('RaycastingGame/resources/textures/4.png'),
            5: self.get_texture('RaycastingGame/resources/textures/5.png'),
        }