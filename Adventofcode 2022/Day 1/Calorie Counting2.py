import sys
sys.path.insert(0, '.')
from tools import log

class Calories:
    def __init__(self, calories:list[int]):
        self.calories = calories # list of calories

    @property
    def value(self):
        return sum(self.calories)

    def __str__(self):
        return f"{self.value()}"
        
    def __repr__(self):
        return self.__str__()

    def __lt__(self, __o: object) -> bool:
        return self.value < __o.value
    
    def __gt__(self, __o: object) -> bool:
        return self.value > __o.value

    def __eq__(self, __o: object) -> bool:
        return self.value == __o.value

    def __le__(self, __o: object) -> bool:
        return self.value <= __o.value

    def __ge__(self, __o: object) -> bool:
        return self.value >= __o.value

    def __ne__(self, __o: object) -> bool:
        return self.value != __o.value

def parse_data(data):
    
    data = data.split("\n\n")

    return [Calories([int(x) for x in d.splitlines()]) for d in data]

def get_biggest(calories:list[Calories]):
    biggest1 = max(calories)
    calories.remove(biggest1)
    biggest2 = max(calories)
    calories.remove(biggest2)
    biggest3 = max(calories)

    return biggest1.value + biggest2.value + biggest3.value

@log
def main(data):
    data = parse_data(data)

    return get_biggest(data)


if __name__ == "__main__":
    data1 = open("./Day 1/data1", "r").read()
    data2 = open("./Day 1/data2", "r").read()

    if data1 != "":
        main(data1)
    else:
        print("No data1 found")
    if data2 != "":
        main(data2)
    else:
        print("No data2 found")