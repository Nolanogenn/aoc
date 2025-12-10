import math
from z3 import Int, Optimize, sat
from tqdm import tqdm

def parseLine(line):
    target = tuple([0 if i == '.' else 1 for i in line[0][1:-1]])
    buttons = [tuple([int(x) for x in i[1:-1].split(',')]) for i in line[1:-1]]
    voltage = [int(x) for x in line[-1][1:-1].split(',')]
    return (target,buttons,voltage)

cache = {}
def apply(state, button):
    if (state,button) in cache:
        return cache[(state,button)]
    s2 = list(state)
    for i in button:
        if s2[i] == 1:
            s2[i] = 0
        else:
            s2[i] = 1
    s2 = tuple(s2)
    cache[(state,button)] = s2
    return s2

def buttonsToMatrix(buttons,target):
    m = [[0 for _ in range(len(buttons))] for i in range(len(target))]
    for i, b in enumerate(buttons):
        for elem in b:
            m[elem][i] = 1
    return m

data = [parseLine(x.strip().split()) for x in open('in').readlines()]
ans_1= 0
#for x in tqdm(data):
#    visited = {}
#    target = x[0]
#    starting = tuple([0 for _ in target])
#    buttons = x[1]
#    query = [(apply(starting,b),[b],1) for b in buttons]
#    while query:
#        curr, pressed, steps = query.pop()
#        goNext = False
#        if curr not in visited:
#            visited[curr] = steps
#            goNext = True
#        elif steps < visited[curr]:
#            visited[curr] = steps
#            if curr != target:
#                goNext = True
#        if goNext:
#            ns = [
#                    (apply(curr, b),b,steps+1)
#                    for b in buttons if b not in pressed
#                    ]
#            query.extend(ns)
#    ans_1 += visited[target]

ans_2= 0
for x in tqdm(data):
    n = len(x[2])
    m = len(x[1])
    M = buttonsToMatrix(x[1], x[2])
    v = [Int(f"x_{j}") for j in range(m)]
    opt = Optimize()
    for j in range(m):
        opt.add(v[j] >= 0)
    for i in range(n):
        opt.add(sum(M[i][j] * v[j] for j in range(m)) == x[2][i])
    opt.minimize(sum(v))
    if opt.check() != sat:
        print("no sol")
    mod = opt.model()
    sol = [mod[v[j]].as_long() for j in range(m)]
    ans_2 += sum(sol)


print(f"SOLUTION FOR PART1: {ans_1}")
print(f"SOLUTION FOR PART2: {ans_2}")
