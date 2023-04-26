import sys
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
            point = [point1[0] -point2[0], point2[1] - point1[1]]

            for i in range(point[0]+1):
                for j in range(point[1]+1):
                    self.points.append(Point(i+point1[0], j+point1[1], TYPE.ROCK))

    def __repr__(self) -> str:
        return f"{self.points}"

class Map:
    def __init__(self) -> None:
        pass


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

    return data




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