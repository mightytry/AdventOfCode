import sys
sys.path.insert(0, '.')
from tools import log

class Point():
    def __repr__(self):
        return str(self.active)

    def __init__(self, x, y, active):
        self.x = int(x)
        self.y = int(y)
        self.active = active


def fold(axis, folding_point, paper):
    offset = int(folding_point)

    if axis == "y":
        for y in range(offset):
            try:
                for x, point in enumerate(paper[offset+y+1]):
                    if paper[offset-y-1][x].active == False:
                        paper[offset-y-1][x].active = point.active
            except IndexError: pass
        paper = paper[:offset]

    elif axis == "x":
        for y in range(len(paper)):
            try:
                for x in range(offset):
                    if paper[y][offset-x-1].active == False:
                        paper[y][offset-x-1].active = paper[y][offset+x+1].active
                paper[y] = paper[y][:offset]
            except IndexError: paper[y] = paper[y][:offset]

    return paper



def parse_data(data):
    data = data.split("\n\n")

    #--------------------Operations--------------------#
    operations = []

    for x in data[1].split("\n"):
        operations.append(x.split(" ")[2].split("="))


    #--------------------Operations--------------------#

    #--------------------Points--------------------#
    points = []

    for p in data[0].split("\n"):
        points.append(p.split(","))

    max_x = int(sorted(points, key=lambda x: int(x[0]))[-1][0])
    max_y = int(sorted(points,key=lambda x: int(x[1]))[-1][1])

    paper = []

    for y in range(max_y + 1):
        row = []
        for x in range(max_x + 1):
            row.append(Point(x, y, False))
        paper.append(row)

    for p in points:
        paper[int(p[1])][int(p[0])].active = True
    #--------------------Points--------------------#

    return paper, operations

def count(paper):
    c = 0

    for y in paper:
        for x in y:
            if x.active == True:
                c += 1

    return c


@log
def main(data):
    data = parse_data(data)
    paper = data[0]

    for o in data[1]:
        #print(str(paper).replace("], [", "\n").replace("True", "#").replace("False", ".")[2:-2].replace(",", " "), "\n\n")
        paper = fold(*o, paper)

    return str(paper).replace("], [", "\n").replace("True", "█").replace("False", " ")[2:-2].replace(", ", "") + "\n"


data1 = open("./Day 13/data1", "r").read()
data2 = open("./Day 13/data2", "r").read()

main(data1)
main(data2)