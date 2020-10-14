import pygame


class Wall:

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/wall.png')
        self.rect = self.image.get_rect()
