import sys
sys.path.insert(0, '.')
from tools import log, timer
from aocd import submit

def parse_data(data):
    return data

def main(data):
    data = parse_data(data)

    return data




if __name__ == "__main__":
    SUBMIT = False
    for num in range(1):
        # last line is expected output
        example = open(f"./Day 10/example{num}", "r").readlines()
        print("Got:", main(example[0:-1]), "Expected:", example[-1].strip().split(",")[0])
    data1 = open("./Day 10/data1", "r").readlines()

    if data1 != "":
        if SUBMIT:
            submit(main(data1), day=10, year=2024)
        else:
            print(main(data1))
    else:
        print("No data1 found")