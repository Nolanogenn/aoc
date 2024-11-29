data = open('in').read()

ans_1= 0
ans_2= 0

stacks,movs = data.split('\n\n')
movs = movs.split('\n')[:-1]
stacks = stacks.split('\n')
num_stacks = int(stacks[-1].split()[-1])

l = {n : [] for n in range(1,num_stacks+1)}
for stack in stacks[:-1]:
    elems = [stack[1+(4*n):2+(4*n)] for n in range(num_stacks)] 
    for i in range(1,num_stacks+1):
        if elems[i-1] != ' ':
            l[i].append(elems[i-1])
l = {n: l[n][::-1] for n in l}

for mov in movs:
    tomove, start, end = [int(x) for x in mov.split() if x.isnumeric()]
    m = l[start][-tomove:]
    for k in  m[::-1]:
        l[end].append(k)
    l[start] = l[start][:-tomove]
ans_1 = ''.join([l[k][-1] for k in l])

l = {n : [] for n in range(1,num_stacks+1)}
for stack in stacks[:-1]:
    elems = [stack[1+(4*n):2+(4*n)] for n in range(num_stacks)] 
    for i in range(1,num_stacks+1):
        if elems[i-1] != ' ':
            l[i].append(elems[i-1])
l = {n: l[n][::-1] for n in l}
for mov in movs:
    tomove, start, end = [int(x) for x in mov.split() if x.isnumeric()]
    m = l[start][-tomove:]
    for k in m:
        l[end].append(k)
    l[start] = l[start][:-tomove]
ans_2 = ''.join([l[k][-1] for k in l])
    
print(f"SOLUTION FOR PART1: {ans_1}")
print(f"SOLUTION FOR PART2: {ans_2}")
