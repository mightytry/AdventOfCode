import sys
sys.path.insert(0, '.')
from tools import log, timer
from aocd import submit

def parse_data(data):
    a = {}
    for y, row in enumerate(data):
        for x, c in enumerate(row.strip()):
            if c != ".":
                if c in a:
                    a[c].add((x, y))
                else:
                    a[c] = {(x, y)}
    return [list(x.strip()) for x in data], a

def in_bounds(data, x, y):
    return x < len(data[0]) and x >= 0 and y < len(data) and y >= 0

def main(data):
    data, antenna = parse_data(data)
    res = 0
    for c in antenna.values():
        for a1 in c:
            for a2 in c:
                if (a1 == a2):
                    continue
                ox = a2[0] - a1[0] 
                oy = a2[1] - a1[1]
                i = 1
                while (in_bounds(data, (nx := (ox*i + a1[0])),(ny := (oy*i + a1[1])))):
                    if (data[ny][nx] != "#"):
                        data[ny][nx] = "#"
                        res +=1
                    i+=1
    return res




if __name__ == "__main__":
    SUBMIT = False
    for num in range(1):
        # last line is expected output
        example = open(f"./Day 8/example{num}", "r").readlines()
        print("Got:", main(example[0:-1]), "Expected:", example[-1].strip().split(",")[1])
    data1 = open("./Day 8/data1", "r").readlines()

    if data1 != "":
        if SUBMIT:
            submit(main(data1), day=8, year=2024)
        else:
            print(main(data1))
    else:
        print("No data1 found")