import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.x = 40
        self.y = 40
        self.speed = 40
        self.image = pygame.image.load('assets/MacGyver.png')
        self.rect = self.image.get_rect()
        self.rect.x = 520
        self.rect.y = 480

    def move_right(self):
        if not self.game.collision(self, self.game.all_walls):
            self.rect.x += self.speed

    def move_left(self):
        if not self.game.collision(self, self.game.all_walls):
            self.rect.x -= self.speed

    def move_up(self):
        if not self.game.collision(self, self.game.all_walls):
            self.rect.y -= self.speed

    def move_down(self):
        if not self.game.collision(self, self.game.all_walls):
            self.rect.y += self.speed
