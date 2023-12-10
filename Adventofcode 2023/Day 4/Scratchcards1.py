import sys
sys.path.insert(0, '.')
from tools import log
# 5:40
class Game:
    def __init__(self, id, nyh: set, wn: set):
        self.id = id
        self.nyh = nyh
        self.wn = wn

    def get_win(self):
        return self.nyh.intersection(self.wn)

def parse_data(data):
    for n, line in enumerate(data.splitlines()):
        l = line.replace("  ", " ").split(": ")[1].split(" | ")
        yield Game(n, set(int(x) for x in l[0].split(" ")), set(int(x) for x in l[1].split(" ")))

@log
def main(data):
    data = parse_data(data)

    return sum(2**(len(x.get_win())-1) for x in data if len(x.get_win()) > 0)




if __name__ == "__main__":
    data1 = open("./Day 4/data1", "r").read()
    data2 = open("./Day 4/data2", "r").read()

    if data1 != "":
        main(data1)
    else:
        print("No data1 found")
    if data2 != "":
        main(data2)
    else:
        print("No data2 found")