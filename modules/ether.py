import pygame
import random
from modules.level import Level


class Ether(Level):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/ether.png')
        self.level = Level
        self.rect = self.image.get_rect()
