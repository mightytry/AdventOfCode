import sys
sys.path.insert(0, '.')
from tools import log
import re

_RE_COMBINE_WHITESPACE = re.compile(r"\s+")

class Race():
    def __init__(self, time, record):
        self.time = time
        self.record = record

    def get_wins(self):
        win = False
        for i in range(self.time):
            r = i * (self.time-i)
            if r > self.record:
                win = True
                yield i
            elif win:
                break

def parse_data(data):
    data = data.splitlines()

    time = int("".join(_RE_COMBINE_WHITESPACE.sub(" ", data[0]).strip().split(" ")[1:]))
    record = int("".join(_RE_COMBINE_WHITESPACE.sub(" ", data[1]).strip().split(" ")[1:]))

    data = Race(time, record)

    return data

@log
def main(data):
    data = parse_data(data)

    r = len(list(data.get_wins()))

    print(r)




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