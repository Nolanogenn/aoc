data = open('in').readlines()
data = [x.strip() for x in data]

ans_1= 0
ans_2= 0

def part1(line):
    elf1, elf2 = line.split(',')
    start1,end1=[int(x) for x in elf1.split('-')]
    start2,end2=[int(x) for x in elf2.split('-')]
    if start1 <= start2 and end1 >= end2:
        return 1
    if start2 <= start1 and end2 >= end1:
        return 1
    return 0

def part2(line):
    elf1, elf2 = line.split(',')
    start1,end1=[int(x) for x in elf1.split('-')]
    start2,end2=[int(x) for x in elf2.split('-')]
    if part1(line) == 1:
        return 1
    if end2 <= end1 and end2 >= start1:
        return 1
    if start2 >= start1 and start2 <= end1:
        return 1
    return 0

for line in data:
    ans_1 += part1(line)
    ans_2 += part2(line)

print(f"SOLUTION FOR PART1: {ans_1}")
print(f"SOLUTION FOR PART2: {ans_2}")
