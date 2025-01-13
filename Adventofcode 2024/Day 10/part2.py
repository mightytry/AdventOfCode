import sys, os
from aocd.get import get_puzzle
sys.path.insert(0, '.')


open("./Day 10/Hoof It2.py", "x").write(open("./Day 10/Hoof It1.py", "r").read().replace('print("Got:", main([x.strip() for x in example[0:-1]]), "Expected:", example[-1].strip().split(",")[0])', 'print("Got:", main([x.strip() for x in example[0:-1]]), "Expected:", example[-1].strip().split(",")[1])').replace('SUBMIT = True', 'SUBMIT = False'))

data = get_puzzle(day=10, year=2024, block=True)
# open the puzzle url in the browser
os.system("start https://adventofcode.com/2024/day/10")
for num, example in enumerate(data.examples):
    open(f"./Day 10/example{num}", "w").write(example.input_data+"\n"+str(-1 if example.answer_a == None else example.answer_a)+","+ str(-1 if example.answer_b == None else example.answer_b))

os.remove("./Day 10/part2.py")