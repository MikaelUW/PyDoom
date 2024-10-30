import pygame as pg
import sys
from settings import *
from mapa import *
from player import *

class Game:
    def __init__(self):
        pg.init()
        info = pg.display.Info()
        self.WIDTH, self.HEIGHT = info.current_w, info.current_h
        self.screen = pg.display.set_mode((self.WIDTH, self.HEIGHT), pg.FULLSCREEN)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.new_game()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self, self.WIDTH, self.HEIGHT)  # Passe WIDTH e HEIGHT

    def update_screen(self):
        self.player.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f"{self.clock.get_fps():.1f}")

    def draw_screen(self):
        self.screen.fill("black")
        self.map.draw()
        self.player.draw_player()

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
 ### RAY CASTING