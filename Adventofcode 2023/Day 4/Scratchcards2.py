import sys
sys.path.insert(0, '.')
from tools import log, timer
# 6:40
class Game:
    def __init__(self, id, nyh: set, wn: set):
        self.id = id
        self.nyh = nyh
        self.wn = wn
        self.parents = set()
        self.amount = 0

    def gen_amount(self):
        for parent in self.parents:
            if parent.amount == 0:
                parent.gen_amount()
        self.amount = 1+sum(x.amount for x in self.parents)

    def get_win(self):
        return self.nyh.intersection(self.wn)

def parse_data(data):
    for n, line in enumerate(data.splitlines()):
        l = line.replace("  ", " ").split(": ")[1].split(" | ")
        yield Game(n+1, set(int(x) for x in l[0].split(" ")), set(int(x) for x in l[1].split(" ")))

def get_winnings(game, games):
    for i in range(game.id, min(game.id+ len(game.get_win()), len(games))):
        if game in games[i].parents:
            continue
        games[i].parents.add(game)
        get_winnings(games[i], games)


@log
def main(data):
    data = list(parse_data(data))

    for game in data:
        get_winnings(game, data)
        game.gen_amount()

    return sum([x.amount for x in data])




if __name__ == "__main__":
    data1 = open("./Day 4/data1", "r").read()
    data2 = open("./Day 4/data2", "r").read()

    if data1 != "":
        main(data1)
    else:
        print("No data1 found")
    if data2 != "":
        main(data2)
    else:
        print("No data2 found")