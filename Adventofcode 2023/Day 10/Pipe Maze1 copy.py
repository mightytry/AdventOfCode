import sys
sys.path.insert(0, '.')
from tools import log, timer

class Types():
    MAP = ["|", "-", "L", "J", "7", "F", ".", "S"]
    NORTH = (0, -1)
    SOUTH = (0, 1)
    EAST = (1, 0)
    WEST = (-1, 0)

    MAP_ROWS = [
        (NORTH, SOUTH), # |
        (EAST, WEST),   # -
        (NORTH, EAST),  # L
        (NORTH, WEST),  # J
        (SOUTH, WEST),  # 7
        (SOUTH, EAST),  # F
        (),             # .
        (NORTH, SOUTH, EAST, WEST), # S
    ]
    START = MAP.index("S")
    STRAIGHT = MAP.index("|")
    CROSS = MAP.index("-")
    L = MAP.index("L")
    J = MAP.index("J")
    SEVEN = MAP.index("7")
    F = MAP.index("F")
    EMPTY = MAP.index(".")

class Tile():
    Map = None

    def __init__(self, x, y, type) -> None:
        self.x = x
        self.y = y
        self.type = type
        self.distance = -1
        self.connections = []
        self.parent = None

    def eval(self):
        for d in Types.MAP_ROWS[self.type]:
            x = self.x + d[0]
            y = self.y + d[1]

            if x < 0 or y < 0 or x >= len(self.Map[y]) or y >= len(self.Map): continue
            t = self.Map[y][x]
            #self.connections.append(t)
            if t.type != Types.EMPTY and t.distance == -1:
               yield t

    @classmethod
    def get_start(cls):
        for x in cls.Map:
            for y in x:
                if y.type == Types.START:
                    return y
                
    @classmethod          
    def as_one_dim(cls):
        return [x for y in cls.Map for x in y]
                
    def __repr__(self) -> str:
        return str(self.distance)
        return str(Types.MAP[self.type])
    
    def __str__(self) -> str:
        return self.__repr__()

@timer
def parse_data(data):
    Tile.Map = [[Tile(m, n, Types.MAP.index(y)) for m, y in enumerate(x)] for n, x in enumerate(data.splitlines())]

    return Tile.get_start()

@log
@timer
def main(data):
    data = parse_data(data)
    start = data
    start.distance = 0
    data = list(filter(lambda x: len(list(x.eval())) == 1, data.eval()))
    d = 0
    while data != []:
        d += 1
        b = []
        for x in data:
            x.distance = d
            c = list(x.eval())
            if len(c) == 1:
                b.extend(c)
        data = b

        
        
    return max(start.as_one_dim(), key=lambda x: x.distance).distance




if __name__ == "__main__":
    data1 = open("./Day 10/data1", "r").read()
    data2 = open("./Day 10/data2", "r").read()

    if data1 != "":
        main(data1)
    else:
        print("No data1 found")
    if data2 != "":
        main(data2)
    else:
        print("No data2 found")