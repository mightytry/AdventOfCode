import sys, time 
sys.path.insert(0, '.')
from tools import log
# 6:40
class Game:
    def __init__(self, id, nyh: set, wn: set):
        self.id = id
        self.nyh = nyh
        self.wn = wn
        self.winnings = 0

    def get_win(self):
        return self.nyh.intersection(self.wn)

def parse_data(data):
    for n, line in enumerate(data.splitlines()):
        l = line.replace("  ", " ").split(": ")[1].split(" | ")
        yield Game(n+1, set(int(x) for x in l[0].split(" ")), set(int(x) for x in l[1].split(" ")))

def get_winnings(game, games):
    game.winnings += 1
    for i in range(game.id, min(game.id+ len(game.get_win()), len(games))):
        get_winnings(games[i], games)


@log
def main(data):
    data = list(parse_data(data))

    t = time.time()
    for game in data:
        get_winnings(game, data)

    print(time.time()-t)

    return sum(x.winnings for x in data)




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