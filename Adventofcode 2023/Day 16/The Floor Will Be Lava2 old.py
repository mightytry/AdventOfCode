import sys
import time, copy
sys.path.insert(0, '.')
from tools import log, timer

sys.setrecursionlimit(1000000)

class Beam:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.tiles = []

    def __hash__(self) -> int:
        return hash((self.x, self.y, self.direction))
    
    def __repr__(self) -> str:
        return f"Beam[{self.x},{self.y},{self.direction}]"


class Tile:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type
        self.loops = {}
        self.visited = set()

    def __hash__(self) -> int:
        return hash((self.x, self.y))
    
    def get_beams(self, beam):
        match self.type:
            case ".":
                return [beam]
            case "/":
                beam.direction = tuple(map(lambda x: x-sum(beam.direction), beam.direction))
                return [beam]
            case "\\":
                if beam.direction[0] == -1 or beam.direction[1] == 1:
                    beam.direction = (beam.direction[0]+1, beam.direction[1]-1)
                    return [beam]
                else:
                    beam.direction = (beam.direction[0]-1, beam.direction[1]+1)
                    return [beam]
            case "-":
                if beam.direction[0] == 0:
                    beam.direction = (1, 0)
                    beam2 = Beam(beam.x, beam.y, (-1, 0))
                    return [beam, beam2] 
                else:
                    return [beam]
            case "|":
                if beam.direction[1] == 0:
                    beam.direction = (0, 1)
                    beam2 = Beam(beam.x, beam.y, (0, -1))
                    beam2.tiles = beam.tiles
                    return [beam, beam2]
                else:
                    return [beam]
                
    def __repr__(self) -> str:
        return  f"{self.type}[{self.x},{self.y},{self.loops}]"
    
    def __str__(self) -> str:
        return f"{self.type}"
    
class Loop:
    def __init__(self, beam, new_tile):
        self.tiles = beam.tiles[beam.tiles.index(new_tile):]
        self.size = len(self.tiles)
        prev = self.tiles[-1]
        for tile in self.tiles:
            direction = (tile.x - prev.x, tile.y - prev.y)
            tile.loops[direction] = self
            prev = tile

    
    def __repr__(self) -> str:
        return f"{self.size}"

class Map:
    def __init__(self, data):
        self.data = list(data)
        self.width = len(self.data[0])
        self.height = len(self.data)
        self.loops = set()


    def next(self, beams:list[Beam], loops: set[Loop] = set(), visited = set(), dis = 0):
        for beam in beams:
            new_tile = self.get_tile(beam)
            if (new_tile is None): 
                dis-=1
                continue
            if (beam.direction in new_tile.loops.keys()):
                if (new_tile.loops[beam.direction] in loops):
                    continue
                dis += new_tile.loops[beam.direction].size
                loops.add(new_tile.loops[beam.direction])
                continue

            if (beam.direction in new_tile.visited):
                if (self.get_tile(beam, False) == beam.tiles[beam.tiles.index(new_tile) +1]):
                    loop = Loop(beam, new_tile)
                    self.loops.add(loop)
                    loops.add(loop)
                    dis -=1
                    continue
                else:
                    dis-=1
                    continue


            dis +=1
            if (new_tile in visited):
                dis -= 1
            new_tile.visited.add(beam.direction)
            beam.tiles.append(new_tile)
            visited.add(new_tile)
            #open("log.txt", "a").write(f"{self}\n{dis}\n\n")
            dis += self.next(new_tile.get_beams(beam), loops, visited)
        return dis

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
    
    def __repr__(self) -> str:
        tilemap = set()
        for beam in self.beams:
            tilemap.add(self.data[beam.y][beam.x])
        return "\n".join(["".join([(str(tile) if any([tile not in b.tiles for b in self.beams]) else (str(tile.visited.__len__())if tile not in tilemap else "b")) for tile in row]) for row in self.data])

def parse_data(data:str):
    return Map([Tile(m, n, y) for m, y in enumerate(x)] for n, x in enumerate(data.splitlines()))

@timer
@log
def main(data):
    data = parse_data(data)
    a = []
    return data.next(data.data[0][0].get_beams(Beam(0,0,(1, 0))))
    for l in range(0, data.height):
        print(data.next(Beam(0,l,(1, 0))))

    return data.loops




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