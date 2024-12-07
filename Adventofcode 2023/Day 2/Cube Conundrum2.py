import sys
sys.path.insert(0, '.')
from tools import log, timer

class Colors:
    red = 0
    green = 1
    blue = 2

class Cube:
    def __init__(self, color:int, amount:int) -> None:
        self.color = color
        self.amount = amount

class Set:
    def __init__(self, cubes) -> None:
        self.cubes = cubes

    def get_color(self, color):
        return sum([x.amount for x in self.cubes if x.color == color])

class Game:
    def __init__(self, id) -> None:
        self.id = id
        self.sets = []

    def get_color(self, color):
        return sum([x.get_color(color) for x in self.sets])
    
    def check_color(self, color, num = None):
        num = num if num != None else 12 + color
        return all([x.get_color(color) <= num for x in self.sets])
    
    def power(self):
        return max([x.get_color(Colors.red) for x in self.sets]) * max([x.get_color(Colors.green) for x in self.sets]) * max([x.get_color(Colors.blue) for x in self.sets])

def parse_data(data):
    games = []
    for line in data.split("\n"):
        num = int(line.split(":")[0].split(" ")[1])
        game = Game(num)
        for set in line.split(": ")[1].split("; "):
            game.sets.append(Set([Cube(Colors.__dict__[x.split(" ")[1]],int(x.split(" ")[0])) for x in set.split(", ")]))
        games.append(game)
    return games


@log
@timer
def main(data):
    data = parse_data(data)

    return sum(map(lambda y: y.power(), data))




if __name__ == "__main__":
    data1 = open("./Day 2/data1", "r").read()
    data2 = open("./Day 2/data2", "r").read()

    if data1 != "":
        main(data1)
    else:
        print("No data1 found")
    if data2 != "":
        main(data2)
    else:
        print("No data2 found")