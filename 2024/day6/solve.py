from tqdm import tqdm
data = open('in').readlines()
data = [x.strip() for x in data]
data_l = [[x for x in y] for y in data]

obstacles = [(i,j) for i in range(len(data)) for j, x in enumerate(data[i])  if x == "#"]
startingPos = [(i,j) for i in range(len(data)) for j, x in enumerate(data[i])  if x == "^"][0]
h = len(data)
w = len(data[0])
d = (-1,0)
nextDirs = {
        (-1,0):(0,+1),
        (0,+1):(+1,0),
        (+1,0):(0,-1),
        (0,-1):(-1,0)
        }

ans_1= 0
ans_2= 0

memo = {}
def inbound(pos):
    if pos in memo:
        return memo[pos]
    if (0 < pos[0] < h) and (0 < pos[1] < w):
        memo[pos] = True
        return True
    memo[pos] = False
    return False

pos = tuple(startingPos)
while inbound(pos):
    data_l[pos[0]][pos[1]] = '$'
    newPos = (pos[0]+d[0], pos[1]+d[1])
    if newPos in obstacles:
        d = nextDirs[d]
    else:
        pos = newPos
ans_1 += sum([1 for x in data_l for y in x if y == '$'])
print(f"SOLUTION FOR PART1: {ans_1}")

visited = [(i,j) for i in range(len(data_l)) for j, x in enumerate(data_l[i]) if x == '$' and (i,j) != startingPos]
for p in tqdm(visited):
    cycle = False
    pos = startingPos
    seen = set()
    d = (-1,0)
    obst = obstacles +[p]
    while inbound(pos) and not cycle:
        state = (pos,d)
        if state in seen:
            cycle = True
            break
        seen.add(state)
        step = (pos[0]+d[0], pos[1]+d[1])
        if step in obst:
            d = nextDirs[d]
        else:
            pos = step
    ans_2 += cycle

print(f"SOLUTION FOR PART2: {ans_2}")
