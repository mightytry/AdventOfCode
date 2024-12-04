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

STR = "XMAS"

def search_direction(data, x, y, direction):
    for i, c in enumerate(STR[2:], 1):
        if not look_in_direction(data, x + direction[0]*i, y+ direction[1]*i, c):
            return 0
    return 1

def search(data, x, y):
    res = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == 0 and dy == 0:
                continue
            if (look_in_direction(data, x +dx, y + dy, STR[1])):
                res += search_direction(data, x +dx, y + dy, (dx, dy))

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
        print("Got:", main(example[0:-1]), "Expected:", example[-1].strip().split(",")[0])
    data1 = open("./Day 4/data1", "r").readlines()

    if data1 != "":
        if SUBMIT:
            submit(main(data1), day=4, year=2024)
        else:
            print(main(data1))
    else:
        print("No data1 found")