import sys
from functools import cache
sys.path.insert(0, '.')
from tools import log

class Vector3():
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Vector3):
            return self.x == o.x and self.y == o.y and self.z == o.z

        return False
    
    def __hash__(self) -> int:
        return hash((self.x, self.y, self.z))
    
    def __repr__(self) -> str:
        return f'Vector3({self.x}, {self.y}, {self.z}, {self.state})'

class Cube():
    def __init__(self, state, child, from_x, to_x, from_y, to_y, from_z, to_z) -> None:
        self.x = range(from_x, to_x+1)
        self.y = range(from_y, to_y+1)
        self.z = range(from_z, to_z+1)
        self.state = state
        self.child = child

    def __contains__(self, o: object) -> bool:
        if isinstance(o, Vector3):
            return o.x in self.x and o.y in self.y and o.z in self.z
        if isinstance(o, Cube):
            return o.x in self.x and o.y in self.y and o.z in self.z

    def __iter__(self):
        for x in self.x:
            for y in self.y:
                for z in self.z:
                    v = Vector3(x, y, z)
                    yield v

    def __repr__(self) -> str:
        return f'Cube({self.x}, {self.y}, {self.z}, {self.state})'
        


def parse_data(data):
    cubes = []
    data = data.split("\n")
    child = None
    for line in reversed(data):
        val = line.split(" ")
        state = True if val[0] == "on" else False
        line = val[1]
        line = [x.split("=")[1] for x in line.split(",")]
        line = [x.split("..") for x in line]
        c = Cube(state, child, *map(int, line[0]), *map(int, line[1]), *map(int, line[2]))
        if c.x.start >= -50 and c.x.stop <= 51 and c.y.start >= -50 and c.y.stop <= 51 and c.z.start >= -50 and c.z.stop <= 51:
            cubes.append(c)
            child = c
   
    return cubes

@log
def main(data):
    data = parse_data(data)

    v = {}
    for i in reversed(data):
        for x in i:
            v[x] = i.state

    return sum(v.values())




if __name__ == "__main__":
    data1 = open("./Day 22/data1", "r").read()
    data2 = open("./Day 22/data2", "r").read()

    if data1 != "":
        main(data1)
    else:
        print("No data1 found")
    if data2 != "":
        main(data2)
    else:
        print("No data2 found")