import sys, itertools

from numpy import equal
sys.path.insert(0, '.')
from tools import log

class Pos():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Octopus():
    def __init__(self, pos, energy):
        self.pos = pos
        self.energy = energy

    def energy_check(self):
        return self.energy-1 == 9
        
    def step(self):
        self.energy += 1
        return self.energy_check()

    def reset(self):
        self.energy = 0

class Octopusses():
    @classmethod
    def __init__(self, octopusses):
        self.octopusses = octopusses
        self.flashes = 0

    @classmethod
    def step(self):
        flashers = []
        
        for row in self.octopusses:
            for octopuss in row:
                if octopuss.step():
                    self.flashes += 1
                    flashers.append(octopuss)

        return self.handle_flasher(flashers)

    @classmethod
    def get_neighbors(self, x, y, flashers):
        neighbors = []
        for elm in [(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0)]:
            if (x+elm[0] >= 0 and y+elm[1] >= 0 and x+elm[0] < len(self.octopusses) and y+elm[1] < len(self.octopusses[x+elm[0]])) and self.octopusses[x+elm[0]][y+elm[1]] not in flashers:
                neighbors.append(self.octopusses[x+elm[0]][y+elm[1]])
        return neighbors

    @classmethod
    def handle_flasher(self, flashers):
        if flashers == []:
            return False
            
        new_flashers = []
        for flasher in flashers:
            flasher.step()
            x = flasher.pos.x
            y = flasher.pos.y
            for octopuss in self.get_neighbors(x,y,flashers):
                if octopuss.step():
                    self.flashes += 1
                    new_flashers.append(octopuss)
        
        self.handle_flasher(new_flashers)
        for flasher in flashers:
            flasher.reset()

def get_data(data):
    octopusses = []

    for x, row in enumerate(data.split('\n')):
        octopuss_row = []
        for y,octopuss in enumerate(row):
            octopuss_row.append(Octopus(Pos(x, y), int(octopuss)))

        octopusses.append(octopuss_row)

    return octopusses

@log
def main(data):
    Octopusses(get_data(data))
    for x in range(1000):
        o = Octopusses.flashes
        Octopusses.step()
        if Octopusses.flashes-o >99:
            return x+1

    return Octopusses.flashes


data1 = open("./Day 11/data1", "r").read()
data2 = open("./Day 11/data2", "r").read()

main(data1)
main(data2)