import pygame


class Player:

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.speed = 40
        self.image = pygame.image.load('assets/MacGyver.png')
        self.rect = self.image.get_rect()

    def move_right(self):
        self.rect.x += self.speed

    def move_left(self):
        self.rect.x -= self.speed

    def move_up(self):
        self.rect.y -= self.speed

    def move_down(self):
        self.rect.y += self.speed
