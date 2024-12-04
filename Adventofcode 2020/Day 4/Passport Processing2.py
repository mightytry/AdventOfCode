import sys
sys.path.insert(0, '.')
from tools import log

class Passport():
    def __init__(self, data):
        self.data = data
        self.fields = {}
        for field in " ".join(data.split("\n")).split(" "):
            self.fields[field.split(":")[0]] = field.split(":")[1]

    def validate(self):
        #part 2
        # if "cid" not in self.fields and len(self.fields) == 7:
        #     return True

        erg = []

        if len(self.fields) == 8 or (len(self.fields) == 7 and "cid" not in self.fields):
            erg.append(1920 <= int(self.fields["byr"]) and int(self.fields["byr"]) <= 2002)
            erg.append(2010 <= int(self.fields["iyr"]) and int(self.fields["iyr"]) <= 2020)
            erg.append(2020 <= int(self.fields["eyr"]) and int(self.fields["eyr"]) <= 2030)
            if self.fields["hgt"][-2:] == "cm":
                erg.append(150 <= int(self.fields["hgt"][:-2]) and int(self.fields["hgt"][:-2]) <= 193)
            elif self.fields["hgt"][-2:] == "in":
                erg.append(59 <= int(self.fields["hgt"][:-2]) and int(self.fields["hgt"][:-2]) <= 76)
            else:
                erg.append(False)
            erg.append(self.fields["hcl"][0] == "#" and len(self.fields["hcl"]) == 7 and all([x in "0123456789abcdef" for x in self.fields["hcl"][1:]]))
            erg.append(self.fields["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])
            erg.append(len(self.fields["pid"]) == 9 and all([x in "0123456789" for x in self.fields["pid"]]))

        else:
            return False

        return all(erg)
        
        
            

        

def parse_data(data):
    data = data.split("\n\n")

    return [Passport(x) for x in data]

@log
def main(data):
    data = parse_data(data)

    return sum([x.validate() for x in data])


data1 = open("./Day 4/data1", "r").read()
data2 = open("./Day 4/data2", "r").read()

main(data1)
#main(data2)