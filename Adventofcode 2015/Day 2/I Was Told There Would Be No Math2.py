import sys
sys.path.insert(0, '.')
from tools import log

class Box():
    def __init__(self, l, w, h) -> None:
        self.length, self.width, self.height = int(l), int(w), int(h)
        pass

    def ribbon(self):
        a = sorted([self.length, self.width, self.height])

        return 2* a[0] + 2* a[1]

    def area(self):
        return self.length*self.height*self.width + self.ribbon()

def parse_data(data):

    return [Box(*d.split("x")) for d in data.split()]

@log
def main(data):
    data = parse_data(data)

    erg = 0

    for box in data:
        erg += box.area()

    return erg




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