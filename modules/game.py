from modules.player import Player
from modules.wall import Wall
from modules.guard import Guard


class Game:

    def __init__(self):
        self.player = Player(self)
        self.wall = Wall()
        self.guard = Guard()
