import sys, itertools
sys.path.insert(0, '.')
from tools import log

a = 1
b = 2 
c = 4
d = 8
e = 16
f = 32
g = 64

nums = {0 : (a+b+c+e+f+g), 1: (c+f), 2: (a+c+d+e+g),3:(a+c+d+f+g), 4 : (b+c+d+f), 5: (a+b+d+f+g), 6:(a+b+d+e+f+g), 7: (a+c+f), 8: (a+b+c+d+e+f+g), 9: (a+b+c+d+f+g)}

@log
def main(data):
    count = 0
    for x in zip(*return_data(data)):
        count += check_string_lenght(*x)
        
    return count
    


def return_data(data):
    return [x.split(" | ")[0].split(" ") for x in data.split('\n')], [x.split(" | ")[1].split(" ") for x in data.split('\n')]

def get_char_num(char, encoder):
    return encoder[["a", "b", "c", "d", "e", "f", "g"].index(char)]

def check_true(data, encoder):
    for x in data:
        val = 0
        for char in x:
            val += get_char_num(char, encoder)
        
        if val not in nums.values():
            return False

    return True

def check_string_lenght(data, out):
    encoder = []
    options = list(itertools.permutations([1,2,4,8,16,32,64]))
    output = ""

    for elm in options:
        if check_true(data,elm):
            encoder = elm
            break
    
    for x in out:
        val = 0
        for char in x:
            val += get_char_num(char, encoder)

        output += str(list(nums.values()).index(val))
    
    return int(output)

data1 = open("./Day 8/data1", "r").read()
data2 = open("./Day 8/data2", "r").read()

main(data1)
main(data2)