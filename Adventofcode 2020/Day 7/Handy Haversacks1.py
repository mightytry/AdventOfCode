import sys
sys.path.insert(0, '.')
from tools import log

class Bag:
    def __init__(self,color_name,contain_bags) -> None:
        self.color_name = color_name
        self.contain_bags = contain_bags
    def __repr__(self) -> str:
        contain_bags = ""
        for elm in self.contain_bags:
            contain_bags = contain_bags + str(elm[0]) + " " + str(elm[1]) + ","
        return self.color_name + "|" + contain_bags 

def parse_data(data):
    data_bags = []
    for line in data.splitlines():
        color_name = line.split(" bags contain ")[0]
        contain_bags = []
        for contain_bag_string in line.split("bags contain ")[1].split(", "):
            string_len = len(contain_bag_string.split(" "))
            if (contain_bag_string.split(" ")[0] == 'no'):
                continue
            number = int(contain_bag_string.split(" ")[0])
            contain_bag = contain_bag_string.split(" ")[1:(string_len-1)]
            if len(contain_bag) >= 2:
                contain_bag = contain_bag[0] + " " + contain_bag[1]
            contain_bags.append((number,contain_bag))
        data_bags.append(Bag(color_name,contain_bags))
    return data_bags

bags_contain_shiny_gold = []
def get_bag_in_bag(data):
    for bag in data:
        if bag.contain_bags == []:
            continue
        for substance in bag.contain_bags:
            if (substance[1] == "shiny gold" or substance[1] in bags_contain_shiny_gold) and bag.color_name not in bags_contain_shiny_gold:
                bags_contain_shiny_gold.append(bag.color_name)
                get_bag_in_bag(data)

@log
def main(data):
    data = parse_data(data)
    get_bag_in_bag(data)
    return len(bags_contain_shiny_gold)

if __name__ == "__main__":
    data1 = open("./Day 7/data1", "r").read()
    data2 = open("./Day 7/data2", "r").read()

    if data1 != "":
        main(data1)
    else:
        print("No data1 found")
    if data2 != "":
        main(data2)
    else:
        print("No data2 found")