import sys
sys.path.insert(0, '.')
from tools import log


class Seed():
    def __init__(self, value) -> None:
        self.value = value
        self.child = None

    def get_end(self):
        return self.child.get_rec_value(self.value)

class Map():
    def __init__(self, name, parent) -> None:
        self.name = name
        self.parent = parent
        self.children = None
        self.ranges = []

    def add_range(self, child):
        self.ranges.append(child)

    def get_rec_value(self, value):
        if self.children == None:
            return self.get_value(value)
        else:
            return self.children.get_rec_value(self.get_value(value))

    def get_value(self, value):
        for i in self.ranges:
            if (x := i.try_map(value)) != None:
                return x
        return value

    

class Range():
    def __init__(self, dest_start, src_start, len) -> None:
        self.src_start = src_start
        self.dest_start = dest_start
        self.len = len

    @property
    def range(self):
        return range(self.src_start, self.src_start + self.len)
    
    def try_map(self, value):
        if value in self.range:
            return self.dest_start + (value - self.src_start)
        return None


def parse_data(data):
    seeds = []
    maps = []
    prev = None
    for line in data.split("\n\n"):
        if line.__contains__("seeds:"):
            seeds = [Seed(int(x)) for x in line.split("seeds: ")[1].split(" ")]
            continue
        line = line.split("\n")
        from_map, to_map = line[0].split("-")[0], line[0].split("-")[2]
        maps.append(Map(to_map, prev))
        if prev:
            prev.children = maps[-1]
        prev = maps[-1]
        for i in line[1:]:
            maps[-1].add_range(Range(*[int(x) for x in i.split(" ")]))
    
    for seed in seeds:
        seed.child = maps[0]

    return seeds, maps

@log
def main(data):
    data = parse_data(data)

    return min([x.get_end() for x in data[0]])




if __name__ == "__main__":
    data1 = open("./Day 5/data1", "r").read()
    data2 = open("./Day 5/data2", "r").read()

    if data1 != "":
        main(data1)
    else:
        print("No data1 found")
    if data2 != "":
        main(data2)
    else:
        print("No data2 found")