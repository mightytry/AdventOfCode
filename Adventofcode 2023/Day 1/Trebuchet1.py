import sys
sys.path.insert(0, '.')
from tools import log

def parse_data(data:str):
    return map(lambda x: list(filter(lambda y: y.isdigit(), x)), data.splitlines())

@log
def main(data):
    data = parse_data(data)
    return sum(map(lambda x: int(x[0] +x[-1]), data))




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