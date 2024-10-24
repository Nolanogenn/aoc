data = open('in').readlines()

pos = [int(x) for x in data[0].split(',')]
sorted_pos = list(set(sorted(pos)))
ans_1=999999999999
for p in sorted(sorted_pos):
    s = sum([abs(x-p) for x in pos])
    if s < ans_1:
        ans_1 = s

print(f"SOLUTION FOR PART1: {ans_1}")

def getFuelConsumption(dist):
    if dist in fuel:
        return fuel[dist]
    if dist == 0:
        return 0
    if dist == 1:
        return 1
    fuelConsumption = getFuelConsumption(dist-1)+ dist
    fuel[dist] = fuelConsumption
    return fuelConsumption

ans_2=9999999999999
fuel = {}
s_pos = sorted(pos)
for p1 in range(max(sorted_pos)):
    s = 0
    for p2 in s_pos:
        dist = abs(p2-p1)
        fuelC = getFuelConsumption(dist)
        s += fuelC
    if s < ans_2:
        ans_2 = s
print(f"SOLUTION FOR PART2: {ans_2}")

