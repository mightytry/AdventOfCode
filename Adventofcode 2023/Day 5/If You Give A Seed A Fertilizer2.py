import sys
import time
sys.path.insert(0, '.')
from tools import log



class Map():
    def __init__(self, name, parent) -> None:
        self.name = name
        self.parent = parent
        self.children = None
        self.ranges = []

    def add_range(self, child):
        self.ranges.append(child)  
        self.ranges.sort(key=lambda x: x.src_start)

    def eval(self, r = None):
        result = []
        rangs = []
        for n, k in enumerate(self.ranges):
            rang = range(max(k.src_start, r.start), min(k.src_stop, r.stop)) if r else k.dest_range

            if not (rang.start < rang.stop): continue
            rangs.append(rang)
            if self.children:
                result.extend(self.children.eval(k.try_map_range(rang)))
            else:
                result.append(k.try_map_range(rang))

        if r:
            rangs.sort(key=lambda x: x.start)
            s = r.start
            calc = []
            for i in rangs:
                if i.start > s:
                    calc.append(range(s, i.start))
                s = i.stop
            if s < r.stop:
                calc.append(range(s, r.stop))

            for i in calc:
                if self.children:
                    result.extend(self.children.eval(i))
                else:
                    result.append(i)

        return result

    def get_value(self, value):
        for i in self.ranges:
            if (x := i.try_map(value)) != None:
                return x
        return value

    

class Range():
    def __init__(self, dest_start, src_start, len) -> None:
        self.src_start = src_start
        self.dest_start = dest_start
        self.src_stop = src_start + len
        self.dest_stop = dest_start + len
        self.intersections = []
        self.len = len

    @property
    def range(self):
        return range(self.src_start, self.src_stop)

    @property
    def dest_range(self):
        return range(self.dest_start, self.dest_stop)

    
    def try_map(self, value):
        if value in self.range:
            return self.dest_start + (value - self.src_start)
        return None

    def try_map_range(self, r):
        if r.start in self.range and r.stop-1 in self.range:
            return range(self.dest_start + (r.start - self.src_start), self.dest_start + (r.stop - self.src_start))
        return None

    def __repr__(self) -> str:
        return f'"{self.dest_start} {self.src_start} {self.len}"'
    
    def __str__(self) -> str:
        return self.__repr__()


def parse_data(data):
    maps = []
    prev = None
    for line in data.split("\n\n"):
        if line.__contains__("seeds:"):
            seedsd = line.split("seeds: ")[1].split(" ")
            map = Map("seeds", None)
            maps.append(map)
            prev = map
            for seed in range(0, len(seedsd), 2):
                map.add_range(Range(int(seedsd[seed]), int(seedsd[seed]), int(seedsd[seed + 1])))
            continue
        line = line.split("\n")
        from_map, to_map = line[0].split("-")[0], line[0].split("-")[2]
        maps.append(Map(to_map, prev))
        if prev:
            prev.children = maps[-1]
        prev = maps[-1]
        for i in line[1:]:
            maps[-1].add_range(Range(*[int(x) for x in i.split(" ")]))

    # for map in maps[1:]:
    #     map.ranges.append(Range(0, 0, min([x.src_start for x in map.ranges])))

    return maps

@log
def main(data):
    data = parse_data(data)

    return min(data[0].eval(), key=lambda x: x.start).start




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