import pygame
import math
from character import Character


class EnemyRotate(Character):

    LINEAR_MOVE =((1.0,0.2),(0.6,0.2), (0.7,0.3),(0.0,0.3))
    LODE_IMAGES_LOC = ((0,0),(1,0),(2,0))
    SPEED = 15
    move_pos = 0
    images = []
    image_index = 0

    def __init__(self,env_context, x=0, y=0):
        super().__init__(env_context, x, y)
        self.linear_move_abs = [(int(self._gc.SCREEN_WIDTH * x), int(self._gc.SCREEN_HEIGHT * y)) for x, y in self.LINEAR_MOVE]
        # self.imagemap = pygame.Surface(self._gc.SMALL_ENEMIES_SIZE)  # Initialize self.image with a surface
        self.imagemap = pygame.image.load(self._gc.SMALL_ENEMIES)
        self._load_image()
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.center = (x + self.linear_move_abs[0][0],y + self.linear_move_abs[0][1])

    def _load_image(self):
        for loc in self.LODE_IMAGES_LOC:
            rect = pygame.Rect(self._gc.SMALL_ENEMIES_LO[0] + loc[0] * self._gc.SMALL_ENEMIES_SIZE[0], self._gc.SMALL_ENEMIES_LO[1] + loc[1] * self._gc.SMALL_ENEMIES_SIZE[1], *self._gc.SMALL_ENEMIES_SIZE)
            image = self.imagemap.subsurface(rect)
            self.images.append(image)
        return


    def update(self):
        # rotate images
        self.image_index = self.image_index + 1 if self.image_index < (len(self.LODE_IMAGES_LOC)-1) * 3 else 0
        cx,cy = self.rect.centerx, self.rect.centery
        self.image = self.images[self.image_index % 3]
        self.rect.center = (cx,cy)

        # move linearly    
        for i in range(0, len(self.linear_move_abs) - 1):
            self.dx, self.dy = self.calculate_velocity(self.linear_move_abs[i], self.linear_move_abs[i+1])
            while True:
                if (self.dx > 0 and self.rect.centerx >= self.linear_move_abs[i+1][0]) or \
                (self.dx < 0 and self.rect.centerx <= self.linear_move_abs[i+1][0]) or \
                (self.dy > 0 and self.rect.centery >= self.linear_move_abs[i+1][1]) or \
                (self.dy < 0 and self.rect.centery <= self.linear_move_abs[i+1][1]):
                    break
                else:
                    return super().update()

    def calculate_velocity (self, from_pos, to_pos):
        #calc vector whose length is SPEED
        from_x, from_y = from_pos
        to_x, to_y = to_pos
        x, y  = to_x - from_x, to_y - from_y
        length = math.sqrt(x**2 + y**2) 
        x, y = x * self.SPEED / length, y * self.SPEED / length
        return (x , y)