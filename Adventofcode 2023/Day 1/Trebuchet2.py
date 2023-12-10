import sys
sys.path.insert(0, '.')
from tools import log

class Index():
    def __init__(self, index, val) -> None:
        self.index = index
        self.val = val

    def check_smaller(self, i, num):
        if (i < self.index):
            self.index = i
            self.val = num
    
    def check_bigger(self, i, num):
        if (i > self.index):
            self.index = i
            self.val = num

    def __repr__(self) -> str:
        return f"({self.index}, {self.val})"

def parse_data(data:str):
    nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
    erg = []

    for line in data.splitlines():
        erg.append((Index(len(line), None), Index(-1, None)))
        for c, num in enumerate(nums):
            if (line.__contains__(num)):
                erg[-1][0].check_smaller(line.index(num), str(c+1))
                erg[-1][1].check_bigger(line.rindex(num), str(c+1))

        for i, c in enumerate(line):
            if (c.isdigit()):
                erg[-1][0].check_smaller(i, c)
                erg[-1][1].check_bigger(i, c)

    return erg

@log
def main(data):
    data = parse_data(data)

    return sum(map(lambda x: int(x[0].val +x[1].val), data))




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