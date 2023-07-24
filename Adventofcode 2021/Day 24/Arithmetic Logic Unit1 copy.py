import sys
import timeit
sys.path.insert(0, '.')
from tools import log

class Instruction():
    vals = {"w" : 0, "x" : 0, "y" : 0, "z" : 0}
    stack = []

    @classmethod
    def reset(cls, stack):
        cls.vals = {"w" : 0, "x" : 0, "y" : 0, "z" : 0}
        cls.stack = stack

    @classmethod
    @property
    def valid(cls):
        return cls.vals["z"] == 0

    def __init__(self, instruction, v1, v2 = None) -> None:
        self.instruction = instruction
        self.value1 = v1
        self.value2 = v2

    def execute(self):
        match self.instruction:
            case "inp":
                Instruction.vals[self.value1] = int(Instruction.stack.pop())
                return
            
        var2 = Instruction.vals[self.value2] if not self.value2.isdecimal() and self.value2[0] != "-" else int(self.value2)
        match self.instruction:
            case "add":
                Instruction.vals[self.value1] += var2
                return
            case "mul":
                Instruction.vals[self.value1] *= var2
                return
            case "div":
                Instruction.vals[self.value1] //= var2
                return
            case "mod":
                Instruction.vals[self.value1] %= var2
                return
            case "eql":
                Instruction.vals[self.value1] = 1 if Instruction.vals[self.value1] == var2 else 0


    def __repr__(self) -> str:
        return f'Instruction({self.instruction}, {self.opcode}, {self.operand})'
    
    @classmethod
    def __reprr__(cls) -> str:
        return f'Instruction({cls.vals})'


def parse_data(data):
    instructions = []

    for line in data.splitlines():
        instructions.append(Instruction(*line.split(" ")))

    return instructions

@log
def main(data):
    data = parse_data(data)

    for x in range(1, 10):
        Instruction.reset(list(str(x)*13))
 
        for instruction in data:
            instruction.execute()

        if x % 1 == 0:
            print(Instruction.__reprr__(), Instruction.valid, x)

        if Instruction.valid:
            return x


if __name__ == "__main__":
    data1 = open("./Day 24/data1", "r").read()
    data2 = open("./Day 24/data2", "r").read()

    if data1 != "":
        main(data1)
    else:
        print("No data1 found")
    if data2 != "":
        main(data2)
    else:
        print("No data2 found")