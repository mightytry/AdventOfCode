import sys
sys.path.insert(0, '.')
from tools import log, timer
from aocd import submit

class Block:
    def __init__(self, id, co, free):
        self.id = id
        self.co = co
        self.free = free

    def __repr__(self):
        return str(self.id)*self.co + "."*self.free
    
    def get_res(self, i):
        res = self.id*(i*self.co+ self.co*(self.co-1)//2)
        advance = self.co + self.free
        return res, advance


def parse_data(data):
    data = data[0].strip()
    return [(Block(i//2, int(data[i]), int(0 if len(data) == i+1 else data[i+1]))) for i in range(0,len(data), 2)]

def main(data):
    data = parse_data(data)
    i = 0
    res = 0
    bi = 0
    g = len(data)-1
    while (g+bi != 0):
        i = g + bi
        b = data[i]
        d = data[i-1]
        for j, c in enumerate(data[:i]):
            if (c.free >= b.co):
                d.free += b.co + b.free
                b.free = c.free-b.co
                c.free = 0
                data.pop(i)
                data.insert(j+1, b)
                bi += 1
                break
        g-=1 
    
    n = 0
    for b in data:
        re, ad = b.get_res(n)
        n += ad #+1
        res += re

    
    return res




if __name__ == "__main__":
    SUBMIT = False
    for num in range(1):
        # last line is expected output
        example = open(f"./Day 9/example{num}", "r").readlines()
        print("Got:", main(example[0:-1]), "Expected:", example[-1].strip().split(",")[1])
    data1 = open("./Day 9/data1", "r").readlines()

    if data1 != "":
        if SUBMIT:
            submit(main(data1), day=9, year=2024)
        else:
            print(main(data1))
    else:
        print("No data1 found")