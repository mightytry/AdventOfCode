import sys
sys.path.insert(0, '.')
from tools import log

class Move:
    def __init__(self,direction,value):
        self.direction = direction
        self.value = value

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"({self.x},{self.y})"

    def __eq__(self, o: object) -> bool:
        return (self.x, self.y) == (o.x, o.y)

    def __hash__(self) -> int:
        return hash((self.x, self.y))

class Tail(Position):
    def __init__(self, head, num = 0):
        super().__init__(head.x, head.y)
        self.head = head
        self.visited = [self.position]
        self.tail = (Tail(self, num + 1)) if num < 10 else None
        

    def get_distance(self):
        return Position(abs(self.head.x - self.x), abs(self.head.y - self.y))

    @property
    def position(self):
        return Position(self.x, self.y)

    def move(self):
        distance = self.get_distance()

        if distance.x == 2 and distance.y == 2:
            self.x += (1) if self.head.x > self.x else (-1)
            self.y += (1) if self.head.y > self.y else (-1)
        elif distance.x == 2 and distance.y == 1:
            self.x += (1) if self.head.x > self.x else (-1)
            self.y = self.head.y
        elif distance.y == 2 and distance.x == 1:
            self.y += (1) if self.head.y > self.y else (-1)
            self.x = self.head.x
        elif distance.x == 2:
            self.x += (1) if self.head.x > self.x else (-1)
        elif distance.y == 2:
            self.y += (1) if self.head.y > self.y else (-1)
        else:
            return

        if isinstance(self.tail, Tail):
            self.tail.move()
            
        self.visited.append(self.position)
        

class Head(Position):
    def __init__(self):
        super().__init__(0,0)
        self.tail = Tail(self)

    def move(self, direction,value):
        for _ in range(value):
            match(direction):
                case "R":
                    self.x += 1
                case "U":
                    self.y -= 1
                case "L":
                    self.x -= 1
                case "D":
                    self.y += 1
            self.tail.move()

def parse_data(data):
    moves = []
    for move in data.split("\n"):
        moves.append(Move(move[0], int(move[2:])))
    return moves


def printt(data):
    maxx = max(data, key=lambda x: x.x).x
    maxy = max(data, key=lambda x: x.y).y
    minx = min(data, key=lambda x: x.x).x
    miny = min(data, key=lambda x: x.y).y

    for y in range(miny, maxy + 1):
        for x in range(minx, maxx + 1):
            if Position(x,y) in data:
                print("X", end="")
            else:
                print(".", end="")
        print()

@log
def main(data):
    data = parse_data(data)

    head = Head()
    for move in data:
        head.move(move.direction, move.value)



    return set(head.tail.tail.tail.tail.tail.tail.tail.tail.tail.visited).__len__()

if __name__ == "__main__":
    data1 = open("./Day 9/data1", "r").read()
    data2 = open("./Day 9/data2", "r").read()

    if data1 != "":
        main(data1)
    else:
        print("No data1 found")
    if data2 != "":
        main(data2)
    else:
        print("No data2 found")