from collections import Counter
import sys
sys.path.insert(0, '.')
from tools import log

def parse_data(data):
    data = data.split("\n\n")
    polymer = list(data[0])
    rules = {}
    polymers = {}

    for rule in data[1].split("\n"):
        rule = rule.split(" -> ")
        rules[rule[0]] = rule[1]
        polymers[rule[0]] = 0

    for step in range(len(polymer)-1):
        polymers[polymer[step] + polymer[step+1]] += 1

    return polymers, rules, polymer

def update_polymer(polymer, rules):
    new_polymer = dict(polymer)
    for pol in polymer:
        if pol in list(rules.keys()):
            f = pol[0] + rules[pol]
            s = rules[pol] + pol[1]

            new_polymer[f] += polymer[pol]
            new_polymer[s] += polymer[pol]

            new_polymer[pol] -= polymer[pol]
        
    
    return new_polymer

@log
def main(data):
    data = parse_data(data)
    polymer = data[0]
    for x in range(40):
        polymer = update_polymer(polymer, data[1])
        
    l = {data[2][-1]: 1}
    for x in polymer:
        if l.get(x[0]) == None:
            l[x[0]] = polymer[x]
        else:
            l[x[0]] += polymer[x]

    sor = sorted(l.items(), key= lambda x: x[1], reverse=True)

    return sor[0][1] - sor[-1][1]


data1 = open("./Day 14/data1", "r").read()
data2 = open("./Day 14/data2", "r").read()

main(data1)
main(data2)