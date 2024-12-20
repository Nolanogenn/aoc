from tqdm import tqdm
from itertools import combinations

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


def check_pos(pos, cost, walls, boundaries, costs):
    if pos in walls:
        return False
    if not 0 <= pos[0] < boundaries[0]:
        return False
    if not 0 <= pos[1] < boundaries[1]:
        return False
    if costs.get(pos,[9999])[0] > cost:
        return True
    return False

check = [(start,0,[])]

while check:
    pos, cost, currentPath = check.pop()
    costs[pos] = (cost, currentPath)
    if pos != end:
        newCost = cost + 1
        n = [
                (pos[0]-1, pos[1]),
                (pos[0]+1, pos[1]),
                (pos[0], pos[1]+1),
                (pos[0], pos[1]-1)
            ]
        check.extend([(x,newCost,currentPath+[x]) for x in n if check_pos(x,newCost,walls,boundaries, costs)])

best_cost, best_path = costs[end]
best_path = [start] + best_path

ans_1 = 0
cheats = {}
for step in best_path:
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    ns = [(step[0]+d[0],step[1]+d[1],step[0]+d[0]*2,step[1]+d[1]*2) for d in dirs]
    ns = [(n[2],n[3]) for n in ns if (n[0],n[1]) in walls and (n[2],n[3]) in best_path]
    for n in ns:
        saved = best_path.index(n)-(best_path.index(step)+2)
        if saved > 0:
            if saved >= 100:
                ans_1 += 1
            if saved not in cheats:
                cheats[saved] = 0
            cheats[saved] += 1

def manh_dist(p1,p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

ans_2= 0
cheats = {}
for comb in tqdm(combinations(best_path,2)):
    dist = manh_dist(comb[0], comb[1])
    if dist <= 20:
        saved = best_path.index(comb[1])-(best_path.index(comb[0])+dist)
        if saved >= 100:
            if saved not in cheats:
                cheats[saved] = 0
            cheats[saved] += 1
            ans_2 += 1
print(f"SOLUTION FOR PART1: {ans_1}")
print(f"SOLUTION FOR PART2: {ans_2}")
