import sys
sys.path.insert(0, '.')
from tools import log, timer


class Distance:
    def __init__(self, g1, g2) -> None:
        self.g1 = g1
        self.g2 = g2

    @property
    def distance(self):
        return abs(self.g1.x - self.g2.x) + abs(self.g1.y - self.g2.y)

class Galaxy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.connections = []
        self.distances = []

    def __repr__(self):
        return f"Galaxy({self.x}, {self.y})"


def parse_data(data: str):
    o = 0
    data = [[y for y in x] for x in data.splitlines()]
    for y in range(len(data)):
        is_empty = True
        for x, char in enumerate(data[y+o]):
            if char == "#":
                is_empty = False
        
        if is_empty:
            data.insert(y+o, ["." for x in range(len(data[y+o-1]))])
            o += 1

    o = 0
    for x in range(len(data[0])):
        is_empty = True
        for y, line in enumerate(data):
            if line[x+o] == "#":
                is_empty = False
        
        if is_empty:
            for y, line in enumerate(data):
                data[y].insert(x+o, ".")
            o += 1

    galaxys = [[Galaxy(m, n) for m, y in enumerate(x) if y == "#"] for n, x in enumerate(data) if "#" in x]

    galaxys = [x for y in galaxys for x in y]

    return galaxys

@log
@timer
def main(data):
    data = parse_data(data)

    d = []
    for n, g1 in enumerate(data):
        for g2 in data[n+1:]:
            d.append(Distance(g1, g2))

    return sum(x.distance for x in d)




if __name__ == "__main__":
    data1 = open("./Day 11/data1", "r").read()
    data2 = open("./Day 11/data2", "r").read()

    if data1 != "":
        main(data1)
    else:
        print("No data1 found")
    if data2 != "":
        main(data2)
    else:
        print("No data2 found")