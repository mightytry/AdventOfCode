import sys
sys.path.insert(0, '.')
from tools import log, timer
from aocd import submit

class Block:
    def __init__(self, id, co, free):
        self.id = id
        self.co = co
        self.free = free

def parse_data(data):
    data = data[0].strip()
    return [(Block(i//2, int(data[i]), int(0 if len(data) == i+1 else data[i+1]))) for i in range(0,len(data), 2)]

def main(data):
    data = parse_data(data)
    i = 0
    res = 0
    for b in data:
        while b.co != 0:
            res += b.id * i
            b.co -= 1
            i+=1
        while b.free != 0 and data[-1].co > 0:
            data[-1].co -= 1
            res += data[-1].id * i
            b.free -= 1
            i += 1
            if (data[-1].co == 0):
                data.pop()

    return res




if __name__ == "__main__":
    SUBMIT = False
    for num in range(1):
        # last line is expected output
        example = open(f"./Day 9/example{num}", "r").readlines()
        print("Got:", main(example[0:-1]), "Expected:", example[-1].strip().split(",")[0])
    data1 = open("./Day 9/data1", "r").readlines()

    if data1 != "":
        if SUBMIT:
            submit(main(data1), day=9, year=2024)
        else:
            print(main(data1))
    else:
        print("No data1 found")