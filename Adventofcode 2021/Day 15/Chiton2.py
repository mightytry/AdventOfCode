import copy
import math
import sys
sys.path.insert(0, '.')
from tools import log

class Vertex():
    def __init__(self, distance,x,y):
        self.cost = math.inf
        self.distance = distance
        self.prev = None
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return str([self.cost,self.distance,self.prev,self.x,self.y])

def parse_data(data):
    l = len(data.split('\n'))
    field = []
    for y,data_line in enumerate(data.split('\n')*5): 
        line = []
        for x,data_char in enumerate([list(data_line)]*5):
            for n, m in enumerate(data_char):
                a = (int(m) + x + int(y/(l)))
                line.append(Vertex(a if (a < 10) else (a-9),x*(len(data_line))+n,y))
        field.append(line)

    field[0][0].cost = 0

    return field


def get_costs(field,point):
    new_field = []
    finish = field[len(field)-1][len(field)-1]

    while True:
        
        for n in get_neighbors(field, point.x, point.y):
            if n != None:
                neighbor = field[n[1]][n[0]]
                a = point.cost + neighbor.distance
                
                if neighbor.cost > a:
                    neighbor.cost = a
                    neighbor.prev = point
                    new_field.append(neighbor)

        point = min(new_field, key=lambda x: x.cost)
        new_field.remove(point)
        if point is finish:
            break
       
    return field
        
def get_smallest_not_visited_point(new_field):
    return min(new_field, key= lambda x: x.cost)

def get_neighbors(field,x,y):
    for elm in ((-1,0),(1,0),(0,-1),(0,1)):
        xn = x+elm[0]
        yn = y+elm[1]
        yield (xn,yn) if xn >= 0 and xn < len(field[0]) and yn < len(field) and yn >= 0 else None

def get_path(point):
    path = []
    while point.prev is not None:
        path.append(point)
        point = point.prev

    return path

def get_sum(path):
    sum = 0
    
    for point in path:
        sum += point.distance
    
    return sum
@log
def main(data):
    data = parse_data(data)
    data = (get_costs(data,data[0][0]))

    print("Done!")
    
    return get_sum(get_path(data[len(data)-1][len(data[0])-1]))


data1 = open("./Day 15/data1", "r").read()
data2 = open("./Day 15/data2", "r").read()

main(data1)
main(data2)