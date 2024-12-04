import sys, functools
sys.path.insert(0, '.')
from tools import log, timer

class Spring_Row:
    def __init__(self,springs,contiguous_group) -> None:
        self.springs = springs
        self.contiguous_group = tuple(contiguous_group)
        self.springs_len = len(self.springs)
        self.contiguous_group_len = len(self.contiguous_group)
        self.c_g_sum = [sum(self.contiguous_group[i:]) for i in range(self.contiguous_group_len+1)]
        self.CACHE = {}

    def eval(self):
        return self.count_possibilities(0,0,0)

    def count_possibilities(self, index, group, length):
        if length > self.contiguous_group[group]:
            return 0
        
        if not self.c_g_sum[group]+self.contiguous_group_len-group-1 <= self.springs_len - index+length:
            return 0
        
        if index == self.springs_len and length == self.contiguous_group[group] and group == self.contiguous_group_len-1:
            return 1

        if (index, group, length) in self.CACHE:
            return self.CACHE[(index, group, length)]
        
        res = 0
        s = self.springs[index]

        if s in "#?":
            res = self.count_possibilities(index+1,group,length+1)
        if s in ".?":
            if length == 0:
                res += self.count_possibilities(index+1,group,0)
            elif length == self.contiguous_group[group]:
                if group == self.contiguous_group_len-1:
                    res += self.count_possibilities(index+1,group,length)
                else:
                    res += self.count_possibilities(index+1,group+1,0)


        self.CACHE[(index, group, length)] = res
        return res   

    def __repr__(self) -> str:
        return str("".join(self.springs)) + "|" + str(self.contiguous_group)

@timer
def parse_data(data):
    for line in data.splitlines():
        #springs = [[sp for sp in elm] for elm in line.split(" ")[0].replace("."," ").split()]
        springs = []
        previous_elm = ""
        for index,elm in enumerate("?".join([line.split(" ")[0]]*5)):
            if not(elm == "." and previous_elm == "."):
                springs.append(elm)
            previous_elm = elm

        contiguous_group = [int(elm) for elm in line.split(" ")[1].split(",")]*5
        yield Spring_Row(springs,contiguous_group)

@log
@timer
def main(data):
    data = list(parse_data(data))
    return (sum(map(lambda x: x.eval(), data)))

#6935

if __name__ == "__main__":
    data1 = open("./Day 12/data1", "r").read()
    data2 = open("./Day 12/data2", "r").read()

    if data1 != "":
        main(data1)
    else:
        print("No data1 found")
    if data2 != "":
        main(data2)
    else:
        print("No data2 found")