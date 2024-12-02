data = open('in').readlines()
data = [x.strip() for x in data][0]

ans_1= 0
ans_2= 0

memo = set()
def checkStr(s):
    if s in memo:
        return False
    if len(s) == len(set(s)):
        return True
    memo.add(s)
    return False

for i in range(len(data)):
    toCheck = data[i:i+4]
    if checkStr(toCheck):
        ans_1 = i+4
        break
for i in range(len(data)):
    toCheck = data[i:i+14]
    if checkStr(toCheck):
        ans_2 = i+14
        break



print(f"SOLUTION FOR PART1: {ans_1}")
print(f"SOLUTION FOR PART2: {ans_2}")
