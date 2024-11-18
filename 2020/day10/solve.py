data = open('in').readlines()
data = [int(x.strip()) for x in data]

ans_1= 0
ans_2= 0

data = sorted(data)
data.insert(0,0)
data.append(max(data)+3)
diffs = []
v = 0
for k in data:
    diffs.append(k-v)
    v = k
ans_1 = diffs.count(1) * diffs.count(3)

counts = {0:1} #one way to reach the first adapter
for a in data[1:]:
    counts[a] = counts.get(a-3,0) + counts.get(a-2,0) + counts.get(a-1,0)

ans_2 = counts[data[-1]]
print(f"SOLUTION FOR PART1: {ans_1}")
print(f"SOLUTION FOR PART2: {ans_2}")
