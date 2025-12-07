data = [x.strip() for x in open('in').readlines()]

rays = [(0,i) for i, x in enumerate(data[0]) if x == 'S']
seen = set([rays[0]])
splitters = [[(i,j) for j,x in enumerate(row) if x == '^'] for i,row in enumerate(data)]
hits = set([])

ans_1= 0
ans_2= 0
reach = []
while rays:
    curr = rays.pop()
    for splitter in splitters[curr[0]+1:]:
        hit = [x for x in splitter if x[1] == curr[1]]
        if hit:
            ans_1 += 1
            hits.add(hit[0])
            l = (splitter[0][0],curr[1]-1)
            r = (splitter[0][0],curr[1]+1)
            if r not in seen:
                seen.add(r)
                rays.append(r)
            if l not in seen:
                seen.add(l)
                rays.append(l)
            break
ans_1 = len(hits)

splitters = [x for x in splitters if x]
starting = [(0,i) for i, x in enumerate(data[0]) if x == 'S'][0]
rays = {starting : 1}
toCheck = set([starting])

for splitter in splitters:
    toRem = []
    toAdd = set()
    for elem in toCheck:
        hits = [x for x in splitter if x[1] == elem[1]]
        if hits:
            toRem.append(elem)
        for h in hits:
            l = (h[0], elem[1]-1)
            r = (h[0], elem[1]+1)
            if l not in rays:
                rays[l] = 0
            rays[l] += rays[(elem[0], elem[1])]
            if r not in rays:
                rays[r] = 0
            rays[r] += rays[(elem[0], elem[1])]
            toAdd.add(r)
            toAdd.add(l)
    toCheck = set([x for x in toCheck if x not in toRem])
    for a in toAdd:
        toCheck.add(a)

ans_2 = sum([rays[x] for x in rays if x in toCheck])
print(f"SOLUTION FOR PART1: {ans_1}")
print(f"SOLUTION FOR PART2: {ans_2}")
