class Maze:

    def getMap(self):
        map = []
        with open("level.txt") as f:
            line = True
            while line:
                line = f.readline()
                if line:
                    line = line.replace("\n", "")
                    map.insert(len(self.map), list(line))

        for x in range(0, 15):
            for y in range(0, 15):
                objectToDisplay = map[x][y]
                if objectToDisplay == "x":
                    pygame.rect.draw(Wall)
