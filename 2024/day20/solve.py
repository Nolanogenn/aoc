from tqdm import tqdm
from itertools import combinations, product

data = open('in').readlines()
data = [x.strip() for x in data]

start = (0,0)
end = (0,0)
costs = {}
walls = set()
path = set()
boundaries = (len(data), len(data[0]))

for i, line in enumerate(data):
    for j, value in enumerate(line):
        if value == '#':
            walls.add((i,j))
        else:
            path.add((i,j))
        if value == 'E':
            end = (i,j)
        if value == 'S':
            start = (i,j)

current = start
bestPath = {}
seen = set()
i = 0
while current != end:
    seen.add(current)
    bestPath[current] = i
    possibles = [(current[0]-1, current[1]),(current[0]+1,current[1]), (current[0],current[1]-1),(current[0],current[1]+1)]
    current = [x for x in possibles if x in path and x not in seen][0]
    i += 1
def manh_dist(p1,p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

ans_1 = 0
combs = combinations(bestPath,2)
for step in bestPath:
    dirs = [(step[0]-2,step[1]),(step[0]+2,step[1]),(step[0],step[1]-2),(step[0],step[1]+2)]
    ns = [n for n in dirs if n in bestPath]
    for n in ns:
        saved = bestPath[n] - bestPath[step]+2
        if saved >= 100:
            ans_1 += 1

ans_2= 0
cheats = {}
#combs = [(x,y,manh_dist(x,y)) for i,x in enumerate(best_path) for j,y in enumerate(best_path) if j-1 >= 100]
#    if  
#    dist = manh_dist(comb[0], comb[1])
#    if dist <= 20:
#        saved = best_path.index(comb[1])-(best_path.index(comb[0])+dist)
#        if saved >= 100:
#            if saved not in cheats:
#                cheats[saved] = 0
#            cheats[saved] += 1
#            ans_2 += 1
print(f"SOLUTION FOR PART1: {ans_1}")
print(f"SOLUTION FOR PART2: {ans_2}")
