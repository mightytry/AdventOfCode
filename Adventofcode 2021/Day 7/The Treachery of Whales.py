import sys
sys.path.insert(0, '.')
from tools import log


def arverage(crabs):
    bps = 0
    fuelbps = 10000000000000000000
    for x in range(1000):
        fuel = get_fuel(crabs, x)
        if fuel < fuelbps:
            bps = x
            fuelbps = fuel
    return bps

@log
def main(data):
    crabs = return_data(data)
    return get_fuel(crabs, arverage(crabs))

def get_fuel(crabs, average):
    fuel = 0
    
    for crab in crabs:
        a = (int(crab) - average if int(crab) - average >= 0 else average - int(crab))
        b = 0
        for x in range(a+1):
            b += x
        fuel += b

    return fuel

def return_data(data):
    return data.split(',')


data1 = open("./Day 7/data1", "r").read()
data2 = open("./Day 7/data2", "r").read()

main(data1)
main(data2)