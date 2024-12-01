data = open('in').readlines()
data = [x.strip() for x in data]

first = sorted([int(x.split()[0]) for x in data])
second = sorted([int(x.split()[1]) for x in data])

pairs = zip(first,second)

ans_1= 0
ans_2= 0

for pair in pairs:
    ans_1 += abs(pair[0]-pair[1])

sims = {x:(first.count(x), second.count(x)) for x in first}
for sim in sims:
    ans_2 += sim * sims[sim][0] * sims[sim][1]

print(f"SOLUTION FOR PART1: {ans_1}")
print(f"SOLUTION FOR PART2: {ans_2}")
