import sys
sys.path.insert(0, '.')
from tools import log

#465 bei benni -> fix

class Rotation:
    def __init__(self, x, y, z ,n) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.n = n

    def __mul__(self, o: object) -> object:
        if isinstance(o, Vector3):
            return self.rotate(self.x * o.x, self.y * o.y, self.z * o.z, self.n)
        if isinstance(o, Rotation):
            return self.rotate(self.x * o.x, self.y * o.y, self.z * o.z, o.n)
    
    # divide not used
    def __truediv__(self, o: object) -> object:
        if isinstance(o, Vector3):
            v = self.reverse_rotate(*o, self.n)
            return Vector3(v.x * self.x, v.y * self.y, v.z * self.z)

    def rotate(self, _x, _y, _z, n):
        match (n):
            case 0:
                return Vector3(_x, _y, _z)
            case 1:
                return Vector3(_y, _x, _z)
            case 2:
                return Vector3(_z, _y, _x)
            case 3:
                return Vector3(_x, _z, _y)
            case 4:
                return Vector3(_y, _z, _x) 
            case 5:
                return Vector3(_z, _x, _y)
    
    # reverse_rotate not used
    def reverse_rotate(self, _x, _y, _z, n): # problem here
        match (n):
            case 0:
                return Vector3(_x, _y, _z)
            case 1:
                return Vector3(_y, _x, _z)
            case 2:
                return Vector3(_z, _y, _x)
            case 3:
                return Vector3(_x, _z, _y)
            case 4:
                return Vector3(_z, _x, _y)
            case 5:
                return Vector3(_y, _z, _x)

    def __repr__(self) -> str:
        return f'Rotation({self.x}, {self.y}, {self.z}, {self.n})'

class Vector3():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return str((self.x, self.y, self.z))

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Vector3):
            return self.x == o.x and self.y == o.y and self.z == o.z
        return False

    def __add__(self, o: object) -> object:
        if isinstance(o, Vector3):
            return Vector3(self.x + o.x, self.y + o.y, self.z + o.z)

    def __sub__(self, o: object) -> object:
        if isinstance(o, Vector3):
            return Vector3(self.x - o.x, self.y - o.y, self.z - o.z)

    def __mul__(self, o: object) -> object:
        if isinstance(o, Vector3):
            return Vector3(self.x * o.x, self.y * o.y, self.z * o.z)
        if isinstance(o, int):
            return Vector3(self.x * o, self.y * o, self.z * o)
        if isinstance(o, Rotation):
            return o * self

    def __div__(self, o: object) -> object:
        if isinstance(o, Vector3):
            return Vector3(self.x / o.x, self.y / o.y, self.z / o.z)
        if isinstance(o, int):
            return Vector3(self.x / o, self.y / o, self.z / o)
        if isinstance(o, Rotation):
            return o / self

    def __sub__(self, o: object) -> object:
        if isinstance(o, Vector3):
            return Vector3(self.x - o.x, self.y - o.y, self.z - o.z)

    def __hash__(self) -> int:
        return hash((self.x, self.y, self.z))

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z

class Position():
    def __init__(self, start, beacons, scanner):
        self.start = start
        self.scanner = scanner
        self.beacons = beacons
        self.intersect = {}
        self.positons = []
        self.gen_positions(start, beacons)

    def gen_positions(self, start, beacons):
        for beacon in beacons:
            b, m, s = sorted((abs(beacon.pos.x- start.pos.x), abs(beacon.pos.y - start.pos.y), abs(beacon.pos.z - start.pos.z))) #here is a problem !WRONG!
            self.positons.append(Vector3(b, m, s))

    def diff(self, other):
        self.intersect = set(self.positons).intersection(other.positons)

        return len(self.intersect)

    def __repr__(self):
        return str(self.positons)

