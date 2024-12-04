import sys
sys.path.insert(0, '.')
from tools import log

class Elve:
    def __init__(self, section):
        self.data = section
        self.section:range = None
        self.solve()

    def solve(self):
        d = self.data.split("-")
        self.section = range(int(d[0]), int(d[1])+1)

class Pair:
    def __init__(self, data):
        self.data = data
        self.elve1:Elve = None
        self.elve2:Elve = None
        self.solve()

    def solve(self):
        d = self.data.split(",")
        self.elve1 = Elve(d[0])
        self.elve2 = Elve(d[1])
            
    @property
    def contains(self):
        if any(i in self.elve1.section for i in self.elve2.section) or any(i in self.elve2.section for i in self.elve1.section):
            return True
        return False


def parse_data(data):
    pairs = []
    for line in data.splitlines():
        pair = Pair(line)
        pairs.append(pair)
    return pairs

@log
def main(data):
    data = parse_data(data)

    count = 0

    for pair in data:
        if pair.contains:
            count += 1
    
    return count




if __name__ == "__main__":
    data1 = open("./Day 4/data1", "r").read()
    data2 = open("./Day 4/data2", "r").read()

    if data1 != "":
        main(data1)
    else:
        print("No data1 found")
    if data2 != "":
        main(data2)
    else:
        print("No data2 found")