import pygame
from global_constants import GlobalConstants

VIPER_IMAGE = "img/VicViperImage_resized.png"
SMALL_ENEMIES = "img/Small Enemies.png"
SCALE_FACTOR = 2

class Character(pygame.sprite.Sprite):
    def __init__(self, env_context, x=0, y=0):
        super().__init__()
        self._gc = GlobalConstants()     
        # self.image = pygame.image.load(VIPER_IMAGE)
        #self.rect.center = (x, y)  # 初期位置を外部から設定
        self.dx, self.dy = 0, 0

    def update(self):
        self.rect.centerx += self.dx
        self.rect.centery += self.dy
  
