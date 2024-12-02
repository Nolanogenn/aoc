from pprint import pprint
data = open('in').readlines()
data = [x.strip() for x in data]

ans_1= 0
ans_2= 0

dirs = {}
workingDir = ""

for line in data:
    if line.startswith("$ cd") and not line.endswith(".."):
        workingDir = line.split()[2]
        dirs[workingDir] = []
    elif not line.startswith("$"):
        if line.startswith("dir"):
            dirs[workingDir].append(line.split()[1])
        else:
            dirs[workingDir].append(int(line.split()[0]))
def findSize(k,d):
    if type(k) == int:
        return k
    return sum([findSize(v,d) for v in d[k]])


dirSize = {}
for d in dirs:
    dirSize[d] = sum([findSize(v, dirs) for v in dirs[d]])

pprint(dirs)
ans_1 = sum([x for x in dirSize.values() if x <= 100_000])

print(f"SOLUTION FOR PART1: {ans_1}")
print(f"SOLUTION FOR PART2: {ans_2}")
