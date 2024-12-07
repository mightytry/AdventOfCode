import sys
sys.path.insert(0, '.')
from tools import log

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

def parse_data(data):
    return [x for x in data.splitlines()]

@log
def main(data):
    data = parse_data(data)
   
    erg = 1
    for r, d in slopes:
        count = 0
        j = 0

        for i in range(0, len(data), d):
            if data[i][j%len(data[0])] == "#":
                count += 1

            j += r

        erg *= count

    return erg


data1 = open("./Day 3/data1", "r").read()
data2 = open("./Day 3/data2", "r").read()

main(data1)
main(data2)