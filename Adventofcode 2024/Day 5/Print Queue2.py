import sys
sys.path.insert(0, '.')
from tools import log, timer
from aocd import submit

class Rule():
    def __init__(self, data):
        self.data = data
        self.upper = data[1]
        self.lower = data[0]

        
class Update():
    def __init__(self, data:list[int]):
        self.data = data

    def sort(self, other: Rule):
        try:
            i_u = self.data.index(other.upper)
            i_l = self.data.index(other.lower)
            if i_u < i_l:
                self.data.pop(i_l)
                self.data.insert(i_u, other.lower)
            return i_u > i_l
        except:
            return True

    @property
    def middle(self):
        return self.data[len(self.data)//2]

def parse_data(data):
    n1, n2 = "".join(data).strip().split("\n\n")
    rules = tuple(Rule(tuple(map(int, d.split("|")))) for d in n1.split("\n"))
    data = tuple(Update(list(map(int, d.split(",")))) for d in n2.split("\n"))
    return rules, data

@timer
def main(data):
    rules, updates = parse_data(data)
    res = 0
    for update in updates:
        w = False
        u = False
        while (not u):
            u = True
            for rule in rules:
                if not update.sort(rule):
                    w = True
                    u = False
        if w:
            res += update.middle

    return res




if __name__ == "__main__":
    SUBMIT = False
    for num in range(1):
        # last line is expected output
        example = open(f"./Day 5/example{num}", "r").readlines()
        print("Got:", main(example[0:-1]), "Expected:", example[-1].strip().split(",")[1])
    data1 = open("./Day 5/data1", "r").readlines()

    if data1 != "":
        if SUBMIT:
            submit(main(data1), day=5, year=2024)
        else:
            print(main(data1))
    else:
        print("No data1 found")