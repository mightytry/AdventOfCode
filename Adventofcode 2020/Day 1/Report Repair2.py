import sys
sys.path.insert(0, '.')
from tools import log

def get_result(data):
    for i in data:
        for j in data:
            for k in data:
                if i + j + k == 2020:
                    return i * j * k

def parse_data(data):
    return [int(x) for x in data.splitlines()]

@log
def main(data):
    data = parse_data(data)

    return get_result(data)


data1 = open("./Day 1/data1", "r").read()
data2 = open("./Day 1/data2", "r").read()

main(data1)
main(data2)