import sys
sys.path.insert(0, '.')
from tools import log

class Card():
    CARDS = list(reversed(list(str(x) for x in ["A", "K", "Q", "J", "T", 9, 8, 7, 6, 5, 4, 3, 2, "J"])))
    def __init__(self, name):
        self.name = name

    @property
    def value(self):
        return self.CARDS.index(self.name)+1

    @classmethod
    def get_value(cls, name):
        return cls.CARDS.index(name) +1
    
    def __repr__(self) -> str:
        return self.name
    
    def __str__(self) -> str:
        return self.__repr__()

class Game():
    def __init__(self, hand, bid):
        self.hand = hand
        self.counts = {"J": 0, "hs": 0}
        for i in self.hand:
            self.counts[i.name] = self.counts.get(i.name, 0) + 1
        self.bid = bid

    @property
    def score(self):
        x = sorted(self.counts.items(), key=lambda x: x[1], reverse=True)
        v = self.hand[0].value*17**5+self.hand[1].value*17**4+self.hand[2].value*17**3+self.hand[3].value*17**2+self.hand[4].value*17
        nj = 1 if x[0][0] == "J" else 0
        if  x[nj][1] + self.counts["J"] == 5:
            v += 7*(17**6)
        elif x[nj][1] + self.counts["J"] == 4:
            v += 6*(17**6)
        elif x[0][1] == 3 and x[1][1] == 2 or (self.counts["J"] ==3 and x[1][1] == 1) or (self.counts["J"] == 2 and x[1][1] == 2) or (self.counts["J"] == 1 and (x[0][1] == 3 or (x[0][1] == 2 and x[1][1] == 2))):
            v += 5*(17**6)
        elif x[nj][1] + self.counts["J"] == 3:
            v += 4*(17**6)
        elif x[0][1] == 2 and x[1][1] == 2 or (self.counts["J"] ==2 and x[1][1] == 1) or (self.counts["J"] == 1 and (x[0][1] == 2)):
            #JJabc
            #Jabbc
            v += 3*(17**6)
        elif x[nj][1] + self.counts["J"] == 2:
            v += 2*(17**6)
        else:
            v += 1*(17**6)

        return v

def parse_data(data):
    data = [Game([Card(x) for x in i.split(" ")[0]], int(i.split(" ")[1])) for i in data.splitlines()]
    
    return data

@log
def main(data):
    data = parse_data(data)

    res = 0
    for n, i in enumerate(sorted(data, key= lambda x: x.score), 1):
        res += n*i.bid

    return res




if __name__ == "__main__":
    data1 = open("./Day 7/data1", "r").read()
    data2 = open("./Day 7/data2", "r").read()

    if data1 != "":
        main(data1)
    else:
        print("No data1 found")
    if data2 != "":
        main(data2)
    else:
        print("No data2 found")