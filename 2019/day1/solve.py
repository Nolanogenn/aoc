data = open('in').readlines()
data = [int(x.strip()) for x in data]

ans_1= 0
ans_2= 0

for line in data:
    x = line/3
    y = x - (x%1)
    z = y - 2
    ans_1 += z

memo = {}
def fuel(line):
    if line <= 6:
        return 0
    x = line / 3
    y = x - (x%1)
    z = y - 2
    return z + fuel(z)

for line in data:
    ans_2 += fuel(line)

print(f"SOLUTION FOR PART1: {ans_1}")
print(f"SOLUTION FOR PART2: {ans_2}")
