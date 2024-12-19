data = open('in').read()
towels, design = data.split('\n\n')

towels = towels.strip().split(', ')
design = design.strip().split('\n')

ans_2 = 0
m_p_len = max(map(len, towels))
memos = {}
def arrangs(d):
    if d in memos:
        return memos[d]
    if len(d) == 0:
        memos[d] = 1
        return 1
    v = d in towels
    for i in range(1, min(m_p_len+1, len(d))):
        if d[:i] not in towels:
            continue
        v += arrangs(d[i:])
    memos[d] = v
    return v

arr = map(arrangs, design)
ans_1 = len([x for x in arr if x>0])
ans_2 = sum(map(arrangs, design))

print(f"SOLUTION FOR PART1: {ans_1}")
print(f"SOLUTION FOR PART2: {ans_2}")
