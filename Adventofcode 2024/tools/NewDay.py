import os
import sys
from aocd.get import get_puzzle
sys.path.insert(0, '.')

def create_day(year, day):
    data = get_puzzle(day=day, year=year, block=True)
    day, name = str(day), data.title
    # open the puzzle url in the browser
    os.system(f"start https://adventofcode.com/{year}/day/{day}")
    os.mkdir(f"./Day {day}")
    for num, example in enumerate(data.examples):
        open(f"./Day {day}/example{num}", "x").write(example.input_data+"\n"+example.answer_a)
    open(f"./Day {day}/data1", "x").write(data.input_data)
    open(f"./Day {day}/{name}1.py", "x").write(open("./tools/vorlage.py", "r").read().replace("{day}", f"{day}").replace("{example_count}", f"{len(data.examples)}").replace("{year}", f"{year}"))
    open(f"./Day {day}/part2.py", "x").write(open("./tools/part2.py", "r").read().replace("{day}", f"{day}").replace("{name}", f"{name}").replace("{year}", f"{year}"))