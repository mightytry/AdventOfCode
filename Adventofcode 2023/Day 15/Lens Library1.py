import sys
sys.path.insert(0, '.')
from tools import log, timer

def get_value(char) -> int:
    return ord(char)

def to_num(hash) -> int:
    v = 0
    for char in hash:
        v += get_value(char)
        v*= 17
        v%= 256
    return v

def parse_data(data):
    return data.split(",")

@timer
@log
def main(data):
    data = parse_data(data)

    return sum(to_num(i) for i in data)




if __name__ == "__main__":
    data1 = open("./Day 15/data1", "r").read()
    data2 = open("./Day 15/data2", "r").read()

    if data1 != "":
        main(data1)
    else:
        print("No data1 found")
    if data2 != "":
        main(data2)
    else:
        print("No data2 found")