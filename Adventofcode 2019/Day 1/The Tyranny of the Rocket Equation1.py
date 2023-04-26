import sys
sys.path.insert(0, '.')
from tools import log

def parse_data(data):
    return [int(x) for x in data.splitlines()]

@log
def main(data):
    data = parse_data(data)
    
    c = 0
    for fuel in data:
        while fuel > 0:
            fuel = fuel//3-2
            if fuel > 0:
                c += fuel

    return c



if __name__ == "__main__":
    data1 = open("./Day 1/data1", "r").read()
    data2 = open("./Day 1/data2", "r").read()

    if data1 != "":
        main(data1)
    else:
        print("No data1 found")
    if data2 != "":
        main(data2)
    else:
        print("No data2 found")