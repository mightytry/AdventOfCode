import sys
sys.path.insert(0, '.')
from tools import log

class File:
    def __init__(self,name,size):
        self.name = name
        self.size = size

class Folder:
    def __init__(self, name, parent = None):
        self.name = name
        self.parent = parent
        self.files = []
        self.size = 0

    def add_size(self, size):
        self.size += size
        if self.parent != None:
            self.parent.add_size(size)
            
    def add_file(self, file):
        if isinstance(file, Folder):
            file.parent = self
            self.files.append(file)
            self.add_size(file.size)
        else:
            self.files.append(file)
            self.add_size(file.size)
    
    def remove_file(self, file):
        if isinstance(file, Folder):
            self.files.remove(file)
            self.add_size(-file.size)
        else:
            self.files.remove(file)
            self.add_size(-file.size)
    
    @property
    def is_vaild(self):
        return self.size <= 100000         

class Command:
    def __init__(self,command,args):
        self.command = command
        self.args = args


class Pointer:
    def __init__(self, root_folder):
        self.folder = root_folder
        self.root_folder = root_folder

    def on_command(self,command):
        if command.command == "dir":
            for file in self.folder.files:
                if file.name == command.args:
                    return
            self.folder.add_file(Folder(command.args, self.folder))
            
        elif command.command == "cd":
            if command.args == "..":
                self.folder = self.folder.parent
            elif command.args == "/":
                self.folder = self.root_folder
            else:
                for file in self.folder.files:
                    if file.name == command.args:
                        self.folder = file
        elif command.command == "ls":
            #does nothing
            pass
        elif command.command == "touch":
            self.folder.add_file(File(command.args[1], command.args[0]))
        else:
            print("Command not found")
        return True

def parse_data(data):
    commands = []

    data = data.splitlines()
    for line in data:
        line = line.replace("$ ","")
        line = line.split(" ")
        try:
            line[0] = int(line[0])
            commands.append(Command("touch", line))
        except:
            if line[0] == "ls":
                commands.append(Command("ls", None))
            else: 
                commands.append(Command(*line))

    return commands

def check_folders(root, folder):
    valid = []
    
    for folder in folder.files:
        if isinstance(folder, Folder):
            if root.size - folder.size < 40000000:
                valid.append(folder)
            valid.extend(check_folders(root, folder))

    return valid
            
@log
def main(data):
    commands = parse_data(data)
    root_folder = Folder("/")

    pointer = Pointer(root_folder)

    for command in commands:
        pointer.on_command(command)

    return sorted(check_folders(root_folder, root_folder), key=lambda x: x.size)[0].size




if __name__ == "__main__":
    data1 = open("./Day 7/data1", "r").read()
    data2 = open("./Day 7/data2", "r").read()

    if data1 != "":
        main(data1)
    else:
        print("No data1 found")
    if data2 != "":
        main(data2)
    else:
        print("No data2 found")