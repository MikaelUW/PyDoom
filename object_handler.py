from sprite_object import *
from object_renderer import ObjectRenderer  # Importando a classe ObjectRenderer

class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.static_sprite_path = 'RaycastingGame/resources/static_sprites'
        self.anim_sprite_path = 'RaycastingGame/resources/animated_sprites'

        # Instância de ObjectRenderer para renderizar os objetos
        self.object_render = ObjectRenderer(game)

        # Adicionando sprites
        #self.add_sprite(SpriteObject(game))
        self.add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + '/dalton/1.png'))
        self.add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + '/thomson/1.png', pos=(8.5, 2)))
        self.add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + '/rutherford/1.png', pos=(12.5, 2)))
        self.add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + '/bohr/1.png', pos=(16.5, 2)))


    def update(self):
        # Atualiza todos os sprites na lista
        for sprite in self.sprite_list:
            sprite.update()

    def add_sprite(self, sprite):
        # Adiciona o sprite à lista
        self.sprite_list.append(sprite)

    def draw(self):
        # Chama o método draw de ObjectRenderer
        self.object_render.draw()  # Agora isso chama o draw de ObjectRenderer
