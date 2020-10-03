import pygame
from objects.maze import Maze
from objects.player import Player
from objects.wall import Wall


class Game:

    def __init__(self):
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.maze = Maze()
        # walls group
        self.wall = Wall(self)
        self.all_walls = pygame.sprite.Group()
        self.spawn_wall()

    def collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_wall(self):
        wall = Wall(self)
        self.all_walls.add(wall)
