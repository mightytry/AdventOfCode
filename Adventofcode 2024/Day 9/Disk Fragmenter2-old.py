import sys
sys.path.insert(0, '.')
from tools import log, timer
from aocd import submit

class Block:
    def __init__(self, id, co):
        self.id = id
        self.co = co
    
    def __repr__(self):
        return "B: " + str(self.id)

class Free:
    def __init__(self, co):
        self.co = co
    def __repr__(self):
        return "S: " +str(self.co)
    

def parse_data(data):
    return [(Block(i//2, int(n)) if not i % 2 else Free(int(n))) for i, n in enumerate(data[0].strip())]

def main(data):
    data = parse_data(data)
    i = 0
    res = 0
    n = []
    for i in range(len(data)-1, -1 , -1):
        if isinstance()

    return n




if __name__ == "__main__":
    SUBMIT = False
    for num in range(1):
        # last line is expected output
        example = open(f"./Day 9/example{num}", "r").readlines()
        print("Got:", main(example[0:-1]), "Expected:", example[-1].strip().split(",")[1])
    data1 = open("./Day 9/data1", "r").readlines()

    if data1== "":
        if SUBMIT:
            submit(main(data1), day=9, year=2024)
        else:
            print(main(data1))
    else:
        print("No data1 found")