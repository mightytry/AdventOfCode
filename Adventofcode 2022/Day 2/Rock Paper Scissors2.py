import sys
sys.path.insert(0, '.')
from tools import log

class ID:
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

class Round:
    def __init__(self, my_play:ID, ending:int):#0 loose 1 draw 2 win
        self.my_play = my_play
        self.ending = ending
    
    @property
    def enemy_play(self):
        match (self.ending):
            case 0:
                match(self.my_play):
                    case ID.ROCK:
                        return ID.SCISSORS
                    case ID.PAPER:
                        return ID.ROCK
                    case ID.SCISSORS:
                        return ID.PAPER
            case 1:
                return self.my_play
            case 2:
                match (self.my_play):
                    case ID.ROCK:
                        return ID.PAPER
                    case ID.PAPER:
                        return ID.SCISSORS
                    case ID.SCISSORS:
                        return ID.ROCK

    @property 
    def winner(self):
        return self.ending

class Player:
    def __init__(self, rounds:list[Round]):
        self.rounds = rounds
        
    @property
    def score(self):
        scores = []

        for round in self.rounds:
            scores.append((round.winner *3) + round.enemy_play)

        return scores

def parse_data(data):
    rounds = []

    for line in data.splitlines():
        rounds.append(Round(["A", "B", "C"].index(line[0])+1, ["X", "Y", "Z"].index(line[2])))
        
    return rounds

@log
def main(data):
    data = parse_data(data)

    player2 = Player(data)

    return sum(player2.score)

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