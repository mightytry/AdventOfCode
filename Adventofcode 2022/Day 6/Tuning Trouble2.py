import sys
sys.path.insert(0, '.')
from tools import log

def parse_data(data):
    return data

def get_truthy(data):
    for i in data:
        if data.count(i) > 1:
            return False

    return True

@log
def main(data):
    data = parse_data(data)
    for i in range(14, len(data)):
        if (get_truthy(data[i-14:i])):
            return i


if __name__ == "__main__":
    data1 = open("./Day 6/data1", "r").read()
    data2 = open("./Day 6/data2", "r").read()

    if data1 != "":
        main(data1)
    else:
        print("No data1 found")
    if data2 != "":
        main(data2)
    else:
        print("No data2 found")