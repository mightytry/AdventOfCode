import sys
sys.path.insert(0, '.')
from tools import log, timer
from aocd import submit

class Direction:
    def __init__(self, dx, dy) -> None:
        self.dx = dx
        self.dy = dy

    def rotate(self):
        return Direction(-self.dy, self.dx)
    
    def apply(self, x, y):
        return (self.dx + x, self.dy + y)
    
    def __hash__(self) -> int:
        return hash((self.dx, self.dy))
    
    def __eq__(self, value: object) -> bool:
        if (isinstance(value, Direction)):
            return self.dx == value.dx and self.dy== value.dy
        return False

class Tile():
    WALL = "#"

    def __init__(self, type, x, y) -> None:
        self.type = type
        self.x = x
        self.y = y
        self.visited = set()

    def visit(self, direction):
        self.visited.add(direction)

    @property
    def pos(self):
        return self.x, self.y

    @property
    def is_start(self):
        return self.type == "^"
    
    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __eq__(self, value: object) -> bool:
        if (isinstance(value, Tile)):
            return self.x == value.x and self.y == value.y
        return False
    
    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
    
class Guard():
    def __init__(self, tile, direction) -> None:
        self.tile = tile
        self.direction = direction
        self.visited = set()

    def goto(self, tile, sim = False):
        self.tile = tile
        self.visited.add((tile,self.direction))

    def rotate(self):
        self.direction = self.direction.rotate()

    def __str__(self) -> str:
        return str(self.tile)

class Map():
    def __init__(self, tiles) -> None:
        self.tiles = tiles

    def get_start(self):
        for row in self.tiles:
            for tile in row:
                if (tile.is_start):
                    return tile
                
    def get_tile(self, x, y):
        if (x in range(0, len(self.tiles[0])) and y in range(0, len(self.tiles))):
            return self.tiles[y][x]
        return None
                
    def move(self, guard, wall= None):
        nt = self.get_tile(*guard.direction.apply(*guard.tile.pos))
        if (nt is not None):
            if nt.type == Tile.WALL or nt == wall:
                guard.rotate()
                return None
            else:
                if (wall and (nt,guard.direction) in guard.visited):
                    return True
                guard.goto(nt, wall != None)
                return None
        else:
            return False
        
    @property
    def visited(self):
        for row in self.tiles:
            for t in row:
                if (len(t.visited) != 0):
                    yield t

    def __str__(self) -> str:
        return "\n".join(["".join([x.type if len(x.visited) == 0 else "X" for x in row]) for row in self.tiles])

def parse_data(data):
    return Map([list(Tile(t, x, y) for x, t in enumerate(row.strip())) for y, row in enumerate(data)])


def main(data):
    map = parse_data(data)
    guard = Guard(map.get_start(), Direction(0, -1))
    prev = guard.tile
    cnt = 0
    while(map.move(guard) is not False):
        g = Guard(prev, guard.direction)
        if (prev != guard.tile):
            while ((res := map.move(g, guard.tile)) is None):
                pass
            if (res is True):
                cnt += 1
        prev = guard.tile
    return cnt

#2226
# high

if __name__ == "__main__":
    SUBMIT = False
    for num in range(1):
        # last line is expected output
        example = open(f"./Day 6/example{num}", "r").readlines()
        print("Got:", main(example[0:-1]), "Expected:", example[-1].strip().split(",")[1])
    data1 = open("./Day 6/data1", "r").readlines()

    if data1 != "":
        if SUBMIT:
            submit(main(data1), day=6, year=2024)
        else:
            print(main(data1))
    else:
        print("No data1 found")