import sys
sys.path.insert(0, '.')
from tools import log, timer

class List():
    def __init__(self, data) -> None:
        self.data = sorted(data)

    def __sub__(self, other):
        return sum([abs(x-y) for x, y in zip(self.data, other.data)])
    

def parse_data(data):
    l1 = List(map(int, map(lambda l:l.split("   ")[0],data.splitlines())))
    l2 = List(map(int, map(lambda l:l.split("   ")[1],data.splitlines())))
    return l1, l2

@log
def main(data):
    data = parse_data(data)
    sim = 0

    return data[0] - data[1]




if __name__ == "__main__":
    data1 = open("./Day 1/data1", "r").read()
    data2 = open("./Day 1/data2", "r").read()

    if data1 != "":
        main(data1)
    else:
        print("No data1 found")
    if data2 != "":
        main(data2)
    else:
        print("No data2 found")