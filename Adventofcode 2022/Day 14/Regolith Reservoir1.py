import sys
import time

import numpy as np
sys.path.insert(0, '.')
from tools import log

class TYPE:
    SAND_SOURCE = "+"
    SAND = "o"
    ROCK = "#"
    AIR = "."

class Point:
    def __init__(self, x, y, type) -> None:
        self.x = x
        self.y = y
        self.type = type

    def __repr__(self) -> str:
        return f"{self.type}"

class Line:
    def __init__(self, points) -> None:
        self.unparsed_points = points
        self.points = []
        self.eval()

    def eval(self):
        for p in range(-1, len(self.unparsed_points)*-1, -1):
            point1 = self.unparsed_points[p-1]
            point2 = self.unparsed_points[p]
            points = list(zip(point1, point2))
            point = [max(i)-min(i) for i in points]

            for i in range(point[0]+1):
                for j in range(point[1]+1):
                    self.points.append(Point(i+min(points[0]), j+min(points[1]), TYPE.ROCK))

    def __repr__(self) -> str:
        return f"{self.points}"

class Map:
    def __init__(self, lines) -> None:
        self.lines = lines
        self.sizes = self.get_sizes()
        self.map = self.get_map()
        self.fill_map()

    def get_sizes(self):
        x = [x.x for i in self.lines for x in i.points]
        y = [x.y for i in self.lines for x in i.points]
        self.start = (min(x), min(y))
        return [max(x)-min(x),max(y)- min(y) ]
    
    def get_map(self):
        return np.full((self.sizes[1]+1, self.sizes[0]+1), TYPE.AIR,dtype=str)
    
    def fill_map(self):
        for line in self.lines:
            for point in line.points:
                self[point.x, point.y] = point.type

    def place_one(self):
        pos = (500, 0)
        try:
            while True:
                if self[pos[0], pos[1]+1] == TYPE.AIR:
                    pos = (pos[0], pos[1]+1)
                    continue
                elif self[pos[0] - 1, pos[1]+1] == TYPE.AIR:
                    pos = (pos[0]- 1, pos[1]+1)
                    continue
                elif self[pos[0] + 1, pos[1]+1] == TYPE.AIR:
                    pos = (pos[0]+ 1, pos[1]+1)
                    continue
                else:
                    self[pos[0], pos[1]] = TYPE.SAND
                    break
            return True
        except IndexError:
            return False


    def __repr__(self) -> str:
        return "\n".join(map(str,self.map.tolist()))
    
    def __str__(self) -> str:
        return repr(self)
    
    def __getitem__(self, key):
        return self.map[key[1]-self.start[1], key[0]-self.start[0]]
    
    def __setitem__(self, key, value):
        self.map[key[1]-self.start[1], key[0]-self.start[0]] = value

def parse_data(data):
    lines = []

    for line in data.splitlines():
        pos = line.split(" -> ")
        pos = [i.split(",") for i in pos]
        pos = [[int(i[0]), int(i[1])] for i in pos]
        lines.append(Line(pos))

    return lines

@log
def main(data):
    data = parse_data(data)

    l= Line([])
    l.points.append(Point(500,0,TYPE.SAND_SOURCE))
    data.append(l)

    _map = Map(data)

    c = 0
    while _map.place_one():
        c+=1

    return c




if __name__ == "__main__":
    data1 = open("./Day 14/data1", "r").read()
    data2 = open("./Day 14/data2", "r").read()

    if data1 != "":
        main(data1)
    else:
        print("No data1 found")
    if data2 != "":
        main(data2)
    else:
        print("No data2 found")