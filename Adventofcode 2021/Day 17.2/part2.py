import sys, os
sys.path.insert(0, '.')


open("./Day 17.2/Trick Shot2.py", "x").write(open("./Day 17.2/Trick Shot1.py", "r").read())

os.remove("./Day 17.2/part2.py")