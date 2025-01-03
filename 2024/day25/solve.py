data = open('in').read()
data = [x.strip().split('\n') for x in data.split('\n\n')]

max_h = len(data[0])-1

ans_1= 0

keys = []
locks = []
for schematics in data:
    heights = []
    t = 'lock'
    if schematics[0][0] == '.':
        t = 'key'
    for c in range(len(schematics[0])):
        col = [s[c] for s in schematics]
        heights.append(len([x for x in col if x =='#'])-1)
    if t == 'key':
        keys.append(heights)
    else:
        locks.append(heights)

for lock in locks:
    for key in keys:
        comb = zip(lock,key)
        sums = [sum(c) for c in comb]
        if not any([x>=max_h for x in sums]):
            ans_1 +=1
            print(lock,key)

print(f"SOLUTION FOR PART1: {ans_1}")
