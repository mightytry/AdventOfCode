import sys
sys.path.insert(0, '.')
from tools import log, timer

class List():
    def __init__(self, data) -> None:
        self.data = sorted(data)

    def count(self, item):
        return self.data.count(item)
    

def parse_data(data):
    l1 = List(map(int, map(lambda l:l.split("   ")[0],data.splitlines())))
    l2 = List(map(int, map(lambda l:l.split("   ")[1],data.splitlines())))
    return l1, l2

@log
def main(data):
    data = parse_data(data)
    sim = 0
    for x in data[0].data:
        sim += data[1].count(x) * x

    return sim




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