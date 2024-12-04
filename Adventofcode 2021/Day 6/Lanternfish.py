import sys
sys.path.insert(0, '.')
from tools import log
from collections import Counter

def subtrakt_one(dictonray):
    new_dictonary = {"6": 0, "8": 0}
    for key, value in sorted(dictonray.items(), reverse=True):
        if key == "0":
            new_dictonary["6"] += value
            new_dictonary["8"] += value
            continue
        
        new_dictonary[str(int(key) -1)] = value

    #print(new_dictonary)
    return new_dictonary
    

@log
def main(data):
    iterations = 10

    dictonray = return_data(data)
    
    for x in range(iterations):
        dictonray = subtrakt_one(dictonray)


    return sum(dictonray.values())

def return_data(data):
    return Counter(data.split(','))


data1 = open("./Day 6/data1", "r").read()
data2 = open("./Day 6/data2", "r").read()

main(data1)
main(data2)