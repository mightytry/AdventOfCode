import sys, copy
sys.path.insert(0, '.')
from tools import log

class Pixel():
    def __init__(self, x, y, lit = False) -> None:
        self.x = x
        self.y = y
        self.lit = lit

    @property
    def binary(self):
        return self.lit * 1
    
    def __repr__(self) -> str:
        return "#" if self.lit else "."

class Algorithm():
    def __init__(self, data:list[Pixel]) -> None:
        self.data = data
        self.empty = data[0].lit
        self.full = data[-1].lit

    def at_binary(self, pos:str) -> Pixel:
        num = int(pos, 2)
        return self.data[num]

class Image():
    def __init__(self, algo:Algorithm, data:list[list[Pixel]]) -> None:
        self.algo = algo
        self.data = data
        self.current = False

    def loop(self):
        self.data = [[Pixel(x+1, y+1, lit = self.calc(x, y)) for x in range(-1, len(self.data[0])+1)] for y in range(-1, len(self.data)+1)]
        # After the first loop, the data is now 2 pixels bigger in each direction
        # And if the algorithms first pixel is lit, all pixels in data are lit
        if self.algo.empty and not self.current:
            self.current = True
        elif not self.algo.full and self.current:
            self.current = False


    def calc(self, x, y):
        bin = ""

        for _y in range(-1, 2):
            for _x in range(-1, 2):
                try:
                    if x<0 or y<0:
                        raise IndexError

                    bin += str(self.data[y+ _y][x+ _x].binary)
                except IndexError:
                    bin += str(int(self.current))

        return self.algo.at_binary(bin).lit
    
    def count(self):
        return sum([sum([pixel.binary for pixel in line]) for line in self.data])
                

    def __repr__(self) -> str:
        return f'Image({self.data})'


def parse_data(data):
    data = data.splitlines()
    algo = Algorithm([Pixel(x, 0, lit = True if char == "#" else False) for x, char in enumerate(data[0])])

    img = Image(algo, [[Pixel(x+1, y+1, lit = True if char == "#" else False) for x, char in enumerate(line)] for y, line in enumerate(data[2:])])


    img.data.insert(0, [Pixel(x, 0, lit = False) for x in range(len(img.data[0]))])
    img.data.append([Pixel(x, len(img.data), lit = False) for x in range(len(img.data[0]))])
    for line in img.data:
        line.insert(0, Pixel(0, line[0].y, lit = False))
        line.append(Pixel(len(line), line[0].y, lit = False))

    return img

@log
def main(data):
    img = parse_data(data)

    img.loop()
    img.loop()

    return img.count()




if __name__ == "__main__":
    data1 = open("./Day 20/data1", "r").read()
    data2 = open("./Day 20/data2", "r").read()

    if data1 != "":
        main(data1)
    else:
        print("No data1 found")
    if data2 != "":
        main(data2)
    else:
        print("No data2 found")