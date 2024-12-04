import sys, math, time, copy
sys.path.insert(0, '.')
from tools import log, timer

class Node():
    SEQUENCE = None
    SEQUENCE_LEN = None

    def __init__(self, code, left, right) -> None:
        self.code = code
        self.left = left
        self.right = right
        self.i = 0
        self.next = self

    def calc(self):
        self.next = self.next.left if self.SEQUENCE[self.i%self.SEQUENCE_LEN] == "L" else self.next.right
        self.i += 1

        if self.next.code[2] == "Z":
            return False
        return True

    def __repr__(self) -> str:
        return f"{self.code} ({self.left.code}, {self.right.code}, {self.i})"

    def __str__(self) -> str:
        return self.__repr__()


def parse_data(data):
    data = data.split("\n\n")

    way = data[0]
    Node.SEQUENCE = way
    Node.SEQUENCE_LEN = len(way)
    nodes = {}
    for x in data[1].splitlines():
        if x == "": continue
        d = x.split(" = (")
        code = d[0]
        left = d[1].split(", ")[0]
        right = d[1].split(", ")[1][:-1]
        nodes[code] = Node(code, left, right)
    
    for node in nodes.values():
        node.left = nodes[node.left]
        node.right = nodes[node.right]
        
    return list(filter(lambda x: x.code[2] == "A", nodes.values()))


@log
def main(data):
    start = parse_data(data)
    mart = copy.copy(start)

    while mart != []:
        for x in mart:
            if not x.calc():
                mart.remove(x)

    return math.lcm(*map(lambda x: x.i, start))




if __name__ == "__main__":
    data1 = open("./Day 8/data1", "r").read()
    data2 = open("./Day 8/data2", "r").read()

    if data1 != "":
        main(data1)
    else:
        print("No data1 found")
    if data2 != "":
        main(data2)
    else:
        print("No data2 found")