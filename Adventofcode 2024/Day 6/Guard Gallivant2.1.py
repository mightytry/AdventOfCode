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

def is_in_bounds(data, x, y):
    return x < len(data[0])-1 and x > 0 and y < len(data)-1 and y > 0

def in_bounds(data, x, y):
    return x < len(data[0]) and x >= 0 and y < len(data) and y >= 0

def trywalk(data, prev, new, direction):
    met = set()
    while (is_in_bounds(data, prev[0], prev[1])):
        while (data[(ny := prev[1]+direction[1])][(nx := prev[0]+direction[0])] == "#" or [nx, ny] == new):
            direction = rotate(direction)
            if ((prev[0], prev[1], direction) in met):
                return True
            else:
                met.add((prev[0], prev[1], direction))
        prev[0] += direction[0]
        prev[1] += direction[1]
    return False


@timer
def main(data):
    data = parse_data(data)
    start = get_start(data)
    s= start.copy()
    direction = (0, -1)
    result = set()
    while (is_in_bounds(data, start[0], start[1])):
        while (data[start[1]+direction[1]][start[0]+direction[0]] == "#"):
            direction = rotate(direction)
        start[0] += direction[0]
        start[1] += direction[1]
        if (s != start and trywalk(data, s.copy(), start, (0, -1))):
            result.add((start[0], start[1]))

    return len(result)


if __name__ == "__main__":
    SUBMIT = False
    for num in range(1):
        # last line is expected output
        example = open(f"./Day 6/example{num}", "r").readlines()
        print("Got:", main(example[0:-1]), "Expected:", example[-1].strip().split(",")[1])
    data1 = open("./Day 6/data1", "r").readlines()

    if data1 != "":
        if SUBMIT:
            submit(main(data1), day=6, year=2024)
        else:
            print(main(data1))
    else:
        print("No data1 found")