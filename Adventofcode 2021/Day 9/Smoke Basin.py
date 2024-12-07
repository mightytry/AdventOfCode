import sys, itertools

from numpy import equal
sys.path.insert(0, '.')
from tools import log

@log
def main(data):
    global cache
    cache = []
    field = data.split("\n")
    return get_sum(get_lowpoints(field))

    
def get_lowpoints(field):
    global cache

    lowpoints = []
    for row_index in range(len(field)):
        for cell_index in range(len(field[row_index])):
            cache = []
            lowpoints.append(check_border(row_index, cell_index, field))

    return lowpoints

def get_sum(lowpoints):
    lowpoints = sorted(lowpoints)
    print(lowpoints)
    return lowpoints[-1]*lowpoints[-2]*lowpoints[-3]


def check_border(row_index, cell_index, field):
    global cache

    cell = int(field[row_index][cell_index])

    size = 1

    if cell == 9:
        return 0

    if ((row_index, cell_index) in cache):
        return 1

    cache.append((row_index, cell_index))



    for loc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        y = row_index + loc[0]
        x = cell_index + loc[1]

        if (x >= 0 and y >= 0 and y < len(field) and x < len(field[y])):
            neighbour = int(field[y][x])

            if (cell+1 == neighbour or cell-1 == neighbour) and neighbour < 9:
                
                size += check_border(y, x, field)

    return size

"""
1236173
4793126
3472850
1345605
"""
    

data1 = open("./Day 9/data1", "r").read()
data2 = open("./Day 9/data2", "r").read()

main(data1)
main(data2)