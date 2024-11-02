data = open('test').readlines()
data = [x.strip() for x in data]

weights = {
        (x,y):int(data[x][y])
        for x in range(len(data))
        for y in range(len(data[0]))
        }
costs={
        p : 999999999999999
        for p in weights
        }
costs[(0,0)] = 0
end = (len(data)-1, len(data[0])-1)
n = [(0,0)]
while n:
    pos = n[0]
    current_w = costs[pos]
    possibleNext = []
    if pos[0] > 0:
        possibleNext.append((pos[0]-1, pos[1]))
    if pos[0] < len(data[0])-1:
        possibleNext.append((pos[0]+1, pos[1]))
    if pos[1] > 0:
        possibleNext.append((pos[0], pos[1]-1))
    if pos[1] < len(data)-1:
        possibleNext.append((pos[0], pos[1]+1))
    for nx in possibleNext:
        w = weights[nx]
        n_w = current_w + w
        if n_w < costs[nx]:
            costs[nx] = n_w #update
            n.append(nx)
    n = n[1:]

ans_1= costs[end]

h = len(data)
w = len(data[0])
def expandGraph(g, times):
    toadd=[]
    for k in g:
        for t in range(times):
            newpos1 =(
                    k[0]+(h*(t+1)),
                    k[1]
                    )
            newpos2 =(
                    k[0],
                    k[1]+(w*(t+1))
                    )
            newpos3 = (
                    k[0]+(h*(t+1)),
                    k[1]+(w*(t+1))
                    )
            if g[k] < 9:
                newVal = g[k] + 1
            if g[k] == 9:
                newVal = 1
            if g[k] < 8:
                newVal2 = g[k] + 2
            if g[k] == 8:
                newVal2 = 1
            toadd.append((newpos1,newVal))
            toadd.append((newpos2,newVal))
            toadd.append((newpos3,newVal2))
    for a in toadd:
        g[a[0]] = a[1]
                
expandGraph(weights,4)
ans_2= 0 
costs={
        p : 99999999999999
        for p in weights
        }
costs[(0,0)] = 0
h = max([x[0] for x in costs])
w = max([x[1] for x in costs])
end = (h, w)
n = [(0,0)]
print(weights)
while n:
    pos = n[0]
    current_w = costs[pos]
    possibleNext = []
    if pos[0] > 0:
        possibleNext.append((pos[0]-1, pos[1]))
    if pos[0] < h:
        possibleNext.append((pos[0]+1, pos[1]))
    if pos[1] > 0:
        possibleNext.append((pos[0], pos[1]-1))
    if pos[1] < w:
        possibleNext.append((pos[0], pos[1]+1))
    for nx in possibleNext:
        w = weights[nx]
        n_w = current_w + w
        if n_w < costs[nx]:
            costs[nx] = n_w #update
            n.append(nx)
    n = n[1:]

ans_2= costs[end]


print(f"SOLUTION FOR PART1: {ans_1}")
print(f"SOLUTION FOR PART2: {ans_2}")
