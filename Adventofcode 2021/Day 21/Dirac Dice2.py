import functools
import sys, copy
sys.path.insert(0, '.')
from tools import log

class Simulate():
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.m = 1
        self.score = 21

    def run(self):
        return self.sim(self.p1, self.p2)
    
    @functools.cache
    def sim(self, p1, p2):
        if p2.score >= self.score:
            return 0, 1
        
        w, l = 0, 0
        for x in range(1,4):
            for y in range(1,4):
                for z in range(1,4):
                    _p1 = copy.deepcopy(p1)
                    _p1.move(x+y+z)
                    _w , _l = self.sim(p2, _p1)
                    w += _l
                    l += _w

        return w, l


class Player():
    def __init__(self, start):
        self.pos = start
        self.score = 0

    def move(self, roll):
        self.pos = (roll+self.pos-1) % 10 +1
        self.score += self.pos

    def __hash__(self) -> int:
        return hash((self.pos, self.score))
    
    def __eq__(self, o: object) -> bool:
        return (self.pos, self.score) == (o.pos, o.score)
    


def parse_data(data):
    data = data.splitlines()
    players = [Player(int(data[0].split(": ")[1])), Player(int(data[1].split(": ")[1]))]

    return players

@log
def main(data):
    data = parse_data(data)
    p1 , p2 = data
    return max(Simulate(p1, p2).run())



if __name__ == "__main__":
    data1 = open("./Day 21/data1", "r").read()
    data2 = open("./Day 21/data2", "r").read()

    if data1 != "":
        main(data1)
    else:
        print("No data1 found")
    if data2 != "":
        main(data2)
    else:
        print("No data2 found")