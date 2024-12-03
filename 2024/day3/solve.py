import re

data = open('in').read()

ans_1= 0
ans_2= 0

pattern = r"mul\([0-9]+,[0-9]+\)"
muls = re.findall(pattern,data)

for mul in muls:
    nums = [int(x) for x in re.findall('[0-9]+', mul)]
    ans_1 += nums[0] * nums[1]

pattern += r"|do[n't]*\(\)"
commands =re.findall(pattern,data)
do = True
for command in commands:
    if command.startswith("mul") and do == True:
        nums = [int(x) for x in re.findall('[0-9]+', command)]
        ans_2 += nums[0] * nums[1]
    if command == "do()":
        do = True
    if command == "don't()":
        do = False

print(f"SOLUTION FOR PART1: {ans_1}")
print(f"SOLUTION FOR PART2: {ans_2}")
