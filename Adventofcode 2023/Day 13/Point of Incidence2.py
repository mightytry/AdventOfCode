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
    s = int("".join(start), base=2)
    for i, pa in enumerate(pattern):
        p = int("".join(pa), base=2)
        res = s&p | ((s ^ int("1"*len(start), base=2)) & (p ^ int("1"*len(start), base=2 )))
        if len(start) - int.bit_count(res) <= 1:
            # 27505
            r = True
            if not back:
                if i%2 == 1:
                    continue
                sm = len(start) - int.bit_count(res)
                for j in range(0, int((i+1)/2)):
                    if pattern[j] != pattern[i-j-1]:
                        sm += 1
                if sm != 1:
                    r = False
            else:
                if i%2 == 0:
                    continue
                sm = len(start) - int.bit_count(res)
                for j in range(0, int((len(pattern)-i)/2)):
                    if pattern[i+j+1] != pattern[len(pattern)-j-1]:
                        sm += 1
                if sm != 1:
                    r = False
            if r:
                return i

# def try_solve_pattern(start, pattern, back= False):
#     s = int("".join(start), base=2)
#     for pa in pattern:
#         p = int("".join(pa), base=2)
#         res = s&p | ((s ^ int("1"*len(start), base=2)) & (p ^ int("1"*len(start), base=2 )))
#         print(start, pa, int.bit_count(res))

def parse_data(data):
    data = data.split("\n\n")
    return [[[("0" if x == "." else "1") for x in d] for d in da.splitlines()] for da in data]

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