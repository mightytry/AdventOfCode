import sys
sys.path.insert(0, '.')
from tools import log, timer
from aocd import submit

class Level():
    def __init__(self, row):
        self.data = list(map(int, row.strip().split(" ")))

    def is_safe(self, order, start = 0,bad = False):
        data = self.data[start:]
        p = data[0]
        for n in data[1:]:
            if abs(p-n) > 3 or abs(p-n) < 1:
                if bad:
                    return False
                bad = True
                continue
            if order != (p < n):
                if bad:
                    return False
                bad = True
                continue
            p = n
        return True

def parse_data(data):
    data = [Level(row) for row in data]
    return data

def main(data):
    data = parse_data(data)

    return sum([(l.is_safe(True) or l.is_safe(False) or l.is_safe(True, 1, True)or l.is_safe(False, 1, True)) for l in data])




if __name__ == "__main__":
    SUBMIT = False
    for num in range(1):
        # last line is expected output
        example = open(f"./Day 2/example{num}", "r").readlines()
        print("Got:", main(example[0:-1]), "Expected:", example[-1].strip().split(",")[1])
    data1 = open("./Day 2/data1", "r").readlines()
    
    if data1 != "":
        if SUBMIT:
            submit(main(data1), day=2, year=2024)
        else:
            print(main(data1))
    else:
        print("No data1 found")