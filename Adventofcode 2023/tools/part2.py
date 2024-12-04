import sys, os
sys.path.insert(0, '.')


open("./Day {day}/{name}2.py", "x").write(open("./Day {day}/{name}1.py", "r").read())

os.remove("./Day {day}/part2.py")