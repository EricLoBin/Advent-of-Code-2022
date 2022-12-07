from inputs.input import get_input

class file:
    def __init__(self, name, size = None, prev = None, ftype = None):
        self.name = name
        self.size = size
        self.prev = prev
        self.type = ftype
        self.files = {}
        self.folders = {}

    @classmethod
    def new_folder(cls, name, prev = None):
        element = cls(name, prev = prev, ftype = "folder")
        prev.folders[name] = element
        return element

    @classmethod
    def new_file(cls, string, prev = None):
        size, name = string.split(" ")
        element = cls(name, int(size), prev = prev, ftype = "file")
        prev.files[name] = element
        return element

    def total_size(self):
        if self.size == None:
            self.size = sum([file.total_size() for file in self.files.values()]) + sum([folder.total_size() for folder in self.folders.values()])
        return self.size

inp = get_input(7).read().splitlines()

root = file('/')

current = root
for line in inp:
    if line[0] == '$': # command
        if line[2] == 'c': # cd
            name = line.split(" ")[2]
            match name:
                case '/':
                    current = root
                case '..':
                    current = current.prev
                case _:
                    if name not in current.folders:
                        file.new_folder(name, prev = current)
                    current = current.folders[name]
    else:
        arg1, arg2 = line.split(" ")
        if arg1 == "dir":
            if arg2 not in current.folders:
                file.new_folder(arg2, prev = current)
        else:
            if arg2 not in current.files:
                file.new_file(line, prev = current)

s = 0

def check_sizes(folder: file):
    global s
    for dir in folder.folders.values():
        t = dir.total_size()
        if t <= 100000:
            s += t
        check_sizes(dir)

check_sizes(root)

print(s)
