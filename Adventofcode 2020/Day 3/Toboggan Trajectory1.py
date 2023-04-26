import sys
sys.path.insert(0, '.')
from tools import log

def parse_data(data):
    return [x for x in data.splitlines()]

@log
def main(data):
    data = parse_data(data)


    j = 0
    count = 0
    for i in range(len(data)):
        if data[i][j%len(data[0])] == "#":
            count += 1

        j += 3
    
    return count


data1 = open("./Day 3/data1", "r").read()
data2 = open("./Day 3/data2", "r").read()

main(data1)
main(data2)