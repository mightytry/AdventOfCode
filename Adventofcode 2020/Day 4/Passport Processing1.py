import sys
sys.path.insert(0, '.')
from tools import log

class Passport():
    def __init__(self, data):
        self.data = data
        self.fields = {}
        for field in " ".join(data.split("\n")).split(" "):
            self.fields[field.split(":")[0]] = field.split(":")[1]

    def validate(self):
        return len(self.fields) == 8 or (len(self.fields) == 7 and "cid" not in self.fields)

def parse_data(data):
    data = data.split("\n\n")

    return [Passport(x) for x in data]

@log
def main(data):
    data = parse_data(data)

    return sum([x.validate() for x in data])


data1 = open("./Day 4/data1", "r").read()
data2 = open("./Day 4/data2", "r").read()

main(data1)
#main(data2)