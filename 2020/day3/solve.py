data = open('in').readlines()
data = [x.strip() for x in data]

ans_1= 0
ans_2= 1

col=3
memos = {}

def getcol(l, i):
    if (''.join(l), i) in memos:
        return memos[(''.join(l), i)]
    if i < len(l):
        memos[(''.join(l),i)] = l[i]
        return l[i]
    memos[(''.join(l),i)] = getcol(l, i-len(l))
    return getcol(l, i-len(l))

for i, line in enumerate(data[1:]):
    c = col*(i+1)
    ch = getcol(line,c)
    if ch == '#':
        ans_1 += 1



movs = [(1,1),(3,1),(5,1),(7,1),(1,2)]
for mov in movs:
    trees=0
    col = mov[0]
    lines = data[mov[1]::mov[1]]
    for i, line in enumerate(lines):
        c = col*(i+1)
        ch = getcol(line,c)
        if ch == '#':
            trees+=1
    ans_2 *= trees

print(f"SOLUTION FOR PART1: {ans_1}")
print(f"SOLUTION FOR PART2: {ans_2}")
