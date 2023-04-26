import copy
import json
from math import ceil, floor
import sys
sys.path.insert(0, '.')
from tools import log

class Number():
    def __repr__(self):
        return str(self.number)

    def __init__(self, depth, number, parrent = None):
        self.number = number
        self.depth = depth
        self.parrent = parrent

    def add_to_depth(self, depth):
        self.depth += depth

    def evaluate(self):
        return self.number

class Data():
    def __repr__(self):
        return str(self.children)

    def __init__(self, depth, children = None, parrent = None):
        self.children = children
        self.parrent = parrent # is set while parsing
        self.depth = depth

    def add_to_depth(self, depth):
        self.depth += depth

        for child in self.children:
            child.add_to_depth(depth)

    def add(self, data):
        out = Data(0, [self, data])

        for d in (self, data):
            d.add_to_depth(1)
            d.parrent = out
        
        return out

    def get_numbers(self):
        nums = []

        for d in self.children:
            if isinstance(d, Number):
                nums.append(d)
            else:
                nums.extend(d.get_numbers())

        return nums

    def reduce(self):
        numbers = self.get_numbers()
        if self.explode(numbers) or self.split(numbers):
            return True
        return False

    def split(self, numbers):
        for num in numbers:
            if num.number >= 10:
                n1 = Number(num.parrent.depth+2, floor(num.number/2))
                n2 = Number(num.parrent.depth+2, ceil(num.number/2))
                data = Data(num.parrent.depth+1, [n1, n2], num.parrent)
                n1.parrent, n2.parrent = data, data
                
                num.parrent.children.insert(num.parrent.children.index(num), data)
                num.parrent.children.remove(num)
                return True 
        return False

    def explode(self, numbers):
        for child in self.children:
            if isinstance(child, Number): continue
            if child.depth >= 4 and isinstance(child.children[0], Number) and isinstance(child.children[1], Number) and len(child.children) == 2:
                #print(numbers)
                n1 = numbers.index(child.children[0])
                n2 = numbers.index(child.children[1])
                if n1 != 0:
                    numbers[n1-1].number += child.children[0].number
                if n2 != len(numbers)-1:
                    numbers[n2+1].number += child.children[1].number

                self.children.insert(self.children.index(child), Number(self.depth+1, 0, self))
                self.children.remove(child)
                return True
                
            if child.explode(numbers):
                return True
        return False

    def evaluate(self):
        num = 0
        for child in range(len(self.children)-1):
            num = 3*self.children[child].evaluate() + 2*self.children[child+1].evaluate()
        return num

def to_class_data(data, depth):
    if isinstance(data, int):
        return Number(depth, data)

    out = []
    pdata = Data(depth)

    for d in data:
        out.append(to_class_data(d, depth+1))

    pdata.children = out

    for x in pdata.children:
        x.parrent = pdata

    return pdata

def parse_data(data):
    out = []
    for d in data.split('\n'):
        out.append(to_class_data(json.loads(d), 0))

    return out




@log
def main(data):
    data = parse_data(data)

    ret = []

    for x in data:
        for y in data:
            #print(d, x)
            a = copy.deepcopy(y).add(copy.deepcopy(x))
            while a.reduce():
                pass
            ret.append(a.evaluate())

    return sorted(ret)[-1]


data1 = open("./Day 18/data1", "r").read()
data2 = open("./Day 18/data2", "r").read()

main(data1)
main(data2)