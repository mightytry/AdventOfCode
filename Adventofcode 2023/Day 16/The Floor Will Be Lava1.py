import sys
import time
sys.path.insert(0, '.')
from tools import log, timer

class Beam:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def __hash__(self) -> int:
        return hash((self.x, self.y, self.direction))
    

class Tile:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.visited = set()
        self.type = type

    def __hash__(self) -> int:
        return hash((self.x, self.y))
    
    def get_beams(self, direction):
        self.visited.add(direction)
        match self.type:
            case ".":
                return [Beam(self.x, self.y, direction)]
            case "/":
                if sum(direction) == 1:
                    return [Beam(self.x, self.y, tuple(map(lambda x: x-1, direction)))]
                else:
                    return [Beam(self.x, self.y, tuple(map(lambda x: x+1, direction)))]
            case "\\":
                if direction[0] == -1 or direction[1] == 1:
                    return [Beam(self.x, self.y, (direction[0]+1, direction[1]-1))]
                else:
                    return [Beam(self.x, self.y, (direction[0]-1, direction[1]+1))]
            case "-":
                if direction[0] == 0:
                    return [Beam(self.x, self.y, (1, 0)), Beam(self.x, self.y, (-1, 0))]
                else:
                    return [Beam(self.x, self.y, direction)]
            case "|":
                if direction[1] == 0:
                    return [Beam(self.x, self.y, (0, 1)), Beam(self.x, self.y, (0, -1))]
                else:
                    return [Beam(self.x, self.y, direction)]
                
    def __repr__(self) -> str:
        return f"{self.type}"
    

class Map:
    def __init__(self, data):
        self.data = list(data)
        self.width = len(self.data[0])
        self.height = len(self.data)
        self.beams = set()

    def next(self):
        new_beams = set()
        for beam in self.beams:
            new_tile = self.get_tile(beam.x, beam.y, beam.direction)
            if (new_tile is None): 
                continue
            if (beam.direction in new_tile.visited):
                continue
            new_beams.update(new_tile.get_beams(beam.direction))
        self.beams = new_beams
        return len(self.beams) != 0

    def get_tile(self, x, y, direction):
        if x + direction[0] < 0 or x + direction[0] >= self.width:
            return None
        if y + direction[1] < 0 or y + direction[1] >= self.height:
            return None

        return self.data[y + direction[1]][x + direction[0]]
    
    def __repr__(self) -> str:
        tilemap = set()
        for beam in self.beams:
            tilemap.add(self.data[beam.y][beam.x])
        return "\n".join(["".join([(str(tile) if len(tile.visited) == 0 else ("#" if tile not in tilemap else "b")) for tile in row]) for row in self.data])

def parse_data(data:str):
    return Map([Tile(m, n, y) for m, y in enumerate(x)] for n, x in enumerate(data.splitlines()))

@timer
@log
def main(data):
    data = parse_data(data)
    data.data[0][0].visited.add((1, 0))
    data.beams.update(data.data[0][0].get_beams((1, 0)))

    while data.next():
        continue

    return list(filter(lambda x: len(x.visited) != 0, (y for x in data.data for y in x))).__len__()




if __name__ == "__main__":
    data1 = open("./Day 16/data1", "r").read()
    data2 = open("./Day 16/data2", "r").read()

    if data1 != "":
        main(data1)
    else:
        print("No data1 found")
    if data2 != "":
        main(data2)
    else:
        print("No data2 found")