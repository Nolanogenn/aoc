from tqdm import tqdm
data = open('in').readlines()
data = [x.strip() for x in data]
data_l = [[x for x in y] for y in data]

obstacles = [(i,j) for i in range(len(data)) for j, x in enumerate(data[i])  if x == "#"]
startingPos = [(i,j) for i in range(len(data)) for j, x in enumerate(data[i])  if x == "^"][0]
d = (-1,0)
nextDirs = {
        (-1,0):(0,+1),
        (0,+1):(+1,0),
        (+1,0):(0,-1),
        (0,-1):(-1,0)
        }

ans_1= 0
ans_2= 0

def inbound(pos, m):
    if pos[0] < 0 or pos[0] >= len(m):
        return False
    if pos[1] < 0  or pos[1] >=len(m[0]):
        return False
    return True

pos = tuple(startingPos)
while inbound(pos, data):
    data_l[pos[0]][pos[1]] = '$'
    newPos = (pos[0]+d[0], pos[1]+d[1])
    if newPos not in obstacles:
        pos = newPos
    else:
        d = nextDirs[d]
ans_1 += sum([1 for x in data_l for y in x if y == '$'])
print(f"SOLUTION FOR PART1: {ans_1}")

visited = [(i,j) for i in range(len(data_l)) for j, x in enumerate(data_l[i]) if x == '$' and (i,j) != startingPos]
predicted_obstacles = [obstacles+[v] for v in visited]

for obstacles in tqdm(predicted_obstacles):
    pos = tuple(startingPos)
    d = (-1,0)
    seen = set((pos, d))
    while inbound(pos, data):
        seen.add((pos,d))
        newPos = (pos[0]+d[0], pos[1]+d[1])
        if newPos not in obstacles:
            if (newPos, d) in seen:
                ans_2 +=1 
                break
            pos = newPos
        else:
            d = nextDirs[d]

print(f"SOLUTION FOR PART2: {ans_2}")
