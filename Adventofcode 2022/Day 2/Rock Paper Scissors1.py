import sys
sys.path.insert(0, '.')
from tools import log

class ID:
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

class Round:
    def __init__(self, my_play:ID, enemy_play:ID):
        self.my_play = my_play
        self.enemy_play = enemy_play
    
    @property 
    def winner(self):
        if  (self.my_play == ID.PAPER and self.enemy_play == ID.ROCK) or \
            (self.my_play == ID.ROCK and self.enemy_play == ID.SCISSORS) or \
            (self.my_play == ID.SCISSORS and self.enemy_play == ID.PAPER):
            return 2 #myplayer
        elif (self.my_play == ID.ROCK and self.enemy_play == ID.PAPER) or \
            (self.my_play == ID.SCISSORS and self.enemy_play == ID.ROCK) or \
            (self.my_play == ID.PAPER and self.enemy_play == ID.SCISSORS):
            return 0 #enemy_player
        elif (self.my_play == ID.ROCK and self.enemy_play == ID.ROCK) or \
            (self.my_play == ID.SCISSORS and self.enemy_play == ID.SCISSORS) or \
            (self.my_play == ID.PAPER and self.enemy_play == ID.PAPER):
            return 1 #in draw

class Player:
    def __init__(self, rounds:list[Round], invert = False):
        self.rounds = rounds
        self.invert = invert
        
    @property
    def score(self):
        scores = []

        for round in self.rounds:
            scores.append(((round.winner * 3) if self.invert == False else (abs(round.winner -2) *3)) + (round.my_play if self.invert == False else round.enemy_play))

        return scores

def parse_data(data):
    rounds = []

    for line in data.splitlines():
        rounds.append(Round(["A", "B", "C"].index(line[0])+1, ["X", "Y", "Z"].index(line[2])+1))
        
    return rounds

@log
def main(data):
    data = parse_data(data)

    player2 = Player(data, True)

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