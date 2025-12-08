import itertools
import math

def dist(x,y):
    n0 = abs(x[0]-y[0])**2
    n1 = abs(x[1]-y[1])**2
    n2 = abs(x[2]-y[2])**2
    return n0+n1+n2

def findParent(p, sets):
    if sets[p] == p:
        return p
    return findParent(sets[p], sets)

def join(p1,p2,parents):
    p1 = findParent(p1,parents)
    p2 = findParent(p2,parents)
    if p1 != p2:
        parents[p2] = p1
        return True

data = [x.strip().split(',') for x in open('in').readlines()]
points = [tuple(int(j) for j in i) for i in data]
parents = {p:p for p in points}
p_comb = itertools.combinations(points,2)
dists = [(x[0],x[1],dist(x[0],x[1])) for x in p_comb]
dists = sorted(dists, key= lambda x: x[2])

for c in range(1000):
    p1, p2,_ = dists[c]
    join(p1, p2, parents)

groups = [findParent(x,parents) for x in parents]
groupsUnique = set(groups)
ls = sorted([groups.count(x) for x in groupsUnique], reverse=True)
ans_1 = 1
for l in ls[:3]:
    ans_1 = ans_1 * l
print(f"SOLUTION FOR PART1: {ans_1}")

c = -1
parents = {p:p for p in points}
l = len(parents.keys())
while l > 1:
    c += 1
    p1,p2, _ = dists[c]
    x = join(p1, p2, parents)
    if x:
        l = l-1

ans_2 = dists[c][0][0] * dists[c][1][0]

print(f"SOLUTION FOR PART2: {ans_2}")
