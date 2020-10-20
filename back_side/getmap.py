class GetMap:

    def __init__(self):
        my_level = []
        with open("level.txt") as f:
            line = True
            while line:
                line = f.readline()
                if line:
                    line = line.replace("\n", "")
                    my_level.insert(len(self.my_level), list(line))
