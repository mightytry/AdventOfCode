import sys
sys.path.insert(0, '.')
from tools import log

class Command():
    commands = {"up": (0, -1), "down": (0, 1), "forward": (1, 1)}

    def __init__(self, data):
        self.command, self.value = self.parse_command(data)
    
    @classmethod
    def parse_command(cls, data):
        data = data.split()

        return cls.commands[data[0]][0], int(data[1]) * cls.commands[data[0]][1]
        

@log
def get_position(data):
    pos = [0, 0]
    aim = 0

    for command in data:
        command = Command(command)

        if command.command == 0:
            aim += command.value
        
        else:
            pos[0] += aim * command.value
            pos[1] += command.value
    
    return(pos[0] * pos[1])

data1 = open("./Day 2/data1", "r").readlines()
data2 = open("./Day 2/data2", "r").readlines()

get_position(data1)
get_position(data2)