from tqdm import tqdm

def parseLine(line):
    target = tuple([0 if i == '.' else 1 for i in line[0][1:-1]])
    buttons = [tuple([int(x) for x in i[1:-1].split(',')]) for i in line[1:-1]]
    voltage = [int(x) for x in line[-1][1:-1].split(',')]
    return (target,buttons,voltage)

def apply(state, button):
    s2 = []
    for i, n in enumerate(state):
        if i not in button:
            s2.append(n)
        else:
            if n == 1:
                s2.append(0)
            else:
                s2.append(1)
    s2 = tuple(s2)
    return s2

data = [parseLine(x.strip().split()) for x in open('in').readlines()]
ans_1= 0
for x in tqdm(data):
    m = 99999999999999
    target = x[0]
    buttons = x[1]
    starting = tuple([0 for _ in x[0]])
    visited = set()
    query = [
            (apply(starting, button),1,str(i))
            for i, button in enumerate(buttons)
            ]
    while query:
        n,step,currButtons = query[0]
        query = query[1:]
        if step >= m:
            break
        visited.add(currButtons)
        if n == target:
            if step < m:
                m = step
        else:
            ns = [
                    (apply(n, button),step+1,currButtons+f";{str(i)}")
                    for i, button in enumerate(buttons)
                    if str(i) not in currButtons.split(';')
                    and currButtons+f";{str(i)}"  not in visited
                    ]
            query.extend(ns)
    ans_1 += m


ans_2= 0


print(f"SOLUTION FOR PART1: {ans_1}")
print(f"SOLUTION FOR PART2: {ans_2}")
