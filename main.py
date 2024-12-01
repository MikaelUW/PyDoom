import pygame as pg
import sys
from settings import *
from mapa import *
from player import *
from raycasting import *
from object_renderer import *

class Game:
    def __init__(self):
        pg.init()
        # Define a tela com os valores WIDTH e HEIGHT importados de settings
        self.screen = pg.display.set_mode((WIDTH, HEIGHT), pg.RESIZABLE)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.new_game()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self, WIDTH, HEIGHT)  # Passe WIDTH e HEIGHT para o Player
        self.object_render = ObjectRenderer(self)
        self.raycasting = RayCasting(self)

    def update_screen(self):
        self.player.update()
        self.raycasting.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f"{self.clock.get_fps():.1f}")

    def draw_screen(self):
        self.screen.fill("#666667")
        self.object_render.draw()
        # Pra debug: descomente pra ver a visao teorica
        #self.map.draw()
        #self.player.draw_player()

    def check_exit(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def run(self):
        while True:
            self.check_exit()
            self.draw_screen()
            self.update_screen()

if __name__ == "__main__":
    game = Game()
    game.run()

