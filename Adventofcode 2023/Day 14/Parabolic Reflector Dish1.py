import sys
sys.path.insert(0, '.')
from tools import log, timer



def parse_data(data):
    grid = [list(line) for line in data.split("\n")]

    return grid

@log
@timer
def main(data):
    grid = parse_data(data)

    grids = list(zip(*grid))

    for x, row in enumerate(grids):
        l = 0
        for y, tile in enumerate(row):
            match tile:
                case "#":
                    l = y+1
                case "O":
                    grid[l][x] = "O"
                    if l != y:
                        grid[y][x] = "."
                    l += 1

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