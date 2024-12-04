import sys
sys.path.insert(0, '.')
from tools import log, timer
from aocd import submit

def parse_data(data):
    data = [list(x.strip()) for x in data]
    return data

def look_in_direction(data, x, y, char):
    if (x not in range(0, len(data[0]))):
        return False
    if (y not in range(0, len(data))):
        return False
    return data[y][x] == char

STR = "AMS"

def search(data, x, y):
    cn = 0
    res = 0
    for dx, dy in ((-1,-1), (-1, 1), (1, -1), (1, 1)):
        if (look_in_direction(data, x +dx, y + dy, STR[1]) and look_in_direction(data, x +dx*-1, y + dy*-1, STR[2])):
            cn += 1
    if cn == 2:
        res += 1

    return res



def main(data):
    data = parse_data(data)
    res = 0
    for j, l in enumerate(data):
        for i, c in enumerate(l):
            if (c == STR[0]):
                res += search(data, i, j)
    return res




if __name__ == "__main__":
    SUBMIT = False
    for num in range(1):
        # last line is expected output
        example = open(f"./Day 4/example{num}", "r").readlines()
        print("Got:", main(example[0:-1]), "Expected:", example[-1].strip().split(",")[1])
    data1 = open("./Day 4/data1", "r").readlines()

    if data1 != "":
        if SUBMIT:
            submit(main(data1), day=4, year=2024)
        else:
            print(main(data1))
    else:
        print("No data1 found")