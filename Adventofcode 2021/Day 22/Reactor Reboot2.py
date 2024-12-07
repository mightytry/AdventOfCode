import sys
from functools import cache
import timeit
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
        self.intersections = []
        self.name = 0

    def __contains__(self, o: object) -> bool:
        if isinstance(o, Vector3):
            return o.x in self.x and o.y in self.y and o.z in self.z
        if isinstance(o, Cube):
            return o.x in self.x and o.y in self.y and o.z in self.z
        
    def __eq__(self, o: object) -> bool:
        if isinstance(o, Cube):
            return self.x == o.x and self.y == o.y and self.z == o.z

        return False
    
    def __hash__(self) -> int:
        return hash(self.name)

  
    def get_on(self):
        if self.intersections == []:
            return len(self.x)*len(self.y)*len(self.z) if self.state else 0
        
        res = len(self.x)*len(self.y)*len(self.z) if self.state else 0
        for inter in self.intersections:
            if self.state:
                res -= inter.get_on()
            elif not self.state:
                res += inter.get_on()

        return res * -1 if not self.state else res
        
    def intersection(self, o):
        if isinstance(o, Cube):
            x ,y ,z = None, None, None
            if self.x.start < o.x.stop and o.x.start < self.x.stop:
                x = range(max(self.x.start, o.x.start), min(self.x.stop, o.x.stop))
            if self.y.start < o.y.stop and o.y.start < self.y.stop:
                y = range(max(self.y.start, o.y.start), min(self.y.stop, o.y.stop))
            if self.z.start < o.z.stop and o.z.start < self.z.stop:
                z = range(max(self.z.start, o.z.start), min(self.z.stop, o.z.stop))
            
            if not x or not y or not z:
                return None
            c = Cube(o.state, o, min(x), max(x), min(y), max(y), min(z), max(z))
            
            for i in self.intersections:
                i.intersection(c)
            self.intersections.append(c)

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
    for num, line in enumerate(reversed(data)):
        val = line.split(" ")
        state = True if val[0] == "on" else False
        line = val[1]
        line = [x.split("=")[1] for x in line.split(",")]
        line = [x.split("..") for x in line]
        c = Cube(state, child, *map(int, line[0]), *map(int, line[1]), *map(int, line[2]))
        cubes.append(c)
        c.name = num
        child = c
   
    return cubes

@log
def main(data):
    data = parse_data(data)

    pro = []
    for i in reversed(data):
        for j in reversed(pro):
            i.intersection(j)        
        pro.append(i)

    return sum([x.get_on() for x in pro])




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