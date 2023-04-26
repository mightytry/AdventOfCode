import sys
sys.path.insert(0, '.')
from tools import log

class Amphipod():
    def __init__(self, group, pos):
        self.group = group
        self.pos = pos
        self.target_group = ord(self.group) - ord("A")

    @property
    def consumption(self):
        return 10**(self.target_group)
    
    @property
    def can_stay(self):
        if self.pos[0] == 0:
            return self.pos[1] != 2 and self.pos[1] != 4 and self.pos[1] != 6 and self.pos[1] != 8
        return True
    
    def move(self, direction):
        self.pos = (self.pos[0] + direction[0], self.pos[1] + direction[1])

    def __repr__(self) -> str:
        return f'A({self.group}, [{self.pos}])'
    
    def __str__(self) -> str:
        return self.group
    
class Empty():
    def __init__(self, pos):
        self.pos = pos

    def __repr__(self) -> str:
        return f'E({self.pos})'
    
    def __str__(self) -> str:
        return "."

class Situation():
    def __init__(self, hallway_len, row1, row2):
        self.hallway_len = hallway_len
        self.hallway = [Empty((0, i)) for i in range(hallway_len)]

        self.row1 = row1
        self.row2 = row2

    @property
    def rooms(self):
        return [[self.row1[x], self.row2[x]] for x in range(len(self.row1))]
    
    def move(self, amphipod, direction):
        if amphipod.pos[0] + direction[0] < 0 or amphipod.pos[0] + direction[0] > 2:
            return False
        if amphipod.pos[1] + direction[1] < 0:
            return False
        if amphipod.pos[0] + direction[0] == 0:
            if amphipod.pos[1] + direction[1] >= self.hallway_len:
                return False
        elif amphipod.pos[0] + direction[0] != 0:
            if amphipod.pos[1] + direction[1] >= len(self.row1):
                return False
            
        if amphipod.pos[0] + direction[0] == 0 and self.hallway[amphipod.pos[1] + direction[1]].__class__ == Amphipod:
            return False
        elif amphipod.pos[0] + direction[0] == 1 and self.row1[amphipod.pos[1] + direction[1]].__class__ == Amphipod:
            return False
        elif amphipod.pos[0] + direction[0] == 2 and self.row2[amphipod.pos[1] + direction[1]].__class__ == Amphipod:
            return False
        
        if amphipod.pos[0] == 0:
            self.hallway[amphipod.pos[1]] = Empty(amphipod.pos)
        elif amphipod.pos[0] == 1:
            self.row1[amphipod.pos[1]] = Empty(amphipod.pos)
        elif amphipod.pos[0] == 2:
            self.row2[amphipod.pos[1]] = Empty(amphipod.pos)

        amphipod.move(direction)
        if amphipod.pos[0] == 0:
            self.hallway[amphipod.pos[1]] = amphipod
        elif amphipod.pos[0] == 1:
            self.row1[amphipod.pos[1]] = amphipod
        elif amphipod.pos[0] == 2:
            self.row2[amphipod.pos[1]] = amphipod

        return True
    
    def gen_solution(self):
        for room in self.rooms:
            for amphipod in room:
                if amphipod.can_stay:
                    self.move(amphipod, (0, 0))


    def __repr__(self) -> str:
        return f"""\
#############
#{"".join(map(str, self.hallway))}#
###{"#".join(map(str, self.row1))}###
  #{"#".join(map(str, self.row2))}#
  #########"""

def parse_data(data):
    data = data.splitlines()

    row1 = list(map(lambda x: Amphipod(x[1], (1, x[0])), enumerate(filter(lambda x: x.isalpha(), data[2].split("#")))))
    row2 = list(map(lambda x: Amphipod(x[1], (2, x[0])), enumerate(filter(lambda x: x.isalpha(), data[3].split("#")))))

    return data[1].count("."), row1 , row2

@log
def main(data):
    data = parse_data(data)

    situation = Situation(*data)

    print(situation)
    print(situation.move(situation.row1[0], (-1, 0)))

    return situation




if __name__ == "__main__":
    data1 = open("./Day 23/data1", "r").read()
    data2 = open("./Day 23/data2", "r").read()

    if data1 != "":
        main(data1)
    else:
        print("No data1 found")
    if data2 != "":
        main(data2)
    else:
        print("No data2 found")