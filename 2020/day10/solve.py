data = open('test').readlines()
data = [int(x.strip()) for x in data]

ans_1= 0
ans_2= 0

data = sorted(data)
data.append(max(data)+3)
diffs = []
v = 0
for k in data:
    diffs.append(k-v)
    v = k
ans_1 = diffs.count(1) * diffs.count(3)

def path(curr, l):
    if l == []:
        print("found")
        ans_2 += 1
        return True
    for i in range(min(3, len(l))):
        if l[i] <= curr + 3:
            c = l[i]
            l2 = l[i+1:]
            path(c, l2)
        else:
            continue
path(data[0],data[1:])

print(f"SOLUTION FOR PART1: {ans_1}")
print(f"SOLUTION FOR PART2: {ans_2}")
