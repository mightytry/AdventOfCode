import sys
sys.path.insert(0, '.')
from tools import log

class Player():
    def __init__(self, start):
        self.pos = start
        self.score = 0

    def move(self, roll):
        self.pos = (roll+self.pos-1) % 10 +1
        self.score += self.pos


def parse_data(data):
    data = data.splitlines()
    players = [Player(int(data[0].split(": ")[1])), Player(int(data[1].split(": ")[1]))]

    return players

@log
def main(data):
    data = parse_data(data)
    p1 , p2 = data
    m = 1
    while p1.score < 1000 and p2.score < 1000:
        p1.move(m + m+1 + m+2)
        if p1.score >= 1000:
            m += 3
            break
        p2.move(m+3 + m+4 + m+5)
        m += 6

    return (m-1) *  min(p1.score, p2.score)



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


