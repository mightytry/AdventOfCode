import sys, os
sys.path.insert(0, '.')


open("./Day 23/Amphipod2.py", "x").write(open("./Day 23/Amphipod1.py", "r").read())

os.remove("./Day 23/part2.py")