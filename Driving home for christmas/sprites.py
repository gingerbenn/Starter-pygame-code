import pygame

from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game=game
        self._layer=PLAYER_LAYER
        self.groups=self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x=x*TILESIZE
        self.y=y*TILESIZE
        self.width=TILESIZE * 2
        self.height=TILESIZE

        self.x_change = 0
        self.y_change = 0

        self.image = self.game.asset_loader.player_image

        self.rect=self.image.get_rect()
        self.rect.x=self.x
        self.rect.y=self.y

    def update(self):
        self.movement()

        self.rect.x+=self.x_change
        self.rect.y+=self.y_change

        self.x_change = 0
        self.y_change = 0

    def movement(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x_change-= PLAYER_SPEED
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x_change+=PLAYER_SPEED
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.y_change-=PLAYER_SPEED
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.y_change+=PLAYER_SPEED

class Block(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x=x*TILESIZE
        self.y=y*TILESIZE
        self.width=TILESIZE
        self.height=TILESIZE

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill("red")

        self.rect=self.image.get_rect()
        self.rect.x=self.x
        self.rect.y=self.y

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()