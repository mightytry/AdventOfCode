import sys, functools, copy
sys.path.insert(0, '.')
from tools import log, timer


class Direction:
    NORTH = 0
    SOUTH = 1
    EAST = 2
    WEST = 3


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


def full_spin(grid):
    return spin(spin(spin(spin(grid, Direction.NORTH), Direction.EAST), Direction.SOUTH), Direction.WEST)


def parse_data(data):
    grid = [list(line) for line in data.split("\n")]

    return grid

def hash(grid):
    return "".join("".join(g) for g in grid)

@log
@timer
def main(data):
    grid = parse_data(data)
    D = [hash(grid)]

    # for x in range(100):
    #     grid = full_spin(grid)
    #     a.append(sum([row.count("O")*(len(grid)-i) for i, row in enumerate(grid)]))

    c = 0
    d = 0
    while True:
        grid = full_spin(grid)
        c += 1
        h = hash(grid)
        if h in D:
            break
        D.append(h)

    print(c, D.index(hash(grid)))

    for d in range((1000000000-c)%(c-D.index(hash(grid)))):
        grid = full_spin(grid)

    #return "\n".join("".join(g) for g in spin(grid, Direction.WEST))
    return sum([row.count("O")*(len(grid)-i) for i, row in enumerate(grid)])




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