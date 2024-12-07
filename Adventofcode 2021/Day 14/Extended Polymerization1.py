from collections import Counter
import sys
sys.path.insert(0, '.')
from tools import log

def parse_data(data):
    data = data.split("\n\n")
    polymer= list(data[0])
    rules = {}

    for rule in data[1].split("\n"):
        rule = rule.split(" -> ")
        rules[rule[0]] = rule[1]

    return polymer, rules

def update_polymer(polymer, rules):
    new_polymer = [polymer[0]]

    for step in range(len(polymer)-1):
        if (char := rules.get(polymer[step] + polymer[step+1])):
            new_polymer.append(char)
        new_polymer.append(polymer[step+1])
    
    return new_polymer

@log
def main(data):
    data = parse_data(data)
    polymer = data[0]

    for x in range(40):
        polymer = update_polymer(polymer, data[1])
        print(x)

    sor = sorted((Counter(polymer)).items(), key= lambda x: x[1], reverse=True)

    return sor[0][1] - sor[-1][1]


data1 = open("./Day 14/data1", "r").read()
data2 = open("./Day 14/data2", "r").read()

main(data1)
main(data2)