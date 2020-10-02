import pygame
from objects.maze import Maze


class Player(Maze):

    def __init__(self):
        super().__init__()
        self.x = 40
        self.y = 40
        self.speed = 40
        self.image = pygame.image.load("assets/MacGyver.png")
        self.rect = self.image.get_rect()
        self.rect.x = 520
        self.rect.y = 480

    def move_right(self):
        self.rect.x += self.speed

    def move_left(self):
        self.rect.x -= self.speed

    def move_up(self):
        self.rect.y -= self.speed

    def move_down(self):
        self.rect.y += self.speed
