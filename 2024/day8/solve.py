from itertools import combinations

ans_1= 0

data = open('in').readlines()
data = [x.strip() for x in data]


busy = []
antennas = {}

def inbound(point, data):
    if (0 <= point[0] < len(data)) and (0 <= point[1] < len(data[0])):
        return True
    return False

for i, x in enumerate(data):
    for j, y in enumerate(x):
        if y != '.':
            if y not in antennas:
                antennas[y] = []
            antennas[y].append((i,j))


busy = set()
for k in antennas:
    combs = combinations(antennas[k],2)
    for comb in combs:
        dist_x = comb[1][0]-comb[0][0]
        dist_y = comb[1][1]-comb[0][1]
        antinode_1 = (comb[0][0]+2*dist_x, comb[0][1]+2*dist_y)
        antinode_2 = (comb[1][0]-2*dist_x, comb[1][1]-2*dist_y)
        if inbound(antinode_1, data):
            busy.add(antinode_1)
        if inbound(antinode_2,data):
            busy.add(antinode_2)
ans_1 = len(busy)

busy = set()
for k in antennas:
    combs = combinations(antennas[k],2)
    for comb in combs:
        print(comb)
        dist_x = comb[1][0]-comb[0][0]
        dist_y = comb[1][1]-comb[0][1]
        antinode_1 = (comb[0][0]+dist_x, comb[0][1]+dist_y)
        while inbound(antinode_1, data):
            busy.add(antinode_1)
            antinode_1 = (antinode_1[0]+dist_x, antinode_1[1]+dist_y)
        antinode_2 = (comb[1][0]-dist_x, comb[1][1]-dist_y)
        while inbound(antinode_2,data):
            busy.add(antinode_2)
            antinode_2 = (antinode_2[0]-dist_x, antinode_2[1]-dist_y)

ans_2 = len(busy)

print(f"SOLUTION FOR PART1: {ans_1}")
print(f"SOLUTION FOR PART2: {ans_2}")
