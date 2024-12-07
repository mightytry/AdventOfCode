import sys
sys.path.insert(0, '.')
from tools import log, timer


class Line:
    def __init__(self, data, num) -> None:
        self.data = data
        self.num = num

    @property
    def is_empty(self):
        return not any(x == "#" for x in self.data)
    
    def __repr__(self) -> str:
        return f"Line({self.num})"
    
class Column:
    def __init__(self, data, num) -> None:
        self.data = data
        self.num = num

    @property
    def is_empty(self):
        return not any(x == "#" for x in self.data)
    
    def __repr__(self) -> str:
        return f"Column({self.num})"

class Galaxy:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Galaxy({self.x}, {self.y})"


def parse_data(data: str):
    START = 1000000 -1
    data = data.splitlines()

    rows = [[] for _ in range(len(data))]
    columns = [[] for _ in range(len(data[0]))]

    for n, y in enumerate(data):
        for m, x in enumerate(y):
            if x == "#":
                g = Galaxy(m, n)
                rows[n].append(g)
                columns[m].append(g)

    o = 0
    for n, x in enumerate(data):
        if not any(y == "#" for y in x): o += START
        else: 
            for x in rows[n]: x.y += o
    o = 0
    for n, x in enumerate(zip(*data)):
        if not any(y == "#" for y in x): o += START
        else: 
            for x in columns[n]: x.x += o
        

    return [x for y in rows for x in y]

@log
@timer
def main(data):
    data = parse_data(data)

    d = 0
    for n, g1 in enumerate(data):
        for g2 in data[n+1:]:
            d += abs(g1.x - g2.x) + abs(g1.y - g2.y)

    return d




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