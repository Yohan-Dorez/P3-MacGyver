import pygame


class Maze(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.background = pygame.image.load('assets/background.png')
