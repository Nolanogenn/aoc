data = [x for x in open('in').readlines()]

problems = [x.split() for x in data[:-1]]
ops = data[-1].split()

def apply(op, l):
    l = [int(x) for x in l]
    if op == '+':
        return sum(l)
    else:
        b = 1
        for elem in l:
            b = b*elem
        return b

ans_1= 0
ans_2= 0

for p in range(len(problems[0])):
    i = [x[p] for x in problems]
    r = apply(ops[p], i)
    ans_1 += r

toMap = []
for l in data[:-1]:
    k = []
    j =[]
    for i,x in enumerate(l):
        if x.isdigit():
            j.append((i,x))
        elif j:
            k.append(j)
            j = []
    toMap.append(k)

for i in range(len(toMap[0])):
    current = [x[i] for x in toMap]
    current = sorted([j for x in current for j in x], key= lambda x: x[0])
    m = current[0][0]
    M = current[-1][0]
    current = [[x for x in current if x[0] ==j] for j in range(m,M+1)]
    current = [int(''.join([x[1] for x in j])) for j in current]
    op = ops[i]
    res = apply(op, current)
    ans_2 += res


print(f"SOLUTION FOR PART1: {ans_1}")
print(f"SOLUTION FOR PART2: {ans_2}")
