import sys, numpy as np
sys.path.insert(0, '.')
from tools import log

def parse_data(data):
    return np.array([np.array(list(s)) for s in data.split("\n")])

@log
def main(data):
    data = parse_data(data)
    cou = 0
    moved = True
    while moved:
        moved = False
        copy = np.copy(data)
        for n, line in enumerate(data):
            for m, c in enumerate(line):
                match c:
                    case ".":
                        continue
                    case ">":
                        if m+1 < len(line) and line[m+1] == ".":
                            copy[n,m] = "."
                            copy[n,m+1] = ">"
                            moved = True
                        elif m+1 == len(line) and line[0] == ".":
                            copy[n,m] = "."
                            copy[n,0] = ">"
                            moved = True
        data = copy
        copy = np.copy(data)
        for n, line in enumerate(data):
            for m, c in enumerate(line):
                match c:
                    case ".":
                        continue
                    case "v":
                        if n+1 < len(data) and data[n+1][m] == ".":
                            copy[n,m] = "."
                            copy[n+1,m] = "v"
                            moved = True
                        elif n+1 == len(data) and data[0,m] == ".":
                            copy[n,m] = "."
                            copy[0,m] = "v"
                            moved = True
        data = copy
        cou +=1

    return cou




if __name__ == "__main__":
    data1 = open("./Day 25/data1", "r").read()
    data2 = open("./Day 25/data2", "r").read()

    if data1 != "":
        main(data1)
    else:
        print("No data1 found")
    if data2 != "":
        main(data2)
    else:
        print("No data2 found")