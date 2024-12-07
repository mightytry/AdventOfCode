import sys
sys.path.insert(0, '.')
from tools import log


class Seat():
    def __init__(self, code):
        self.code = code
        
        self.row = self.get_row()
        self.column = self.get_column()
        self.id = self.row * 8 + self.column

    def get_row(self):
        row = 0
        for i in range(7):
            if self.code[i] == "B":
                row += 2**(6-i)
        return row

    def get_column(self):
        column = 0
        for i in range(3):
            if self.code[7+i] == "R":
                column += 2**(2-i)
        return column
    

def parse_data(data):
    return [Seat(x) for x in data.splitlines()]

@log
def main(data):
    data = parse_data(data)

    max_id = max([x.id for x in data])

    for i in range(max_id):
        if i not in [x.id for x in data] and i-1 in [x.id for x in data] and i+1 in [x.id for x in data]:
            return i



if __name__ == "__main__":
    data1 = open("./Day 5/data1", "r").read()
    data2 = open("./Day 5/data2", "r").read()

    if data1 != "":
        main(data1)
    else:
        print("No data1 found")
    if data2 != "":
        main(data2)
    else:
        print("No data2 found")