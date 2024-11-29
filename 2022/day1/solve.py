data = open('in').readlines()
data = [x.strip() for x in data]

ans_1= 0
ans_2= 0

cals = []
currCal = 0
for line in data:
    if line == '':
        cals.append(currCal)
        currCal = 0
    else:
        currCal += int(line)
ans_1 = max(cals)

top_3 = sorted(cals, reverse=True)[:3]
ans_2 = sum(top_3)

print(f"SOLUTION FOR PART1: {ans_1}")
print(f"SOLUTION FOR PART2: {ans_2}")
