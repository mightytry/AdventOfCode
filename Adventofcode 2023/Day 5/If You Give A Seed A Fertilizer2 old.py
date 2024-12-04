import sys
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

    def eval(self, maps, i = 0):
        if i == len(maps):
            return
        
        for k in maps[i].ranges:
            for j in range(i + 1, len(maps)):
                if len(k.intersections) >= 1 and k.dest_range in k.intersections[-1].values():
                    break
                d = {}
                for l in maps[j].ranges:
                    inter = range(max(k.dest_start, l.src_start), min(k.dest_range.stop, l.range.stop))
                    for x in k.intersections:
                        for y in x.values():
                            inter = range(max(inter.start, y.stop), max(inter.stop, y.start))
                            
                    if inter.start < inter.stop:
                        d[l] = inter
                    if inter == k.dest_range:
                        break
                last = k.dest_start
                for x in sorted(d.keys(), key=lambda x: x.src_start):
                    if x.src_start > last:
                        r = Range(last, last, x.src_start - last)
                        maps[j].add_range(r)
                        d[r] = r.range
                        last = x.src_start
                        continue
                    last = x.src_start + x.len

                k.intersections.append(d)
            
    def get_result_range(self, ra, ranged= None):
        if self.children == None:
            return ra

        ranges = []
        for i in ra.intersections:
            for k, j in i.items():
                ranges.append((j,k, self.children.get_result_range(k, j)))
        return ranges
        
    def print(self, l, ranges = None, old = None):
        if isinstance(l, Range):
            return l
        res = []
        if isinstance(l, list):
            for i in l:
                if ranges == None:
                    res.append(i[0])
                    res.append(self.print(i[2], i[0], i[1]))
                    continue
                leng = min(ranges.stop-ranges.start, i[0].stop-i[0].start)
                rang = range(ranges.start-old.src_start+i[1].src_start, ranges.start-old.src_start+leng+i[1].src_start)
                res.append(rang)
                res.append(self.print(i[2], rang, i[1]))

        return res
        

    

class Range():
    def __init__(self, dest_start, src_start, len) -> None:
        self.src_start = src_start
        self.dest_start = dest_start
        self.intersections = []
        self.len = len

    @property
    def range(self):
        return range(self.src_start, self.src_start + self.len)

    @property
    def dest_range(self):
        return range(self.dest_start, self.dest_start + self.len)

    
    def try_map(self, value):
        if value in self.range:
            return self.dest_start + (value - self.src_start)
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

    for n, map in enumerate(data):
        map.eval(data, n)

    #return data[0].print(data[0].get_result_range(data[0].ranges[0]))

    return [[(y, y.intersections) for y in x.ranges] for x in data[0:]]




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