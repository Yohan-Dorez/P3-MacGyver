import pygame
from modules.level import Level


class Ether(Level):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/ether.png')
