import sys, math
sys.path.insert(0, '.')
from tools import log, timer
from aocd import submit

class Equation:
    def __init__(self, res, numb):
        self.res = res
        self.numb = numb

    @staticmethod
    def methods(n1, n2):
        yield n1 + n2
        yield n1 * n2
        yield int(str(n1) + str(n2))
    
    def solve(self, n, i):
        if i == len(self.numb):
            return n == self.res
        for f in self.methods(n, self.numb[i]):
            if self.solve(f, i+1):
                return True
        return False

    def result(self):
        if (self.solve(self.numb[0], 1)):
            return self.res
        return 0

def parse_data(data):
    return [Equation(int(x.split(":")[0]), list(map(int, x.split(":")[1].strip().split(" ")))) for x in data]

@timer
def main(data):
    data = parse_data(data)

    return sum(map(Equation.result, data))


if __name__ == "__main__":
    SUBMIT = False
    for num in range(1):
        # last line is expected output
        example = open(f"./Day 7/example{num}", "r").readlines()
        print("Got:", main(example[0:-1]), "Expected:", example[-1].strip().split(",")[1])
    data1 = open("./Day 7/data1", "r").readlines()

    if data1 != "":
        if SUBMIT:
            submit(main(data1), day=7, year=2024)
        else:
            print(main(data1))
    else:
        print("No data1 found")