import sys
from turtle import st
sys.path.insert(0, '.')
from tools import log

NOTHING = 0
OVERSHOOT = 1
HIT = 2


class Vector2():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return str((self.x, self.y))

class Map():
    def __init__(self, data):
        data = data.replace("target area: x=", "").replace("y=", "").split(", ")
        x = [int(i) for i in data[0].split("..")]
        y = [int(i) for i in data[1].split("..")]
        self.box = (range(x[0], x[1]+1), range(y[0], y[1]+1))

    def check_state(self):
        if self.box[1].start > self.position.y or self.box[0].stop < self.position.x:
            return OVERSHOOT
        if self.position.x in self.box[0] and self.position.y in self.box[1]:
            return HIT
        return NOTHING

    def simulate(self, velo):
        self.highest_y = 0
        self.position = Vector2(0, 0)
        self.velocity = Vector2(*velo)

        while self.check_state() == NOTHING:
            self.step()

        return self.check_state()

    def step(self):
        # position increases by its velocity
        self.position.x += self.velocity.x
        self.position.y += self.velocity.y
        if self.position.y > self.highest_y:
            self.highest_y = self.position.y
        # x velocity changes by 1 toward the value 0 or does not change if it is already 0.
        self.velocity.x += (1 if self.velocity.x < 0 else -1) if self.velocity.x != 0 else 0

        #y velocity decreases by
        self.velocity.y -= 1


def find_velocity(data):
    map = Map(data)
    max = map.box[0].stop
    solutions = []

    for y in range(map.box[1].start, max):
        for x in range(max):
            map.simulate((x, y))
            if map.check_state() == HIT:
                solutions.append((x, y))

    return len(solutions)

def parse_data(data):
    return data

@log
def main(data):
    velo = find_velocity(parse_data(data)) 

    return velo

data1 = open("./Day 17/data1", "r").read()
data2 = open("./Day 17/data2", "r").read()

main(data1)
main(data2)