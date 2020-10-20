from modules.player import Player
from modules.guard import Guard
from modules.ether import Ether
from modules.wall import Wall
from back_side import *


class Game:

    def __init__(self):
        self.player = Player(self)
        self.guard = Guard()
        self.ether = Ether()
        self.draw_map = getmap.GetMap()
        self.wall = Wall()
