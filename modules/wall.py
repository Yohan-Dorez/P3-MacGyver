import pygame
from modules.level import Level


class Wall(Level):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/wall.png')

    def draw_wall(self, display_surf, image_surf):
        bx = 0
        by = 0
        for i in range(0, self.M * self.N):
            if self.level[bx + (by * self.M)] == 1:
                display_surf.blit(image_surf, (bx * 40, by * 40))

            bx = bx + 1
            if bx > self.M - 1:
                bx = 0
                by = by + 1
