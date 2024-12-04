import sys
sys.path.insert(0, '.')
from tools import log, timer
from aocd import submit
import regex as re

def parse_data(data):
    pat = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)|(?<do>do\(\))|(?<dont>don't\(\))")
    data = pat.findall("".join(data))
    return data

def main(data):
    data = parse_data(data)
    en = True
    res = 0
    for (n1, n2, do, dont) in data:
        if do:
            en = True
        if dont:
            en = False
        if en and n1 and n2:
            res += int(n1) * int(n2)
    return res




if __name__ == "__main__":
    SUBMIT = False
    for num in range(1):
        # last line is expected output
        example = open(f"./Day 3/example{num}", "r").readlines()
        print("Got:", main(example[0:-1]), "Expected:", example[-1].strip().split(",")[0])
    data1 = open("./Day 3/data1", "r").readlines()

    if data1 != "":
        if SUBMIT:
            submit(main(data1), day=3, year=2024)
        else:
            print(main(data1))
    else:
        print("No data1 found")