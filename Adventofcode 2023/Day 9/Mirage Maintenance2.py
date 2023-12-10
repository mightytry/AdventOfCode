import sys
sys.path.insert(0, '.')
from tools import log, timer


class History():
    def __init__(self, values) -> None:
        self.values = values

    def get_last(self):
        return self.get_last_r(self.values)

    def get_last_r(self, row):
        if all((x == row[0] for x in row)):
            return row[0]
        else:
            return row[0] - self.get_last_r([(row[x+1] - row[x]) for x in range(len(row)-1)])
        
    def get_next_row(self, row, len):
        s = next(row)
        for x in range(len(row)-1):
            x = next(row)
            yield x - s
            s = x

    def __str__(self) -> str:
        return " ".join(self.values)
    
    def __repr__(self) -> str:
        return self.__str__()
    

def parse_data(data):
    return [History([int(y) for y in x.split(" ")]) for x in data.split("\n")]

@log
def main(data):
    data = parse_data(data)

    return sum((x.get_last()) for x in data)




if __name__ == "__main__":
    data1 = open("./Day 9/data1", "r").read()
    data2 = open("./Day 9/data2", "r").read()

    if data1 != "":
        main(data1)
    else:
        print("No data1 found")
    if data2 != "":
        main(data2)
    else:
        print("No data2 found")