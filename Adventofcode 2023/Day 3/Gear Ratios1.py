import sys
sys.path.insert(0, '.')
from tools import log

class Position():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Part():
    def __init__(self, char, pos, num) -> None:
        self.char = char
        self.pos = pos
        self.num = num
        num.add_part(self)

class Number():
    def __init__(self):
        self.parts = []
        self.symbols = set()

    @property
    def number(self):
        return int("".join([part.char for part in self.parts]))
    
    def add_part(self, part):
        self.parts.append(part)

    def __repr__(self) -> str:
        return f'N({self.number})'
    
    def __str__(self) -> str:
        return str(self.number)
    

class Symbol():
    def __init__(self, char, pos) -> None:
        self.char = char
        self.pos = pos
        self.numbers = set()

    def evaluate(self, board):
        for x in range(self.pos.x-1, self.pos.x+2):
            for y in range(self.pos.y-1, self.pos.y+2):
                if x == self.pos.x and y == self.pos.y:
                    continue
                if x < 0 or y < 0:
                    continue
                if x >= len(board[0]) or y >= len(board):
                    continue
                if isinstance(board[y][x], Part):
                    self.numbers.add(board[y][x].num)
                    board[y][x].num.symbols.add(self)

    def __repr__(self) -> str:
        return f'S({self.char})'
    
    def __str__(self) -> str:
        return self.char

def parse_data(data):
    board = []
    nums = []
    symbols = []
    for y, line in enumerate(data.splitlines()):
        num = None
        board.append([])
        for x, char in enumerate(line):
            if char.isdigit():
                if num is None:
                    num = Number()
                    nums.append(num)
                board[-1].append(Part(char, Position(x, y), num))
                continue
            elif char != ".":
                symbol = Symbol(char, Position(x, y))
                board[-1].append(symbol)
                symbols.append(symbol)
            else:
                board[-1].append(None)
            num = None

    for symbol in symbols:
        symbol.evaluate(board)

    return board, nums, symbols

@log
def main(data):
    data = parse_data(data)

    return sum(map(lambda x: x.number, filter(lambda x: len(x.symbols) > 0, data[1])))






if __name__ == "__main__":
    data1 = open("./Day 3/data1", "r").read()
    data2 = open("./Day 3/data2", "r").read()

    if data1 != "":
        main(data1)
    else:
        print("No data1 found")
    if data2 != "":
        main(data2)
    else:
        print("No data2 found")