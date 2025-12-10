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

data = [parseLine(x.strip().split()) for x in open('in').readlines()]
ans_1= 0
for x in tqdm(data):
    visited = {}
    target = x[0]
    starting = tuple([0 for _ in target])
    buttons = x[1]
    query = [(apply(starting,b),b,1) for b in buttons]
    while query:
        curr, lastB, steps = query.pop()
        goNext = False
        if curr not in visited:
            visited[curr] = steps
            goNext = True
        elif steps < visited[curr]:
            visited[curr] = steps
            if curr != target:
                goNext = True
        if goNext:
            ns = [
                    (apply(curr, b), b,steps+1) for b in buttons if b != lastB
                    ]
            query.extend(ns)
    ans_1 += visited[target]



ans_2= 0


print(f"SOLUTION FOR PART1: {ans_1}")
print(f"SOLUTION FOR PART2: {ans_2}")
