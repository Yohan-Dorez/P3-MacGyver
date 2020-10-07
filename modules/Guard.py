import pygame
from modules.level import Level


class Guard(Level):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/Guard.png')
        self.rect = self.image.get_rect()
        self.rect.x = 560
        self.rect.y = 120
