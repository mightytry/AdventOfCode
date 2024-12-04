import copy
import sys
import timeit
sys.path.insert(0, '.')
from tools import log

class Part:    
    class Type:
        ADD = 0
        SUB = 1

    def __init__(self, type, n) -> None:
        self.type = type
        self.n = n

    def gen(self, parts, z, i):
        if (z := self.eval(z, i)) is False:
            return False
        if len(parts) == 0:

            if z == 0:
                return []
            else:
                return False
        parts = copy.deepcopy(parts)
        
        e = parts.pop(0)
        for g in range(1, 10, 1):
            if (r := e.gen(parts, z, g)) != False:
                r.append(g)
                return r
        
        return False

    def eval(self, z, i):
        match self.type:
            case Part.Type.ADD:
                z = z *26 + self.n + i
            case Part.Type.SUB:
                if z % 26 + self.n == i:
                    z //= 26
                else:
                    return False
                
        return z

    def __repr__(self) -> str:
        return f"Part({self.type}, {self.n})"
    
    def __str__(self) -> str:
        return repr(self)
    
def parse_data(data) -> list[Part]:
    ONT1 = 15
    ONT2 = 5
    parts = []
    data = data.split("\n")
    for n, line in enumerate(data):
        if "inp" in line:
            if "-" in data[n+ONT2]:
                parts.append(Part(Part.Type.SUB, int(data[n+ONT2].split(" ")[-1])))
            else:
                parts.append(Part(Part.Type.ADD, int(data[n+ONT1].split(" ")[-1])))

    return parts



@log
def main(data):
    data = parse_data(data)

    p = data.pop(0)
    for i in range(1, 10, 1):
        if (r := p.gen(data, 0, i)) != False:
            r.append(i)
            return "".join(map(str,reversed(r)))


if __name__ == "__main__":
    data1 = open("./Day 24/data1", "r").read()
    data2 = open("./Day 24/data2", "r").read()

    if data1 != "":
        main(data1)
    else:
        print("No data1 found")
    if data2 != "":
        main(data2)
    else:
        print("No data2 found")