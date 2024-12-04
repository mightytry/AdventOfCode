import sys
sys.path.insert(0, '.')
from tools import log

def parse_data(data):
    return data

@log
def main(data):
    data = parse_data(data)

    floor = 0

    for n, i in enumerate(data):
        if i == "(":
            floor += 1
        elif i == ")":
            floor -= 1

        if floor == -1:
            return n +1




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