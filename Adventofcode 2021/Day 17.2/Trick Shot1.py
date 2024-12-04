import sys
sys.path.insert(0, '.')
from tools import log

#data = []

def parse_data(data):
    target_pos = []
    data = data.replace("target area: x=", "").replace("y=", "").split(", ")
    target_pos.append(list(map(lambda a: a.split(".."),data)))
    return make_int(target_pos[0])

def make_int(data):
    for x,elmx in enumerate(data):
        for y,elmy in enumerate(elmx):
            data[x][y] = int(elmy)
    return data

def try_velocity(target_pos,max_try):
    for vx in range(max_try):
        for vy in range(max_try):

            x_pos = 0
            x_delta  = 0
            y_pos = 0
            y_delta = 0
            while not (x_pos > target_pos[0][1]) or not (y_pos < target_pos[1][0]):
                if vx + x_delta >= 0:
                    x_pos = x_pos + vx + x_delta
                    x_delta -= 1
                    print(x_pos)

                y_pos = y_pos + vy + y_delta
                y_delta -= 1

                if x_pos >= target_pos[0][0] and  x_pos <=target_pos[0][1] and y_pos >= target_pos[1][0] and  y_pos <=target_pos[1][1]:
                    return x_pos, y_pos
            return 0,0



@log
def main(data):
    target_pos = parse_data(data)

    return try_velocity(target_pos,10)
    return target_pos


data1 = open("./Day 17.2/data1", "r").read()
data2 = open("./Day 17.2/data2", "r").read()

main(data1)
main(data2)