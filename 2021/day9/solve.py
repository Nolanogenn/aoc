data = open('in').readlines()
data = [x.strip() for x in data]
max_h = len(data)
max_w = len(data[0].strip())

def expandBasin(tocheck):
    basin = set()
    checking = tocheck.pop()
    seen = set()
    while tocheck:
        #print(checking, seen, tocheck, [data[x[0]][x[1]] for x in tocheck], basin)
        seen.add(checking)
        if data[checking[0]][checking[1]] != '9':
            basin.add(checking)
            toapp = set()
            if checking[0] < max_h-1:
                toapp.add((checking[0]+1, checking[1]))
            if checking[0] > 0:
                toapp.add((checking[0]-1, checking[1]))
            if checking[1] < max_w - 1:
                toapp.add((checking[0], checking[1]+1))
            if checking[1] > 0:
                toapp.add((checking[0], checking[1]-1))
            toapp = [x for x in toapp if x not in seen]
            tocheck.extend(toapp)
        checking = tocheck.pop()
    return len(basin)



ans_1 = 0
ans_2 = 1
basins = []
for i, line in enumerate(data):
    for j, h in enumerate(line):
        tocheck = []
        if i < max_h-1:
            tocheck.append((i+1,j))
        if i > 0:
            tocheck.append((i-1,j))
        if j < max_w - 1:
            tocheck.append((i,j+1))
        if j > 0:
            tocheck.append((i,j-1))
        if all([h<data[x[0]][x[1]] for x in tocheck]):
            ans_1 += int(h)+1
            print(f"LOOKING AT ({i}, {j}) WITH CHECKING: {tocheck}")
            size =  expandBasin(tocheck)
            basins.append(size)

threeLargestBasins = sorted(basins)[-3:]
for b in threeLargestBasins:
    ans_2 *= b
print(f"SOLUTION FOR PART1: {ans_1}")
print(f"SOLUTION FOR PART2: {ans_2}")
        
