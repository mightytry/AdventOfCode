import sys, numpy as np
sys.path.insert(0, '.')
from tools import log, timer

def solve_pattern(pattern):
    #rows
    if (x := try_solve_pattern(pattern[0], pattern[1:])) != None:
        return int(x/2+1)*100
    if (x := try_solve_pattern(pattern[-1], pattern[:-1], back=True)) != None:
        return int((len(pattern)+x)/2)*100

    pattern = list(zip(*pattern))
    #columns
    if (x := try_solve_pattern(pattern[0], pattern[1:])) != None:
        return int(x/2+1)
    if (x := try_solve_pattern(pattern[-1], pattern[:-1], back=True)) != None:
        return int((len(pattern)+x)/2)
    
    return False

def try_solve_pattern(start, pattern, back= False):
    if start in pattern:
        for i in [i for i, x in enumerate(pattern) if x == start]:
            # 27505
            r = True
            if not back:
                if i%2 == 1:
                    continue
                for j in range(0, int((i+1)/2)):
                    if pattern[j] != pattern[i-j-1]:
                        r = False
                        break
            else:
                if i%2 == 0:
                    continue
                for j in range(0, int((len(pattern)-i)/2)):
                    if pattern[i+j+1] != pattern[len(pattern)-j-1]:
                        r = False
                        break
            if r:
                return i


def parse_data(data):
    data = data.split("\n\n")
    return [da.splitlines() for da in data]

@log
@timer
def main(data):
    data = parse_data(data)

    return sum([solve_pattern(da) for da in data[:]])




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