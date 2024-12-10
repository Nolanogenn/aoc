import sys

sys.setrecursionlimit(100000)

data = open('in').readlines()
data = [x.strip() for x in data]

starts = [((i,j),0) for i, line in enumerate(data) for j, v in enumerate(line) if v == '0']
movs = {"U":(-1,0),"D":(1,0),"L":(0,-1),"R":(0,1)}
movs_name = ["U", "D", "L", "R"]

def dfs(pos):
    seen = set()
    query = [pos]
    while query:
        p = query.pop(0)
        if p[1] == 9:
            seen.add(p[0])
        else:
            s = p[0]
            v = p[1]
            ms = [s[0]>0,s[0]<len(data)-1,s[1]>0,s[1]<len(data[0])-1]
            movements = [movs[x] for i, x in enumerate(movs_name) if ms[i]]
            to_add = [((s[0]+m[0],s[1]+m[1]),v+1) for m in movements if int(data[s[0]+m[0]][s[1]+m[1]]) == v+1]
            query.extend(to_add)
    return seen

ans_1= 0
ans_2= 0

for start in starts:
    ans_1 += len(dfs(start))

def dfs_2(pos,total):
    if pos == []:
        return total
    p = pos.pop()
    if p[1] == 9:
        total += 1
        return dfs_2(pos, total)
    s = p[0]
    v = p[1]
    ms = [s[0]>0,s[0]<len(data)-1,s[1]>0,s[1]<len(data[0])-1]
    movements = [movs[x] for i, x in enumerate(movs_name) if ms[i]]
    to_add = [((s[0]+m[0],s[1]+m[1]),v+1) for m in movements if int(data[s[0]+m[0]][s[1]+m[1]]) == v+1]
    pos.extend(to_add)
    return dfs_2(pos,total)

ans_2 = dfs_2(starts,0)

print(f"SOLUTION FOR PART1: {ans_1}")
print(f"SOLUTION FOR PART2: {ans_2}")
