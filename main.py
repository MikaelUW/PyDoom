import pygame as pg
import sys
from settings import *
from mapa import * 

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
        self.clock = pg.time.Clock()
        self.new_game()

    def new_game(self):
        self.map = Map(self)  # Passa a instância de Game para Map

    def show_fps(self):
        pg.display.flip()
        self.clock.tick(FPS)
        pg.display.set_caption(f"{self.clock.get_fps():.1f}")
        
    # draw things on screnn
    def black_screen(self):
        self.screen.fill("black")
        self.map.draw()  # Desenha o mapa

    def check_exit(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def run(self):
        while True:
            self.check_exit()
            self.black_screen()
            self.show_fps()

if __name__ == "__main__":
    game = Game()
    game.run()

#3:43 time