import sys, progressbar
sys.path.insert(0, '.')
from tools import log

class Item:
    def __init__(self, monkey, value):
        self.monkey = monkey
        self.value = value
        self.worry_level = value
        self.worry_levels = set()

    @property
    def valid(self):
        return self.worry_level % self.monkey.test.value == 0

    def inspect(self):
        self.monkey.operation.eval(self)
        self.monkey.test.eval(self)

    def __repr__(self):
        return f"{self.value}"

    def __str__(self):
        return f"{self.value}"

class Test:
    def __init__(self, monkey, value, true_monkey, false_monkey):
        self.monkey = monkey
        self.value = value
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey

    def eval(self, i1):
        if i1.valid:
            self.monkey - i1
            self.true_monkey + i1
        else:
            self.monkey - i1
            self.false_monkey + i1
            
class Items:
    def __init__(self, monkey, value):
        self.monkey = monkey
        self.items = [Item(monkey, int(item)) for item in value]

    def add(self, item):
        item.monkey = self.monkey
        self.items.append(item)

    def remove(self, item):
        self.items.remove(item)

    def __repr__(self):
        a = (", ".join([str(item) for item in self.items]))
        return f"{a}"

class Operation:
    def __init__(self, monkey, op):
        self.monkey = monkey
        self.modulus = 0
        self.op = op

    def eval(self, i1):
        i1.worry_level = int(int(eval(f"{self.op}", {"old": i1.worry_level})))%self.modulus
        

class Monkey:
    def __init__(self, name, items, operation, divisible_value, true_monkey, false_monkey):
        self.name = name
        self.items = Items(self, items)
        self.operation = Operation(self, operation)
        self.test = Test(self, divisible_value, true_monkey, false_monkey)

        self.count = 0

    def eval(self):
        for item in list(self.items.items):
            item.inspect()
            self.count += 1

    def __add__(self, other):
        if isinstance(other, Item):
            self.items.add(other)

    def __sub__(self, other):
        if isinstance(other, Item):
            self.items.remove(other)

    def __repr__(self):
        return f"{self.name}: {self.items}"


def parse_data(data):
    monkeys = []
    data = data.splitlines()
    for index,line in enumerate(data):
        if line.startswith("Monkey"):
            name = line.split(":")[0]
            items = data[index+1].split("Starting items: ")[1].split(", ")
            operation = data[index+2].split("Operation: new = ")[1]
            divisible_value = int(data[index+3].split("Test: divisible by ")[1])
            true_monkey = int(data[index+4].split("If true: throw to monkey ")[1])
            false_monkey = int(data[index+5].split("If false: throw to monkey ")[1])
            monkeys.append(Monkey(name,items,operation,divisible_value,true_monkey,false_monkey))

    for monkey in monkeys:
        monkey.test.true_monkey = monkeys[monkey.test.true_monkey]
        monkey.test.false_monkey = monkeys[monkey.test.false_monkey]

    return monkeys

def set_divisor(monkys:list[Monkey]):
    v = 1
    for monkey in monkys:
        v *= monkey.test.value

    for monkey in monkys:
        monkey.operation.modulus = v

@log
def main(data):
    data:list[Monkey] = parse_data(data)

    # get divisor
    set_divisor(data)

    # add widget to show count
    pg = progressbar.ProgressBar(maxval=10000, widgets=[progressbar.Counter(), ' ', progressbar.Bar(), ' ', progressbar.Percentage(), ' ', progressbar.ETA()])
    pg.start()

    for x in range(10000):
        for monkey in data:
            monkey.eval()
        pg.update(x+1)

    pg.finish()

    data = sorted(data, key=lambda x: x.count, reverse=True)

    return data[0].count * data[1].count




if __name__ == "__main__":
    data1 = open("./Day 11/data1", "r").read()
    data2 = open("./Day 11/data2", "r").read()

    if data1 != "":
        main(data1)
    else:
        print("No data1 found")
    if data2 != "":
        main(data2)
    else:
        print("No data2 found")