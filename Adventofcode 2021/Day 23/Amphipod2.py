import copy
import math
from multiprocessing import Pool
import sys
import time
import timeit
from functools import cache, lru_cache
from queue import PriorityQueue

sys.path.insert(0, '.')
from tools import log

class Position():
    NONE = -1
    HALLWAY = 1
    ROW1 = 2
    ROW2 = 3
    ROW3 = 4
    ROW4 = 5

    def __init__(self, line, pos):
        self.pos = pos
        self.line = line

    def __repr__(self) -> str:
        return f'(L:{self.line}, P:{self.pos})'
    
    def __str__(self) -> str:
        return repr(self)

class Amphipod():
    def __init__(self, group, pos:Position):
        self.group = group
        self.pos = pos
        self.target_group = ord(self.group) - ord("A")

    @property
    def room_pos(self):
        return self.target_group*2 + 3

    @property
    def consumption(self):
        return 10**(self.target_group)
    
    def move(self, direction):
        self.pos.line += direction[0]
        self.pos.pos += direction[1]

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
    
class Wall():
    def __init__(self, pos):
        self.pos = pos

    def __repr__(self) -> str:
        return f'W({self.pos})'
    
    def __str__(self) -> str:
        return "#"

class Situation():
    Queue = None

    def __init__(self, hallway_len, row1, row2, row3, row4,  create = True):
        self.rows = [row1, row2, row3, row4]
        #self.moves = []
        self.amphis = row1 + row2 + row3 + row4
        self.cost = 0
        self.hallway_len = hallway_len
        if (create):
            self.gen_board()


    def gen_board(self):
        _row1 = copy.deepcopy(self.rows[0])
        _row2 = copy.deepcopy(self.rows[1])
        _row3 = copy.deepcopy(self.rows[2])
        _row4 = copy.deepcopy(self.rows[3])
        for x in range(3):
            _row1.insert(x*2+1, Wall(Position(Position.ROW1, x*2+4)))
            _row2.insert(x*2+1, Wall(Position(Position.ROW2, x*2+4)))
            _row3.insert(x*2+1, Wall(Position(Position.ROW3, x*2+4)))
            _row4.insert(x*2+1, Wall(Position(Position.ROW4, x*2+4)))

        self.board = [
            [Wall(Position(Position.NONE, x)) for x in range(self.hallway_len+2)],
            [Wall(Position(Position.NONE, 0)), *[Empty(Position(Position.HALLWAY, x)) for x in range(self.hallway_len)], Wall(Position(Position.NONE, self.hallway_len+1))],
            [*[Wall(Position(Position.NONE, x)) for x in range(3)], *_row1, *[Wall(Position(Position.NONE, x)) for x in range(3)]],
            [*[Wall(Position(Position.NONE, x)) for x in range(3)], *_row2, *[Wall(Position(Position.NONE, x)) for x in range(3)]],
            [*[Wall(Position(Position.NONE, x)) for x in range(3)], *_row3, *[Wall(Position(Position.NONE, x)) for x in range(3)]],
            [*[Wall(Position(Position.NONE, x)) for x in range(3)], *_row4, *[Wall(Position(Position.NONE, x)) for x in range(3)]],
            [Wall(Position(Position.NONE, x)) for x in range(self.hallway_len+2)]
        ]

    
    def can_move_in_room(self, amphipod:Amphipod):
        room = amphipod.target_group
        a = self.board[Position.ROW1][amphipod.room_pos]
        b = self.board[Position.ROW2][amphipod.room_pos]
        c = self.board[Position.ROW3][amphipod.room_pos]
        d = self.board[Position.ROW4][amphipod.room_pos]
        if (a.__class__ == Empty and b.__class__ == Empty and c.__class__ == Empty and d.__class__ == Empty):
            target = d
        elif (d.target_group == room and a.__class__ == Empty and b.__class__ == Empty and c.__class__ == Empty):
            target = c
        elif (d.target_group == room and c.target_group == room and a.__class__ == Empty and b.__class__ == Empty):
            target = b
        elif (d.target_group == room and c.target_group == room and b.target_group == room and a.__class__ == Empty):
            target = a
        else:
            return False
        #Check way to room
        if amphipod.pos.pos < target.pos.pos:
            mi = amphipod.pos.pos+1
            ma = target.pos.pos+1
        else:
            mi = target.pos.pos
            ma = amphipod.pos.pos

        for x in range(mi, ma):
            if (self.board[Position.HALLWAY][x].__class__ != Empty):
                return False

        return target
        
    def move(self, amphipod:Amphipod, direction:tuple[int, int]):
        moves = amphipod.pos.line + direction[0] - Position.HALLWAY + amphipod.pos.line - Position.HALLWAY + abs(direction[1])

        self.cost += amphipod.consumption * moves
        #self.moves.append((amphipod, direction))

        self.board[amphipod.pos.line][amphipod.pos.pos] = Empty(Position(amphipod.pos.line, amphipod.pos.pos))
        amphipod.move(direction)
        self.board[amphipod.pos.line][amphipod.pos.pos] = amphipod
    
    def can_stay(self, amphipod:Amphipod, direction:tuple[int, int]):
        pos = amphipod.pos.pos + direction[1]
        if (amphipod.pos.line + direction[0] == Position.HALLWAY):
            return pos != 3 and pos != 5 and pos != 7 and pos != 9
        else:
            return True

    def gen_moves(self, amphipod:Amphipod):  
        try:
            if amphipod.room_pos == amphipod.pos.pos and all([self.board[x][amphipod.pos.pos].room_pos == amphipod.room_pos for x in range(amphipod.pos.line+1, Position.ROW4+1)]):
                return []
        except:
            pass
        pos_moves = []
        free = all([self.board[x][amphipod.pos.pos].__class__ == Empty for x in range(Position.HALLWAY, amphipod.pos.line)])
        if ((target := self.can_move_in_room(amphipod)) and (free or amphipod.pos.line == Position.HALLWAY)):
            pos_moves.append((target.pos.line-amphipod.pos.line, target.pos.pos-amphipod.pos.pos))
        elif (amphipod.pos.line != Position.HALLWAY and free):
            for x in range(amphipod.pos.pos+1, len(self.board[Position.HALLWAY])-1):
                if (self.board[Position.HALLWAY][x].__class__ == Empty):
                    dire = (Position.HALLWAY-amphipod.pos.line, x-amphipod.pos.pos)
                    if (self.can_stay(amphipod, dire)):
                        pos_moves.append(dire)
                else:
                    break
            for x in range(amphipod.pos.pos-1, 0, -1):
                if (self.board[Position.HALLWAY][x].__class__ == Empty):
                    dire = (Position.HALLWAY-amphipod.pos.line, x-amphipod.pos.pos)
                    if (self.can_stay(amphipod, dire)):
                        pos_moves.append(dire)
                else:
                    break

        return pos_moves

    def check_solution(self):
        n = 0
        for ampi in self.amphis:
            if (ampi.pos.pos != ampi.room_pos or ampi.pos.line == Position.HALLWAY):
                n+=1
        return n

    def do_new(self):
        new = Situation(self.hallway_len, [], [], [], [], False)
        new.board = [
            [Wall(Position(Position.NONE, x)) for x in range(self.hallway_len+2)],
            [Wall(Position(Position.NONE, 0)), *[Empty(Position(Position.HALLWAY, x)) for x in range(self.hallway_len)], Wall(Position(Position.NONE, 2))],
            [*[Wall(Position(Position.NONE, x)) for x in range(3)], Empty(Position(Position.ROW1, 3)), Wall(Position(Position.ROW1, 4)),Empty(Position(Position.ROW1, 5)), Wall(Position(Position.ROW1, 6)),Empty(Position(Position.ROW1, 7)), Wall(Position(Position.ROW1, 8)),Empty(Position(Position.ROW1, 9)), *[Wall(Position(Position.NONE, x)) for x in range(3)]],
            [*[Wall(Position(Position.NONE, x)) for x in range(3)], Empty(Position(Position.ROW2, 3)), Wall(Position(Position.ROW2, 4)),Empty(Position(Position.ROW2, 5)), Wall(Position(Position.ROW2, 6)),Empty(Position(Position.ROW2, 7)), Wall(Position(Position.ROW2, 8)),Empty(Position(Position.ROW2, 9)), *[Wall(Position(Position.NONE, x)) for x in range(3)]],
            [*[Wall(Position(Position.NONE, x)) for x in range(3)], Empty(Position(Position.ROW3, 3)), Wall(Position(Position.ROW3, 4)),Empty(Position(Position.ROW3, 5)), Wall(Position(Position.ROW3, 6)),Empty(Position(Position.ROW3, 7)), Wall(Position(Position.ROW3, 8)),Empty(Position(Position.ROW3, 9)), *[Wall(Position(Position.NONE, x)) for x in range(3)]],
            [*[Wall(Position(Position.NONE, x)) for x in range(3)], Empty(Position(Position.ROW4, 3)), Wall(Position(Position.ROW4, 4)),Empty(Position(Position.ROW4, 5)), Wall(Position(Position.ROW4, 6)),Empty(Position(Position.ROW4, 7)), Wall(Position(Position.ROW4, 8)),Empty(Position(Position.ROW4, 9)), *[Wall(Position(Position.NONE, x)) for x in range(3)]],
            [Wall(Position(Position.NONE, x)) for x in range(self.hallway_len+2)]
        ]
        for n, ampi in enumerate(self.amphis):
            new.amphis.append(Amphipod(ampi.group, Position(ampi.pos.line, ampi.pos.pos)))
            new.board[ampi.pos.line][ampi.pos.pos] = new.amphis[n]
        new.cost = self.cost
        return new

    @lru_cache(maxsize=1000000)
    def gen_solution(self):
        mooved = False

        for n, amphipod in enumerate(self.amphis):
            moves = self.gen_moves(amphipod)
            if (len(moves) != 0):
                mooved = True
            for move in moves:
                new = self.do_new()
                new.move(new.amphis[n], move)
                Situation.Queue.put(new)

        if (not mooved and self.check_solution() == 0):
            return True

    def __repr__(self) -> str:
        return "\n".join(map(lambda x: "".join(map(str, x)), self.board))
    
    def __str__(self) -> str:
        return repr(self)
    
    def __lt__(self, other):
        return self.cost < other.cost 
    
    def __eq__(self, other):
        return str(self) == str(other)
    
    def __hash__(self):
        return hash(str(self))

def parse_data(data):
    data = data.splitlines()

    row1 = list(map(lambda x: Amphipod(x[1], Position(Position.ROW1, x[0]*2+3)), enumerate(filter(lambda x: x.isalpha(), data[2].split("#")))))
    row2 = list(map(lambda x: Amphipod(x[1], Position(Position.ROW2, x[0]*2+3)), enumerate(filter(lambda x: x.isalpha(), "#D#C#B#A#".split("#")))))
    row3 = list(map(lambda x: Amphipod(x[1], Position(Position.ROW3, x[0]*2+3)), enumerate(filter(lambda x: x.isalpha(), "#D#B#A#C#".split("#")))))
    row4 = list(map(lambda x: Amphipod(x[1], Position(Position.ROW4, x[0]*2+3)), enumerate(filter(lambda x: x.isalpha(), data[3].split("#")))))

    return data[1].count("."), row1 , row2, row3, row4

@log
def main(data):
    Situation.Queue = PriorityQueue()
    Situation.gen_solution.cache_clear()
    data = parse_data(data)

    situation = Situation(*data)
    situation.gen_solution()

    while not Situation.Queue.empty():
        i = Situation.Queue.get()
        if Situation.gen_solution(i) == True:
            break

    return i.cost




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