class Link:
    def __init__(self, pos1, pos2) -> None:
        self.pos1 = pos1
        self.pos2 = pos2

    def get_relative(self, scanner):
        b1 = self.pos1 if self.pos1.scanner is scanner else self.pos2
        b2 = self.pos2 if self.pos1.scanner is scanner else self.pos1
        #vom s1 muss der start beacon die gleiche distanc zu einem beacon haben wie beim anderen scanner der start beacon zu dem beacon (s2 solange drehen bis es passt)
        #die beacons bekommt man indem man schaut wo in der positons liste der beacon mit der position bei beiden scannern ist und dann den beacon daraus nimmt
        pos = list(b1.intersect)[0]
        start = b2.start.pos
        beacon2 = b2.beacons[b2.positons.index(pos)]
        beacon1 = b1.beacons[b1.positons.index(pos)]
        pos = beacon1.pos - b1.start.pos
        pos2 = beacon2.pos - b2.start.pos
        

        for o in ((1, 1, 1), (1, -1, 1), (1, 1, -1), (1, -1, -1), (-1, 1, 1), (-1, -1, 1), (-1, 1, -1), (-1, -1, -1)):
            for n in range(6):
                r = Rotation(o[0], o[1], o[2], n)
                if pos == pos2*r:
                    b2.scanner.rotation = r
                    b2.scanner.parent = b1.scanner
                    b2.scanner.pos = (b1.scanner.pos + b1.scanner.calc(beacon1.pos - r*beacon2.pos)) # the problem was here
                    return


class Positions:
    def __init__(self, beacons, scanner) -> None:
        self.scanner = scanner
        self.positions = []
        self.init_positions(beacons)

    def init_positions(self, beacons):
        for n, beacon in enumerate(beacons):
            self.positions.append(Position(beacon, beacons[n+1:] + beacons[:n], self.scanner))

    def diff(self, other):
        a = []
        for pos1 in self.positions:
            for pos2 in other.positions:
                d = pos1.diff(pos2)
                a.append((d, pos1, pos2))

        a = list(filter(lambda x: x[0] > 10, a))
        if len(a) != 0:
            if a[0][1].diff(a[0][2]) + a[0][2].diff(a[0][1]) == 22:
                return Link(a[0][1], a[0][2])
        

        return None

    def __repr__(self):
        return str(self.positions)

class Beacon:
    def __init__(self, parent, coords):
        self.pos = Vector3(*coords)
        self.apos = None
        self.relative_positions = []
        self.parent = parent

    def __repr__(self) -> str:
        return f"{self.parent, self.pos}"

class Scanner:
    def __init__(self, name, data):
        self.name = name
        self.beacons = list(map(lambda x: Beacon(self, x), data))
        self.positions = Positions(self.beacons, self)
        self.rotation:Rotation = None
        self.pos = Vector3(0,0,0) if self.name == 0 else None
        self.parent = None

    def compare(self, other):
        link = self.positions.diff(other.positions)
        if link:
            distance = link.get_relative(self)

            return distance
        
        return "No link found"

    def calc(self, stuff):
        if self.parent is None:
            return stuff
        else:
            return self.parent.calc(self.rotation*stuff) # and problem here

    def __repr__(self) -> str:
        return "Scanner: "+ (str(self.name) + " " + str(self.pos))
    
    def __iter__(self):
        return iter(self.pos)

class Beacons:
    def __init__(self, data):
        self.scanners = data
        self.beacons = {}
        self.link()

    def link(self):
        beacons = []

        while any(scanner.pos is None for scanner in self.scanners):
            for scanner in self.scanners:
                for other in self.scanners:
                    if scanner == other: continue
                    if other.pos is None and scanner.pos is not None:
                        scanner.compare(other)
        
        for scanner in self.scanners:
            for beacon in scanner.beacons:
                p = self.get_beacon_pos(scanner, beacon)
                beacons.append(p)
        
        self.beacons = set(beacons)

    @staticmethod
    def get_beacon_pos(scanner, beacon):
        b1 = scanner.pos + scanner.calc(beacon.pos)
        return b1# Vector3(b1.x, b2.y, b1.z)
     

def get_manhattan_distance(scanners):
    maxi = 0
    for scanner in scanners:
        for scanner2 in scanners:
            if scanner == scanner2: continue
            maxi = n if (n := sum(map(abs,scanner2.pos - scanner.pos))) > maxi else maxi
    return maxi
     

def parse_data(data:str):
    scanner = []

    for n, line in enumerate(data.split("\n\n")):
        if line == "": continue

        lines = line.split("\n")[1:]

        coords = map(lambda x: map(lambda x: int(x), x.split(",")), lines)

        scanner.append(Scanner(n, coords))

    return scanner

@log
def main(data):
    data = parse_data(data)

    beacons = Beacons(data)

    return get_manhattan_distance(data)



if __name__ == "__main__":
    data1 = open("./Day 19/data1", "r").read()
    data2 = open("./Day 19/data2", "r").read()

    if data1 != "":
        main(data1)
    else:
        print("No data1 found")
    if data2 != "":
        main(data2)
    else:
        print("No data2 found")