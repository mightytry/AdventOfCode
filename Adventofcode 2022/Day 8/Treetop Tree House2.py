import sys
sys.path.insert(0, '.')
from tools import log

class Position:
    def __init__(self, x:int, y:int) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Position({self.x}, {self.y})"

class Tree:
    def __init__(self, height:int, pos:Position, forest) -> None:
        self.height = height
        self.pos = pos
        self.forest = forest

    def __repr__(self) -> str:
        return f"Tree({self.height}, {self.pos})"

    def __str__(self) -> str:
        return f"Tree({self.height}, {self.pos})"

    def __lt__(self, o: object) -> bool:
        if isinstance(o, Tree):
            return self.height < o.height
        else:
            return self.height < o
    
    @property
    def distance(self):
        row1 = list(reversed(self.forest.grid[self.pos.y][:self.pos.x]))
        row2 = self.forest.grid[self.pos.y][self.pos.x+1:]
        col1 = list(reversed([row[self.pos.x] for row in self.forest.grid[:self.pos.y]]))
        col2 = [row[self.pos.x] for row in self.forest.grid[self.pos.y+1:]]

        distances = []
        for i in (row1, row2, col1, col2):
            if i == []:
                distances.append("1")
                continue
            count = 0
            for elm in i:
                if elm < self:
                    count += 1
                else:
                    count += 1
                    break
            if count != 0:
                distances.append(str(count))

        if distances == []:
            return 0
        e = eval("*".join(distances))

        return e
            
        

class Forest:
    def __init__(self) -> None:
        self.grid = []

    def add_row(self, row):
        self.grid.append(row)

    def get_visible(self):
        count = max([max(row, key= lambda x: x.distance) for row in self.grid], key= lambda x: x.distance)
        return count.distance

def parse_data(data):
    forest = Forest()
    for y, line in enumerate(data.splitlines()):
        trees = []
        for x,height in enumerate(line):
            tree = Tree(int(height),Position(x,y),forest)
            trees.append(tree)
        forest.add_row(trees)
    return forest

@log
def main(data):
    forest = parse_data(data)

    return forest.get_visible()



if __name__ == "__main__":
    data1 = open("./Day 8/data1", "r").read()
    data2 = open("./Day 8/data2", "r").read()

    if data1 != "":
        main(data1)
    else:
        print("No data1 found")
    if data2 != "":
        main(data2)
    else:
        print("No data2 found")
