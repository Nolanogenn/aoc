from pprint import pprint
import re

data = open('input.txt').readlines()
data = [d.replace('\n', '') for d in data]
needed_space = 30000000
disk_space = 70000000

dirs = {}

path = []
for line in data:
    match line.split():
        case ["$", "cd", '..']:
            path.pop()
        case ["$", "cd", directory]:
            path.append(directory) 
            currentDir = '/'.join(path)
            dirs[currentDir] = [0]
        case ["dir", directory]:
            tmppath = path + [directory]
            dirs[currentDir].append('/'.join(tmppath))
        case [size, _] if size.isnumeric():
            dirs[currentDir][0] += int(size)

def getsize(d, dirs):
    size = 0
    for elem in d:
        if type(elem) == int:
            size += elem
        else:
            toadd = getsize(dirs[elem], dirs)
            size += toadd
    return size

usedspace = getsize('/', dirs)
freespace = disk_space - usedspace
tofree = needed_space - freespace

canBeDeleted = 100000000000000
for d in dirs:
    s = getsize(dirs[d], dirs)
    if s >= tofree and s <= canBeDeleted:
        canBeDeleted = s
print(canBeDeleted)
