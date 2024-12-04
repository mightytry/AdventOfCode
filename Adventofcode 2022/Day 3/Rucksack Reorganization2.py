import sys
sys.path.insert(0, '.')
from tools import log

class Rucksack:
    def __init__(self, c1, c2, c3):
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.common = set()
        self.solve()

    def solve(self):
        self.common = list(set(self.c1).intersection(self.c2, self.c3))

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
    data = data.splitlines()

    for step in range(0, len(data),3):
        rucksack = Rucksack(data[step],data[step+1],data[step+2])
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