import sys

import numpy as np
sys.path.insert(0, '.')
from tools import log


class Rectangle:
    def __init__(self, id, pos, size) -> None:
        self.id = id
        self.pos = int(pos[0]), int(pos[1])
        self.size = int(size[0]), int(size[1])



def parse_data(data):
    data = data.split("\n")
    rects = []
    for d in data:
        id = d.split(" ")[0].strip("#")
        pos = d.split(" ")[2].strip(":").split(",")
        size = d.split(" ")[3].split("x")
        rects.append(Rectangle(id, pos, size))

    return rects

@log
def main(data):
    data = parse_data(data)

    for d in data:
        for g in data:
            if d.id != g.id:
                if d.pos[0] < g.pos[0] + g.size[0] and d.pos[0] + d.size[0] > g.pos[0] and d.pos[1] < g.pos[1] + g.size[1] and d.pos[1] + d.size[1] > g.pos[1]:
                    data.remove(d)
                    data.remove(g)
                    break
        

    return  data




if __name__ == "__main__":
    data1 = open("./Day 3/data1", "r").read()
    data2 = open("./Day 3/data2", "r").read()

    if data1 != "":
        main(data1)
    else:
        print("No data1 found")
    if data2 != "":
        main(data2)
    else:
        print("No data2 found")