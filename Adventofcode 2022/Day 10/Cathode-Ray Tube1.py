import sys
sys.path.insert(0, '.')
from tools import log


class Command:
    def __init__(self,pos,cycles,type,value = 0):
        self.pos = pos
        self.cycles = cycles
        self.type = type
        self.value = int(value)
        self.finised = False
    
    def __repr__(self) -> str:
        return f'{self.pos}|{self.type} {self.value}'
    
    def get_valid(self,now_pos):
        return now_pos == (self.pos + self.cycles)

def parse_data(data):
    dataa = []
    for pos,line in enumerate(data.splitlines()):
        if len(line.split(" ")) > 1:
            command = Command(pos,2,line.split(" ")[0],line.split(" ")[1])
        else:
            command = Command(pos,1,*line.split(" "))
        dataa.append(command)
    return dataa

@log
def main(data):
    data = parse_data(data)
    cycles = [20,60,100,140,180,220]
    values = []
    solutions = []
    value = 1
    old_value = 1
    number_of_cycle = 0

    for elm in data:
        if elm.type == "noop":
            number_of_cycle += 1
        elif elm.type == "addx":
            number_of_cycle += 2
        
        for cycle in cycles:
            if cycle == number_of_cycle:
                values.append(value)
                solutions.append(value*cycle)
                cycles.remove(cycle)
            elif cycle == (number_of_cycle - 1):
                values.append(old_value)
                solutions.append(value*cycle)
                cycles.remove(cycle)
        
        if elm.type == "addx":
            value += elm.value

        old_value = value
        
    return sum(solutions)


if __name__ == "__main__":
    data1 = open("./Day 10/data1", "r").read()
    data2 = open("./Day 10/data2", "r").read()

    if data1 != "":
        main(data1)
    else:
        print("No data1 found")
    if data2 != "":
        main(data2)
    else:
        print("No data2 found")