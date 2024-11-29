data = open('in').readlines()
data = [x.strip() for x in data]

ans_1= 0
ans_2= 0

lower = [chr(x) for x in range(ord('a'), ord('z')+1)]
upper = [chr(x) for x in range(ord('A'), ord('Z')+1)]
letters = lower + upper
values = list(range(1,53))
prio = {
        letters[i]:values[i]
        for i in range(len(letters))
        }
for line in data:
    split_at = len(line)//2
    item1 = line[:split_at]
    item2 = line[split_at:]
    incommon = [x for x in item1 if x in item2][0]
    ans_1 += prio[incommon]

i = 0
for line in data[::3]:
    group = [line, data[i+1], data[i+2]]
    inCommon = [x for x in group[0] if x in group[1]]
    inCommon = [x for x in group[2] if x in inCommon][0]
    i += 3
    ans_2 += prio[inCommon]

print(f"SOLUTION FOR PART1: {ans_1}")
print(f"SOLUTION FOR PART2: {ans_2}")
