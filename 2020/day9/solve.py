import math

data = open('in').readlines()
data = [int(x.strip()) for x in data]

ans_1= 0
ans_2= 0

for i, line in enumerate(data[25:]):
    toFind = int(line)
    preamble = [int(x) for x in data[i:25+i]]
    values = [toFind - x for x in preamble]
    if all([x not in preamble for x in values if toFind//2 != x]):
        ans_1 = toFind
        break

def part2(ans_1, total, index_start, index_end, min_value, max_value):#num to find, total, index start, index end, min and max
    if total == ans_1:
        return min_value + max_value
    if total > ans_1:
        return False
    index_end += 1
    return part2(ans_1, sum(data[index_start:index_end]), index_start, index_end, min(data[index_start:index_end]), max(data[index_start:index_end]))
    
for k in range(len(data)):
    x = part2(ans_1, data[k], k, k+1, data[k], data[k])
    if x != False:
        ans_2 = x
        break


print(f"SOLUTION FOR PART1: {ans_1}")
print(f"SOLUTION FOR PART2: {ans_2}")
