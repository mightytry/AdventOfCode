import sys
sys.path.insert(0, '.')
from tools import log

class Packet:
    def __init__(self, data) -> None:
        self.index = None
        self.data = eval(data)

    def __lt__(self, other):
        return self.compare(self.data, other.data)

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

    def __repr__(self) -> str:
        return f"{self.data}"
            

def parse_data(data):
    p = []
    for line in data.splitlines():
        if line == "":
            continue
        p.append(Packet(line))

    p.append(Packet("[[2]]"))
    p.append(Packet("[[6]]"))

    return p

@log
def main(data):
    data = parse_data(data)

    data = sorted(data)
    
    for n, i in enumerate(data, 1):
        i.index = n

    v = 1
    for elm in data:
        if elm.data == [[2]]:
            v *= elm.index
        elif elm.data == [[6]]:
            v *= elm.index
        

    return v


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