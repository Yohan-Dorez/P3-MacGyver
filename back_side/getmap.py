class Maze:

    def getMap(self):
        maze = []
        with open("level.txt") as f:
            line = True
            while line:
                line = f.readline()
                if line:
                    line = line.replace("\n", "")
                    maze.insert(len(self.maze), list(line))

        for x in range(0, 15):
            for y in range(0, 15):
                objectToDisplay = maze[x][y]
                if objectToDisplay == "x":
                    pygame.rect.draw(Wall)
