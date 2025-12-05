def getR(x):
    m, M = x.split('-')
    return [int(m), int(M)]

def isFresh(x, ranges):
    for r in ranges:
        if x >= r[0] and x <= r[1]:
            return True
    return False

def getNewRanges(ranges):
    newRanges = []
    skip = False
    for i, elem in enumerate(ranges):
        if skip:
            skip = False
            pass
        elif i == len(ranges) -1:
            newRanges.append(elem)
            pass
        else:
            if elem[1] >= ranges[i+1][1]:
                newRanges.append(elem)
                skip = True
            elif elem[1] >= ranges[i+1][0]:
                newRanges.append([elem[0], ranges[i+1][1]])
                skip = True
            else:
                newRanges.append(elem)
    return newRanges

ranges, ingr = open('in').read().strip().split('\n\n')
ranges = sorted([getR(r) for r in ranges.split('\n')])
ingr = [int(x) for x in ingr.split('\n')]

ans_1= 0
ans_2= 0

newRanges = getNewRanges(ranges)
while len(newRanges) != len(ranges):
    ranges = newRanges
    newRanges = getNewRanges(ranges)

for i in ingr:
    ans_1 += isFresh(i, ranges)
ans_2 = sum([x[1]-x[0]+1 for x in ranges])

print(f"SOLUTION FOR PART1: {ans_1}")
print(f"SOLUTION FOR PART2: {ans_2}")
