import itertools

def getArea(x,y):
    h = abs(x[0] - y[0])+1
    w = abs(x[1] - y[1])+1
    return h*w

def crosses(pair, line):
    wL = min((line[0][1], line[1][1]))
    WL = max((line[0][1], line[1][1]))
    hL = min((line[0][0], line[1][0]))
    HL = max((line[0][0], line[1][0]))
    h = min((pair[0][0], pair[1][0]))
    H = max((pair[0][0], pair[1][0]))
    w = min((pair[0][1], pair[1][1]))
    W = max((pair[0][1], pair[1][1]))
    if line[0][0] == line[1][0]:
        if h < line[0][0] < H and (WL > w or wL < w):
            return True
        return False
    if w < line[0][1] < W and (HL > h or wL < H):
        return True
    return False




data = [x.strip().split(',') for x in open('test').readlines()]
tiles = [(int(x[0]), int(x[1])) for x in data]
tilesPairs = itertools.combinations(tiles,2)

areas = [getArea(x[0], x[1]) for x in tilesPairs]
areas = sorted(areas)
ans_1 = areas.pop()

ans_2= 0
tilesPairs = list(itertools.combinations(tiles,2))
lines = [
        x for x in tilesPairs
        if (x[0][0] == x[1][0] or x[0][1] == x[1][1])
        ]

for pair in tilesPairs:
    valid = True
    for l in lines:
        if crosses(pair, l):
            print(pair,l)
            valid = False
    if valid:
        print(pair, getArea(pair[0], pair[1]))


print(f"SOLUTION FOR PART1: {ans_1}")
print(f"SOLUTION FOR PART2: {ans_2}")
