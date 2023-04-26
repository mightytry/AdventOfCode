import sys
sys.path.insert(0, '.')
from tools import log

def get_value(data, bit_index):
    zero_counter = 0
    one_counter = 0
    for bit in data:
        if bit[bit_index] == "0":
            zero_counter += 1
        elif bit[bit_index] == "1":
            one_counter += 1

    if one_counter < zero_counter:
        return "0"
    else:
        return "1"

def get_list(data, bit_index, bit):
    new_data = []

    for bita in data:
        if bita[bit_index] == bit:
            new_data.append(bita)

    return new_data

@log
def get_position(data):
    gamma = data
    epsilon = data

    for index in range(12):
        bit = get_value(gamma, index)
        gamma = get_list(gamma, index, bit)
        
        bit = "1" if get_value(epsilon, index) == "0" else "0"
        if len(epsilon) != 1:
            epsilon = get_list(epsilon, index, bit)


    return(int("".join(gamma).removesuffix("\n"), 2) * int("".join(epsilon).removesuffix("\n"), 2))

data1 = open("./Day 3/data1", "r").readlines()
data2 = open("./Day 3/data2", "r").readlines()

get_position(data1)
get_position(data2)