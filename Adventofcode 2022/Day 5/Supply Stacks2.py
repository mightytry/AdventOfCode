import sys
sys.path.insert(0, '.')
from tools import log

class Move:
    def __init__(self, amount,start,goal):
        self.amount = amount
        self.start = start
        self.goal = goal

    def __repr__(self):
        return str(self.amount) + " from " + str(self.start) + " to " + str(self.goal)

    def __str__(self):
        return str(self.amount) + " from " + str(self.start) + " to " + str(self.goal)

class Stack:
    def __init__(self):
        self.crates = []

    def pull(self, amount):
        if len(self.crates) >= amount:
            c = self.crates[:amount]
            self.crates = self.crates[amount:]
            return c
        else:
            return False
            
    def push(self,amount):
        amount.extend(self.crates)
        self.crates = amount
        
    def __repr__(self):
        return str(self.crates)

    def __str__(self):
        return str(self.crates)
        
class Crate:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

def parse_data(data):
    data = data.split("\n\n")

    stacks = []
    moves = []

    d = data[0].splitlines()[:-1]

    for stack in range(int((len(d[0])+1)/4)):
        stacks.append(Stack())

    for row in range(len(d)):
        for crate in range(0, len(d[row]), 4):
            if d[row][crate:crate+3] != "   ":
                stacks[int(crate/4)].crates.append(Crate(d[row][crate+1:crate+2]))
        
    
    for line in data[1].splitlines():
        amount = int(line.split(" ")[1])
        start = int(line.split(" ")[3])
        goal = int(line.split(" ")[5])
        move = Move(amount,start,goal)
        moves.append(move)

    return stacks, moves

def move_crate(stacks, move):
    crates = stacks[move.start-1].pull(move.amount)
    if crates:
        stacks[move.goal-1].push(list(crates))
    else:
        print("Not enough crates in stack", move.start)

def move_all(stacks, moves):
    for move in moves:
        move_crate(stacks, move)

def print_stacks(stacks):
    for stack in stacks:
        yield stack.crates[0].name

@log
def main(data):
    stacks, moves = parse_data(data)
    move_all(stacks, moves)

    return "".join(list(print_stacks(stacks)))


if __name__ == "__main__":
    data1 = open("./Day 5/data1", "r").read()
    data2 = open("./Day 5/data2", "r").read()

    if data1 != "":
        main(data1)
    else:
        print("No data1 found")
    if data2 != "":
        main(data2)
    else:
        print("No data2 found")