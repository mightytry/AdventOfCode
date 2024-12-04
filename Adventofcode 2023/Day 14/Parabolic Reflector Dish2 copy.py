import sys, functools, copy, timeit
sys.path.insert(0, '.')
from tools import log, timer
from collections import Counter


class Direction:
    NORTH = 0
    SOUTH = 1
    EAST = 2
    WEST = 3


def spin2(grid):
    # transpose
    grid = list(map("".join, zip(*grid)))

    new_grid = []

    for row in grid:
        ordered_rows = []
        for group in row.split("#"):
            ordered_rows.append("O"*(o := group.count("O"))+ "."*(len(group)-o) )

        new_grid.append("#".join(ordered_rows))

    return tuple(list(map("".join, zip(*new_grid))))


def spin(grid, direction):
    grids = grid
    if direction < Direction.EAST:
        grids = list(zip(*grid))
    reverse = direction%2 == 1

    for x, row in enumerate(grids):
        l = 0
        for y, tile in enumerate(reversed(row) if reverse else row):
            match tile:
                case "#":
                    l = y+1
                case "O":
                    if l == y: 
                        l += 1
                        continue 
                    ln = l
                    if reverse:
                        r = len(row)
                        y = r-y-1
                        ln = r-l-1
                    
                    if direction < Direction.EAST:
                        grid[ln][x] = "O"
                        grid[y][x] = "."
                    else:
                        grid[x][ln] = "O"
                        grid[x][y] = "."
                    l += 1

    return grid


def spin3(hori_qubic, hori_qubics, qubics, qubic, round):
    # north
    for q in hori_qubics:
        q.next_free_pos = q.y+1
    for r in round:
        q = hori_qubics[hori_qubic[r.x][r.y]]
        r.y = q.next_free_pos
        q.next_free_pos += 1

    
    # west
    for q in qubics:
        q.next_free_pos = q.x+1
    
    for r in round:
        q = qubics[qubic[r.y][r.x]]
        r.x = q.next_free_pos
        q.next_free_pos += 1

    # south
    for q in hori_qubics:
        q.next_free_pos = q.y-1
    for r in round:
        q = hori_qubics[hori_qubic[r.x][r.y]+1]
        r.y = q.next_free_pos
        q.next_free_pos -= 1


    # east
    for q in qubics:
        q.next_free_pos = q.x-1

    for r in round:
        q = qubics[qubic[r.y][r.x]+1]
        r.x = q.next_free_pos
        q.next_free_pos -= 1

def debug(round, grid):
    x = y = 0
    grid = [["." for i in row] for row in grid]
    for r in round:
        grid[r.y][r.x] = "O"
    return ("\n".join("".join(row) for row in grid))


def full_spin(grid):
    return spin(spin(spin(spin(grid, Direction.NORTH), Direction.EAST), Direction.SOUTH), Direction.WEST)


class QubicStone:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.next_free_pos = None  

    def __repr__(self):
        return str(self.x)
    
class RoundStone:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return str(self.x)
    
    def __iter__(self):
        return (self.x, self.y).__iter__()
    
    def __hash__(self):
        return (self.x, self.y)

def parse_data(data):
    grid = [list(line) for line in data.split("\n")]

    qubic = []
    qubics = []
    lens = 0
    for y, row in enumerate(grid):
        qubic.append([])
        qubics.append(QubicStone(-1, y))
        lens += 1
        for x, tile in enumerate(row):
            if tile == "#":
                qubics.append(QubicStone(x, y))
                lens += 1
            qubic[-1].append(lens-1)
        qubics.append(QubicStone(len(row), y))
        lens += 1

    grids = list(zip(*grid))

    hori_qubic = []
    hori_qubics = []
    lens = 0
    for x, row in enumerate(grids):
        hori_qubic.append([])
        hori_qubics.append(QubicStone(x, -1))
        lens += 1
        for y, tile in enumerate(row):
            if tile == "#":
                hori_qubics.append(QubicStone(x, y))
                lens += 1
            hori_qubic[-1].append(lens-1)
        hori_qubics.append(QubicStone(x, len(row)))
        lens += 1

    return hori_qubic, hori_qubics, qubics, tuple(qubic), tuple(RoundStone(x, y) for y, row in enumerate(grid) for x, tile in enumerate(row) if tile == "O")

def hash(grid):
    return set(row.__hash__() for row in grid)


@log
@timer
def main(data):
    hori_qubic, hori_qubics, qubics, qubic, round = parse_data(data)

    c = 0
    D = [hash(round)]
    while True:
        spin3(hori_qubic, hori_qubics, qubics, qubic, round)
        c += 1
        if hash(round) in D:
            break
        D.append(hash(round))

    for d in range((1000000000-c)%(c-D.index(hash(round)))):
        spin3(hori_qubic, hori_qubics, qubics, qubic, round)

    #return "\n".join("".join(g) for g in spin(grid, Direction.WEST))
    return sum(len(qubic)-r.y for r in round)




if __name__ == "__main__":
    data1 = open("./Day 14/data1", "r").read()
    data2 = open("./Day 14/data2", "r").read()

    if data1 != "":
        main(data1)
    else:
        print("No data1 found")
    if data2 != "":
        main(data2)
    else:
        print("No data2 found")