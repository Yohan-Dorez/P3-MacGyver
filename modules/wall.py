import pygame


class Wall(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/wall.png')
        self.rect = self.image.get_rect()

#    def draw_wall(self, display_surf, image_surf):
#         bx = 0
#         by = 0
#         for i in range(0, self.x * self.y):
#             if self.maze[bx + (by * self.x)] == 1:
#                 display_surf.blit(image_surf, (bx * 40, by * 40))
#
#             bx = bx + 1
#             if bx > self.x - 1:
#                 bx = 0
#                 by = by + 1
