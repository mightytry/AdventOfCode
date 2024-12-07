import sys, numpy
sys.path.insert(0, '.')
from tools import log

wins = []


def assamble_array(code_lines):
    code_lines


def parse_data(data:str):
    bingo_fields = []
    bingo_numerbs = []

    parsed_data = data.split("\n\n")
    bingo_numerbs = parsed_data.pop(0).split(",")

    for x in parsed_data:
        array = []
        for y in x.replace("  ", " ").split("\n"):
            array.append(y.removeprefix(" ").split(" "))

        bingo_fields.append(array)

    return numpy.array(bingo_fields), bingo_numerbs

@log
def main(data):
    bingo_fields, bingo_numerbs = parse_data(data)
    index = 0

    while not check_win(bingo_fields.tolist()):
        bingo_fields[bingo_fields == (bingo_numerbs[index])] = -1
        index += 1

    return add_unmarked(bingo_fields.tolist()[wins[-1]]) * int(bingo_numerbs[index-1])

def check_win(bingo_fields):
    global wins

    for num, field in enumerate(bingo_fields):
        if check_all(field):
            if num not in wins:
                wins.append(num)

            if len(wins) == len(bingo_fields):
                return True
    return False
        
def check_all(field):
    return is_horizontal(field) or is_vertical(field)

def is_horizontal(bingo_field): # 2 dimmensionales Array
    for row in bingo_field:
        index_of_drawn_numbers = 0
        for elm in row:
            if elm == "-1":
                index_of_drawn_numbers += 1
        if (index_of_drawn_numbers == 5):
            return True    
    return False   
    
def is_vertical(bingo_field): # 2 dimmensionales Array
    for column in range(len(bingo_field)):
        index_of_drawn_numbers = 0
        for row in range(len(bingo_field[column])):
            if bingo_field[row][column] == "-1":
                index_of_drawn_numbers += 1
        if index_of_drawn_numbers == 5:
            return True    
    return False   

def add_unmarked(field):
    mysum = 0
    for row in field:
        for number in row:
            if number != "-1":
                mysum += int(number)
    return mysum

"""
    [[
        [],  <---
        [],
        [],
        [],
        []
    ], [
        [],  <---
        [],
        [],
        [],
        []
    ], [
        [],  <---
        [],
        [],
        [],
        []
    ], [
        [],  <---
        [],
        [],
        [],
        []
    ], [
        [],  <---
        [],
        [],
        [],
        []
    ]]
"""

data1 = open("./Day 4/data1", "r").read()
data2 = open("./Day 4/data2", "r").read()

main(data1)
wins = []
main(data2)