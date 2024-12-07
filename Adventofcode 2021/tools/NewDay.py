import os
import sys
sys.path.insert(0, '.')

day, name = input("Day + Name: ").split(": ")
day = day.replace("Day ", "")

os.mkdir(f"./Day {day}")
open(f"./Day {day}/data1", "x")
open(f"./Day {day}/data2", "x")
open(f"./Day {day}/test.py", "x")
open(f"./Day {day}/{name}1.py", "x").write(open("./tools/vorlage.py", "r").read().replace("{day}", f"{day}"))
open(f"./Day {day}/part2.py", "x").write(open("./tools/part2.py", "r").read().replace("{day}", f"{day}").replace("{name}", f"{name}"))