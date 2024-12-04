import sys
sys.path.insert(0, '.')
from tools import log


def parse_data(data):
    return list(map(int, data.split(",")))


@log
def main(data):
    data = parse_data(data)

    data[1] = 12
    data[2] = 2

    i = 0
    while (True):
        if data[i] == 1:
            data[data[i+3]] = data[data[i+1]] + data[data[i+2]]
        elif data[i] == 2:
            data[data[i+3]] = data[data[i+1]] * data[data[i+2]]
        else:
            break
        i += 4

    return data[0]


if __name__ == "__main__":
    data1 = open("./Day 2/data1", "r").read()
    data2 = open("./Day 2/data2", "r").read()

    if data1 != "":
        main(data1)
    else:
        print("No data1 found")
    if data2 != "":
        main(data2)
    else:
        print("No data2 found")
