import math
import sys
sys.path.insert(0, '.')
from tools import log
sys.setrecursionlimit(1500000)

class Map:
    def __init__(self) -> None:
        self.map = []
        self.start = None
        self.end = None

    def __repr__(self) -> str:
        c = "\n".join([repr(x) for x in self.map])
        return c

    def find_shortest_path(self, current):
        for neighbour in current.neighbours.neighbours:
            if neighbour == None:
                continue
            if neighbour.elevation - current.elevation > 1:
                continue

            if neighbour.cost > current.cost + 1:
                neighbour.cost = current.cost + 1
                neighbour.previous = current
                if neighbour == self.end:
                    return neighbour
                else:
                    self.find_shortest_path(neighbour)
        

class Position:
    def __init__(self, x, y, elevation, map) -> None:
        self.x = x
        self.y = y
        self.elevation = elevation
        self.map = map

        self.cost = math.inf
        self.previous = None

        self.neighbours = Neighbours(self, map)

    def eval(self):
        self.neighbours.eval()

    def __repr__(self) -> str:
        return f"{self.cost}"


class Neighbours:
    def __init__(self, parrent, map) -> None:
        self.parrent = parrent
        self.map = map
        self.neighbours = []
        self.visited = False
        #   | 1 | 
        # 2 | P | 3
        #   | 4 |

    def eval(self):
        for i in ((-1, 0),(0, -1), (0, 1), (1, 0)):
            x = self.parrent.x + i[1]
            y = self.parrent.y + i[0]
            if x < 0 or y < 0 or x >= len(self.map.map[0]) or y >= len(self.map.map):
                self.neighbours.append(None)
                continue
            self.neighbours.append(self.map.map[y][x])            

def parse_data(data):
    data = data.splitlines()
    map = Map()
    for y,line in enumerate(data):
        map.map.append([])
        for x,char in enumerate(line):
            map.map[y].append(Position(x, y, ord(char)-97, map))
            if char == "S":
                map.start = map.map[y][x]
                map.start.elevation = 0
                map.start.cost = 0
            elif char == "E":
                map.end = map.map[y][x]
                map.end.elevation = 25
                

    for y,line in enumerate(map.map):
        for x,position in enumerate(line):
            position.eval()

    return map

@log
def main(data):
    data = parse_data(data)

    data.find_shortest_path(data.start)

    return data.end




if __name__ == "__main__":
    data1 = open("./Day 12/data1", "r").read()
    data2 = open("./Day 12/data2", "r").read()

    if data1 != "":
        main(data1)
    else:
        print("No data1 found")
    if data2 != "":
        main(data2)
    else:
        print("No data2 found")