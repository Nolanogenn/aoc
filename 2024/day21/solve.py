import math
data = open('in').readlines()
codes = [x.strip() for x in data]

keys = {
        'A' : (0,2),
        '^' : (0,1),
        '<' : (1,0),
        '>' : (1,2),
        'v' : (1,1),
        }
nums = {
        'A' : (3,2),
        '0' : (3,1),
        '1' : (2,0),
        '2' : (2,1),
        '3' : (2,2),
        '4' : (1,0),
        '5' : (1,1),
        '6' : (1,2),
        '7' : (0,0), 
        '8' : (0,1),
        '9' : (0,2),
        }
def boundaries(x):
    if not 0 <= x[0] <= 3:
        return False
    if not 0 <= x[1] < 3:
        return False
    if x == (3,0):
        return False
    return True
paths = {}
for num1 in nums:
    paths[num1] = {}
    for num2 in nums:
        paths[num1][num2] = []
        tocheck = [(nums[num1],'')]
        seen = set()
        while tocheck:
            current = tocheck[0]
            tocheck = tocheck[1:]
            p = current[0]
            c = current[1]
            if p == nums[num2]:
                paths[num1][num2].append(c)
            else:
                seen.add(p)
                m = ['^', 'v', '<', '>']
                n = [(p[0]-1,p[1]),(p[0]+1,p[1]),(p[0],p[1]-1),(p[0],p[1]+1)]
                toadd = [(n[i],c+m[i]) for i,x in enumerate(n) if boundaries(x) and x not in seen]
                tocheck.extend(toadd)
paths_min = {}
for n in paths:
    paths_min[n] = {}
    for n2 in paths[n]:
        m = min([len(x) for x in paths[n][n2]])
        paths_min[n][n2] = [x for x in paths[n][n2] if len(x) == m]

def boundaries(x):
    if not 0 <= x[0] <= 1:
        return False
    if not 0 <= x[1] < 3:
        return False
    if x == (0,0):
        return False
    return True
paths = {}
for num1 in keys:
    paths[num1] = {}
    for num2 in keys:
        paths[num1][num2] = []
        tocheck = [(keys[num1],'')]
        seen = set()
        while tocheck:
            current = tocheck[0]
            tocheck = tocheck[1:]
            p = current[0]
            c = current[1]
            if p == keys[num2]:
                paths[num1][num2].append(c)
            else:
                seen.add(p)
                m = ['^', 'v', '<', '>']
                n = [(p[0]-1,p[1]),(p[0]+1,p[1]),(p[0],p[1]-1),(p[0],p[1]+1)]
                toadd = [(n[i],c+m[i]) for i,x in enumerate(n) if boundaries(x) and x not in seen]
                tocheck.extend(toadd)
paths_keys = {}
for n in paths:
    paths_keys[n] = {}
    for n2 in paths[n]:
        m = min([len(x) for x in paths[n][n2]])
        paths_keys[n][n2] = [x for x in paths[n][n2] if len(x) == m]

ans_1= 0
ans_2= 0


def buildSeq(k,i,prev,res,paths):
    if i == len(k):
        return res
    res = [x+path+'A' for x in res for path in paths[prev][k[i]]]
    return buildSeq(k,i+1,k[i],res, paths)

def shortestSeq(keys, depth, cache, paths):
    total = 0
    if depth == 0:
        return len(keys)
    if (keys, depth) in cache:
        return cache[(keys,depth)]
    subk =[x for x in  keys.replace('A', 'A_').split('_') if len(x) > 0]
    for k in subk:
        seqs = buildSeq(k,0,'A',[''],paths)
        m = math.inf
        for seq in seqs:
            v = shortestSeq(seq, depth-1, cache, paths)
            if v < m:
                m = v
        total += m
    cache[(keys,depth)] = total
    return total

memos = {}
for code in codes:
    seqs = buildSeq(code,0,'A',[''],paths_min)
    total = 0
    for seq in seqs:
        m = math.inf
        for seq in seqs:
            v = shortestSeq(seq,2,memos,paths_keys)
            if v < m:
                m = v
    total += m
    j = int(''.join([x for x in code if x.isnumeric()]))
    ans_1 += total * j
    total = 0
    for seq in seqs:
        m = math.inf
        for seq in seqs:
            v = shortestSeq(seq,25,memos,paths_keys)
            if v < m:
                m = v
    total += m
    j = int(''.join([x for x in code if x.isnumeric()]))
    ans_2 += total * j



print(f"SOLUTION FOR PART1: {ans_1}")
print(f"SOLUTION FOR PART2: {ans_2}")
