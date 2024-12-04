import sys
sys.path.insert(0, '.')
from tools import log

class Pair:
    def __init__(self, index, left, right) -> None:
        self.index = index
        self.left = eval(left)
        self.right = eval(right)

    @property
    def in_order(self):
        return self.compare(self.left, self.right)

    def compare(self, left, right):
        for v in range(min(len(left), len(right))):
            if type(left[v]) == type(right[v]) == int:
                erg = left[v] - right[v]
                if erg == 0:
                    continue
                elif erg > 0:
                    return False
                else:
                    return True

            elif type(left[v]) == type(right[v]) == list:
                erg = self.compare(left[v], right[v])
                if erg == None:
                    continue
                else: 
                    return erg
            else:
                return self.compare(left[v], [right[v]]) if type(left[v]) == list else self.compare([left[v]], right[v])

        return None if len(left) == len(right) else True if len(left) < len(right) else False
            


def parse_data(data):
    data = data.split("\n\n")

    p = []

    for n, i in enumerate(data, 1):
        p.append(Pair(n, *i.splitlines()))

    return p

@log
def main(data):
    data = parse_data(data)

    return sum(map(lambda x: x[1].index if x[0] else 0, zip([x.in_order for x in data], data)))


if __name__ == "__main__":
    data1 = open("./Day 13/data1", "r").read()
    data2 = open("./Day 13/data2", "r").read()

    if data1 != "":
        main(data1)
    else:
        print("No data1 found")
    if data2 != "":
        main(data2)
    else:
        print("No data2 found")