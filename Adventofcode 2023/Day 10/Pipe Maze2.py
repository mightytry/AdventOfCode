import sys
sys.path.insert(0, '.')
from tools import log, timer

sys.setrecursionlimit(100000)

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
    OPEN = [F, L]
    CLOSE = [J, SEVEN]

class Tile():
    Map = None

    def __init__(self, x, y, type) -> None:
        self.x = x
        self.y = y
        self.type = type
        self.distance = -1
        self.connections = []
        self.parent = None
        self.is_inner = None

    def eval(self, distance=0):
        for d in Types.MAP_ROWS[self.type]:
            x = self.x + d[0]
            y = self.y + d[1]

            if x < 0 or y < 0 or x >= len(self.Map[y]) or y >= len(self.Map): continue
            t = self.Map[y][x]
            self.connections.append(t)
        if self.parent not in self.connections and distance != 0:
            return
        self.distance = distance
        for t in self.connections:
            if t.type != Types.EMPTY and (t.distance == -1 or t.distance > distance+1):
                t.parent = self
                t.eval(distance+1)
    
    def get_neighbours(self, is_inner):
        self.is_inner =     def get_neighbours(self, is_inner):

        for y in range(-1, 2):
            for x in range(-1, 2):
                if x == 0 and y == 0: continue
                nx = self.x + x
                ny = self.y + y
                if nx < 0 or ny < 0 or ny >= len(self.Map) or nx >= len(self.Map[ny]): continue
                t = self.Map[ny][nx]
                if t.distance != -1 or t.is_inner == False: continue
                t.get_neighbours(is_inner)

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
        #return str(self.distance)
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

    data.eval()

    c = 0

    #return "\n".join(["".join("".join(str(int(y.is_inner) if y.is_inner != None else y) for y in x)) for x in Tile.Map])
    #return "\n".join(["".join("".join(str(1 if y.distance != -1 else y) for y in x)) for x in Tile.Map])
    return sum((1 if x.is_inner else 0) for x in Tile.as_one_dim())




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