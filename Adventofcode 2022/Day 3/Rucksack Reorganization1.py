import sys
sys.path.insert(0, '.')
from tools import log

class Rucksack:
    def __init__(self, data):
        self.data = data
        self.c1 = []
        self.c2 = []
        self.common = set()
        self.solve()

    def solve(self):
        l = len(self.data)
        self.c1 = self.data[:l//2]
        self.c2 = self.data[l//2:]
        self.common = list(set(self.c1).intersection(set(self.c2)))

    @property
    def priority(self):
        v = 0
        for x in self.common:
            if x.isupper():
                v += ord(x)-ord('A')+27
            else:
                v += ord(x)-ord('a') + 1
        return v

def parse_data(data):
    rucksacks = []

    for line in data.splitlines():
        rucksack = Rucksack(line)
        rucksacks.append(rucksack)
        
    return rucksacks

@log
def main(data):
    data = parse_data(data)
    v = 0

    for rucksack in data:
        v += rucksack.priority

    return v


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