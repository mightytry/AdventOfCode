import sys
sys.path.insert(0, '.')
from tools import log, timer
from aocd import submit

def get_start(data):
    for y, row in enumerate(data):
        for x, c in enumerate(row):
            if (c == "^"):
                return [x, y]

def rotate(direction):
    return (-direction[1], direction[0])

def parse_data(data):
    return [list(x.strip()) for x in data]


@timer
def main(data):
    data = parse_data(data)
    start = get_start(data)
    direction = (0, -1)
    result = 0
    while (start[0] < len(data[0])-1 and start[0] > 0 and start[1] < len(data)-1 and start[1] > 0):
        while (data[start[1]+direction[1]][start[0]+direction[0]] == "#"):
            direction = rotate(direction)
        if (data[start[1]][start[0]] != "X"):
            result += 1
        data[start[1]][start[0]] = "X"
        start[0] += direction[0]
        start[1] += direction[1]
    result += 1

    return result




if __name__ == "__main__":
    SUBMIT = False
    for num in range(2):
        # last line is expected output
        example = open(f"./Day 6/example{num}", "r").readlines()
        print("Got:", main(example[0:-1]), "Expected:", example[-1].strip().split(",")[0])
    data1 = open("./Day 6/data1", "r").readlines()

    if data1 != "":
        if SUBMIT:
            submit(main(data1), day=6, year=2024)
        else:
            print(main(data1))
    else:
        print("No data1 found")