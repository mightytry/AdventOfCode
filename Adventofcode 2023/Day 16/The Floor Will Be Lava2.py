import sys
import time
from functools import lru_cache
sys.path.insert(0, '.')
from tools import log, timer

sys.setrecursionlimit(100000000)

class Beam:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def getloop(self, tile):
        try:
            index = self.tiles.index((tile, self.direction))
            loop_tiles = self.tiles[index:]
            loop = Loop(loop_tiles)
            for t in loop_tiles:
                t[0].loops[t[1]] = loop
            return loop
        except ValueError:
            return None

    def __repr__(self) -> str:
        return f"Beam[{self.x},{self.y},{self.direction}]"

    def __hash__(self) -> int:
        return self.x*255+self.y+ self.direction[0]*1024+self.direction[1]*1024*1024
    
    def __eq__(self, o: object) -> bool:
        if isinstance(o, Beam):
            return self.x == o.x and self.y == o.y and self.direction == o.direction
        return hash(self) == hash(o)

class Tile:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type

    def __hash__(self) -> int:
        return self.x*255+self.y
    
    def get_beams(self, direction):
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
        return f"{self.x}, {self.y}, {self.loops}"
    
class Map:
    def __init__(self, data):
        self.data = list(data)
        self.width = len(self.data[0])
        self.height = len(self.data)
        self.cache = {}

    def next(self, beam, visited = {}):
        new_tile = self.get_tile(beam)

        if (new_tile is None):
            return None

        if ((c:=self.cache.get(beam, None)) != None):
            return c

        if (beam in visited and visited[beam] == 2):
            return None


    
        visited[beam] = 0 if beam not in visited else visited[beam]+1
        result = {new_tile}
        for b in new_tile.get_beams(beam.direction):
            if ((res:=self.next(b)) is not None):
                result.update(res)

      
        self.cache[beam] = result

        return result


    def get_tile(self, beam:Beam, set:bool = True):
        if beam.x + beam.direction[0] < 0 or beam.x + beam.direction[0] >= self.width:
            return None
        if beam.y + beam.direction[1] < 0 or beam.y + beam.direction[1] >= self.height:
            return None
        
        if set:
            beam.x += beam.direction[0]
            beam.y += beam.direction[1]
        else:
            return self.data[beam.y + beam.direction[1]][beam.x + beam.direction[0]]
        return self.data[beam.y][beam.x]
    
    def print(self, beams) -> str:
        tilemap = set()
        for beam in beams:
            tilemap.add(self.data[beam.y][beam.x])
        return "\n".join(["".join([(str(tile) if len(tile.visited) == 0 else ("#" if tile not in tilemap else "b")) for tile in row]) for row in self.data])

def parse_data(data:str):
    return Map([Tile(m, n, y) for m, y in enumerate(x)] for n, x in enumerate(data.splitlines()))

@timer
@log
def main(data):
    data = parse_data(data)
   
    m = 0
    for i in range(data.height):
        m = max(m, len(data.next(Beam(-1, i, (1, 0)), {})))
        m = max(m, len(data.next(Beam(data.width, i, (-1, 0)), {})))

    for i in range(data.width):
        m = max(m, len(data.next(Beam(i, -1, (0, 1)), {})))
        m = max(m, len(data.next(Beam(i, data.height, (0, -1)), {})))
    return m




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