import sys
sys.path.insert(0, '.')
from tools import log, timer

class Node():
    def __init__(self, code, left, right) -> None:
        self.code = code
        self.left = left
        self.right = right

    def go_left(self):
        return self.left
    
    def go_right(self):
        return self.right

    def __repr__(self) -> str:
        return f"{self.code} ({self.left.code}, {self.right.code})"

    def __str__(self) -> str:
        return self.__repr__()

def parse_data(data):
    data = data.split("\n\n")

    way = data[0]
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
        
    return way, nodes, next(filter(lambda x: x.code == "AAA", nodes.values())), next(filter(lambda x: x.code == "ZZZ", nodes.values()))

@log
@timer
def main(data):
    way, nodes, start, end = parse_data(data)

    i = 0
    while start != end:
        if way[i%len(way)] == "L":
            start = start.go_left()
        else:
            start = start.go_right()
        #print(i%len(way), start, end)
        i += 1


    return i




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