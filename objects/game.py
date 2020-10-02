from objects.maze import Maze
from objects.macgyver import Player


class Game:

    def __init__(self):
        self.maze = Maze()
        self.player = Player()
        self.pressed = {}
