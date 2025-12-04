data = [x.strip() for x in open('in').readlines()]

def getNeighbor(x,y,M):
    check = [(x-1,y),(x,y-1),(x-1,y-1),
             (x+1,y),(x,y+1),(x+1,y+1),
             (x-1,y+1),(x+1,y-1)]
    check = [str(x) for x in check if all([j > -1 for j in x]) and all([j<M for j in x])]
    return check

def findReachable(m):
    reachable = []
    for k in m:
        N = m[k]
        occupied = [j in m for j in N]
        if sum(occupied) < 4:
            reachable.append(k)
    return reachable

ans_1= 0
ans_2= 0

m = {}
M = len(data)
for i, line in enumerate(data):
    for j, elem in enumerate(line):
        if data[i][j] == "@":
            m[str((i,j))] = getNeighbor(i,j,M)

reachable = findReachable(m)
ans_1 = len(reachable)

while reachable:
    ans_2 += len(reachable)
    for r in reachable:
        m.pop(r)
    reachable = findReachable(m)
print(f"SOLUTION FOR PART1: {ans_1}")
print(f"SOLUTION FOR PART2: {ans_2}")
