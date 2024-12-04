import sys
sys.path.insert(0, '.')
from tools import log


def to_num(str):
    return int(str.replace("\n", ""))

@log
def get_largernums(data):
    last_number = to_num(data[0]) + to_num(data[1]) +to_num(data[2])
    lager_numbers = 0


    for iter in range(2, len(data)-2):
        number = to_num(data[iter]) + to_num(data[iter + 1]) +to_num(data[iter + 2])

        if number > last_number:
            lager_numbers += 1

        last_number = number

    return lager_numbers


data1 = open("./Day 1/data1", "r").readlines()
data2 = open("./Day 1/data2", "r").readlines()

get_largernums(data1)
get_largernums(data2)