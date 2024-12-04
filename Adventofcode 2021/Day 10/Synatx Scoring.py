import sys, itertools

from numpy import equal
sys.path.insert(0, '.')
from tools import log

chunk_character = [("(", ")"),("[","]"),("{","}"),("<",">")]
start_char = {")" : "(", "]" : "[", "}" : "{", ">" : "<"}
end_char = {"(": ")" , "[" : "]", "{" : "}" , "<" : ">"}


def load_line(data):
    lines = []
    for line in data.split('\n'):
        lines.append(line)
    return lines

#lol = '{([(<{}[<>[]}>{[]{[(<()>'
#print(lol.split('('))

def get_char_pos(line, close = 1):
    close_char_pos = []
    for pos,elm in enumerate(line):
        for check_char in chunk_character:
            if check_char[close] == elm:
                close_char_pos.append(pos)
                break
    return close_char_pos

def get_lowes_point(pos, open_chars):
    lowest = -1

    for x in range(len(open_chars)):
        if open_chars[x] < pos:
            lowest = x
        else:
            return lowest

    return lowest
    
def check_corrpted(line):
    close_chars = get_char_pos(line)
    open_chars = get_char_pos(line, 0)

    for pos in close_chars:
        char = line[pos]
        low_point = get_lowes_point(pos, open_chars)

        if line[open_chars[low_point]] != start_char[char]:
            return [" "]
            #return end_char[line[open_chars[low_point]]], char

        open_chars.remove(open_chars[low_point])

    erg = list(map(lambda x: end_char[line[x]], open_chars))

    erg.reverse()

    return erg
        
@log
def main(data):
    scores = []
    data = load_line(data)
    for line in data:
        number = 0
        for e in check_corrpted(line):
            number = number * 5 + {")": 1,"]":2,"}":3,">":4, " ": 0}[e]
        scores.append(number)
    while True:
        try: scores.remove(0)
        except ValueError: break
    print(sorted(scores))
    return sorted(scores)[int(len(scores)/2)]


data1 = open("./Day 10/data1", "r").read()
data2 = open("./Day 10/data2", "r").read()

main(data1)
main(data2)