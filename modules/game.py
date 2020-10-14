from modules.player import Player
from modules.guard import Guard
from modules.ether import Ether
import back_side


class Game:

    def __init__(self):
        self.player = Player(self)
        self.guard = Guard()
        self.ether = Ether()
        self.draw_map = back_side.getmap
