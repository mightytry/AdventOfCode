import sys
sys.path.insert(0, '.')
from tools import log, timer

class Entry:
    def __init__(self, value):
        self.value = value
        if ("=" in value):
            self.label = value[:-2]
            self.value = int(value[-1])
        else:
            self.label = value[:-1]
            self.value = None
        self.hash = self.get_hash()


    def get_hash(self):
        return to_num(self.label)
    
    def __eq__(self, other):
        return self.label == other.label

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
    return [Entry(v) for v in data.split(",")]

@timer
@log
def main(data):
    data = parse_data(data)
    boxes = {i:[] for i in range(256)}
    for i in data:
        if i in boxes[i.hash]:
            if i.value == None:
                boxes[i.hash].remove(i)
            else:
                boxes[i.hash][boxes[i.hash].index(i)].value = i.value
        else:
            if i.value != None:
                boxes[i.hash].append(i)

    val = 0
    for n, b in boxes.items():
        for m, i in enumerate(b):
            val += (n+1)*(m+1)*i.value

    return val




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