import itertools
from tqdm import tqdm 

data = open('in').readlines()
data = [x.strip().split('-') for x in data]
edges = set(map(frozenset, data))

def is_clique(nodes,edges) -> bool:
    pairs = itertools.combinations(nodes,2)
    return all(frozenset(p) in edges for p in pairs)
def find_maximum_clique(nodes,edges):
    for clique_size in range(len(nodes),2,-1):
        possible = itertools.combinations(nodes,clique_size)
        for clique in possible:
            if is_clique(clique,edges):
                return clique
    return None

conns = {}
for a,b in data:
    if a not in conns:
        conns[a] = []
    if b not in conns:
        conns[b] = []
    conns[a].append(b)
    conns[b].append(a)


ans_1= 0
ans_2= 0

three_way = []

#for start,_ in tqdm(data):
#    seen = set()
#    n = conns[start]
#    good = start.startswith('t')
#    tocheck = [([start],j,good) for j in n]
#    while tocheck:
#        current = tocheck[0]
#        tocheck = tocheck[1:]
#        c = current[0]
#        m = current[1]
#        good = current[2]
#        if len(c) == 3:
#            if m == start and good:
#                three_way.append(','.join(sorted(c)))
#        else:
#            for co in conns[m]:
#                good = m.startswith('t')
#                tocheck.append((c+[m],co,good))
#ans_1 = len(set(three_way))

max_clique = ("", [])
for node in conns.keys():
    neighbors = conns[node]
    local_maximum = find_maximum_clique(neighbors, edges)
    if local_maximum and len(local_maximum) > len(max_clique[1]):
        max_clique = (node, local_maximum)
clique = [max_clique[0]] + list(max_clique[1])

ans_2 = ','.join(sorted(clique))

print(f"SOLUTION FOR PART1: {ans_1}")
print(f"SOLUTION FOR PART2: {ans_2}")
