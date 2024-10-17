from pprint import pprint
import re

data = open('input.txt').readlines()
data = [d.replace('\n', '') for d in data]
threshold = 100000

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

pprint(dirs)
def getsize(d, dirs):
    size = 0
    for elem in d:
        if type(elem) == int:
            size += elem
        else:
            toadd = getsize(dirs[elem], dirs)
            size += toadd
    return size

totals = []
for d in dirs:
    size = getsize(dirs[d], dirs)
    if size <= threshold:
        print(d, size)
        totals.append(size)

print(sum(totals))
