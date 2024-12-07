import sys
sys.path.insert(0, '.')
from tools import log

class Password():
    def __init__(self, data):
        self.data = data
        self.min = int(data.split("-")[0])
        self.max = int(data.split("-")[1].split(" ")[0])
        self.letter = data.split(" ")[1].split(":")[0]
        self.password = data.split(" ")[2]

    def is_valid(self):
        count = self.password.count(self.letter)
        return count >= self.min and count <= self.max


def parse_data(data):
    return [Password(x) for x in data.splitlines()]

@log
def main(data):
    data = parse_data(data)

    return sum([x.is_valid() for x in data])


data1 = open("./Day 2/data1", "r").read()
data2 = open("./Day 2/data2", "r").read()

main(data1)
main(data2)