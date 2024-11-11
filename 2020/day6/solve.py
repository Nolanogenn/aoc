data = open('in').readlines()
data = [x.strip() for x in data]

ans_1= 0
ans_2= 0

seen = set()
for line in data:
    if line == '':
        ans_1 += len(seen)
        seen = set()
    else:
        for char in line:
            seen.add(char)
ans_1 += len(seen)

seen = set()
start = True
for line in data:
    if line == '':
        print(seen)
        ans_2 += len(seen)
        seen = set()
        start = True
    else:
        if start:
            for char in line:
                seen.add(char)
            start = False
        else:
            rem = []
            for char in seen:
                if char not in line:
                    rem.append(char)
            for r in rem:
                seen.remove(r)
ans_2 += len(seen)

print(f"SOLUTION FOR PART1: {ans_1}")
print(f"SOLUTION FOR PART2: {ans_2}")
