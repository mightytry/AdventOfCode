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
    o = 0
    data = data.splitlines()
    lines = [Line(list(x), n) for n, x in enumerate(data)]
    cols = [Column(x, n) for n, x in enumerate(zip(*data))]

    empty_lines = [x for x in lines if x.is_empty]
    empty_cols = [x for x in cols if x.is_empty]

    galaxys = [[Galaxy(m, n) for m, y in enumerate(x.data) if y == "#"] for n, x in enumerate(lines) if "#" in x.data]
    galaxys = [x for y in galaxys for x in y]

    for g1 in galaxys:
        line = filter(lambda x: x.num <= g1.y, lines)
        col = filter(lambda x: x.num <= g1.x, cols)
        

    return empty_lines, empty_cols, galaxys

@log
@timer
def main(data):
    data = parse_data(data)
    return data
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