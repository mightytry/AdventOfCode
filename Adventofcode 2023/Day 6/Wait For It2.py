import math
import sys
sys.path.insert(0, '.')
from tools import log

class Race():
    def __init__(self, time, record):
        self.time = time
        self.record = record

    def get_abc(self, a, b, c):
        # -(b) +- sqrt(b^2 -4ac) /2a
        return (-b + math.sqrt(b**2 - 4*a*c)) / (2*a), (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)

    def get_wins(self):
        # i (time - i) - record
        # i*time - i*i - record
        # -i*i + i*time - record
        a = -1
        b = self.time
        c = -self.record
        x1, x2 = self.get_abc(a, b, c)
        x1 = int(x1)
        x2 = int(x2)
        return x2-x1
        

def parse_data(data):
    data = data.splitlines()

    time = int("".join(data[0].split()[1:]))
    record = int("".join(data[1].split()[1:]))

    data = Race(time, record)

    return data

@log
def main(data):
    data = parse_data(data)

    return (data.get_wins())




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