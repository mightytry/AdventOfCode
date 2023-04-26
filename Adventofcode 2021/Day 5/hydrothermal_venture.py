import sys
from collections import Counter
sys.path.insert(0, '.')
from tools import log


class line:
    def __init__(self, coords:list[int]) -> None:
        x1, y1, x2, y2 = coords
        self.x1, self.y1, self.x2, self.y2 = int(x1), int(y1), int(x2), int(y2)
        self.is_diagonal = False

        if self.x1 < self.x2:
            self.range_x = range(self.x1, self.x2+1)
        else:
            self.range_x = range(self.x2, self.x1+1)

        if self.y1 < self.y2:
            self.range_y = range(self.y1, self.y2+1)
        else:
            self.range_y = range(self.y2, self.y1+1)

    def __str__(self) -> str:
        return f"(({self.x1}, {self.y1}), ({self.x2}, {self.y2}))"
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def is_valid(self):
        if self.x1 == self.x2 or self.y1 == self.y2:
            return True
        elif (self.y1 - self.y2)/(self.x1 - self.x2) == 1 or (self.y1 - self.y2)/(self.x1 - self.x2) == -1:
            self.is_diagonal = True
            return True
        return False


def parse_data(data):
    lines = []
    
    for x in data.replace(" -> ", ",").split("\n"):
        lines.append(line(x.split(",")))
    
    return lines

@log
def main(data):
    thelist = check(parse_data(data))

    thelist = Counter(thelist)

    point_counter = len(list(filter(lambda x: thelist[x] > 1, thelist)))
    
    return point_counter


def check(coordinates):
    thelist = []
    for line in coordinates:
        if line.is_valid():
            if line.is_diagonal:
                for num in range(len(line.range_y)):
                    thelist.append((line.range_x[(num if int((line.y1 - line.y2)/(line.x1 - line.x2)) == 1 else num +1) * int((line.y1 - line.y2)/(line.x1 - line.x2))], line.range_y[num])) # 3,1 1,3 -> 1,3 1,3
            else:
                if len(line.range_x) == 1:
                    for y in line.range_y:
                        thelist.append((line.x1, y))
                if len(line.range_y) == 1:
                    for x in line.range_x:
                        thelist.append((x, line.y1))
            
    return thelist
    

data1 = open("./Day 5/data1", "r").read()
data2 = open("./Day 5/data2", "r").read()

main(data1)
main(data2)