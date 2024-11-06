data = open('test').readlines()
data = [x.strip() for x in data]

ans_1= 0
ans_2= 0

for line in data:
    nums, letter, string = line.split()
    print(nums,letter,strint)

print(f"SOLUTION FOR PART1: {ans_1}")
print(f"SOLUTION FOR PART2: {ans_2}")
