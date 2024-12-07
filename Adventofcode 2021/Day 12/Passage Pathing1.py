import sys
sys.path.insert(0, '.')
from tools import log

class Path():
    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name

    def __init__(self, name):
        self.name = name
        self.routes = []

    def contains(self, path):
        return path in self.routes

    def add_route(self, route):
        self.routes.append(route)



class Paths():
    paths = {} # -> {"GC", path class}

    @classmethod
    def create(self, path):
        """Returns True if newly created and False if already exists"""
        if path not in self.paths.keys():
            route = Path(path)
            self.paths[route.name] = route
            return route
        return False

    @classmethod
    def get_path(self, path_str):
        if (path := self.create(path_str)) == False:
            path = self.paths[path_str]
        return path
        
    @classmethod
    def add_path_route(self, path_str, route_str):
        path = self.get_path(path_str)
        route = self.get_path(route_str)
            
        if not route.contains(path):
            route.add_route(path)

        if not path.contains(route):
            path.add_route(route)


def parse_data(data):
    parsed = []
    for route in data.split("\n"):
        parsed.append(route.split("-"))
    return parsed


def get_paths(path, base):
    ret = []
    if path == "end":
        return [[Paths.paths["end"]]]

    filtered = list(filter(lambda x: (x.name != x.name.lower()) or x.name not in base, Paths.paths[path].routes))

    new_base = list(base)
    new_base.append(path)

    for route in filtered:
        for p in get_paths(route.name, new_base):
            l = [Paths.paths[path]]
            l.extend(p)
            ret.append(l)

    return ret # []

@log
def main(data):
    Paths.paths = {}
    data = parse_data(data)
    
    for x in data:
        Paths.add_path_route(*x)

    erg = []

    for y in get_paths("start", []):
        erg.append(list(map(lambda x: x.name, y)))

    return len(erg)


data1 = open("./Day 12/data1", "r").read()
data2 = open("./Day 12/data2", "r").read()

main(data1)
main(data2)