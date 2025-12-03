from functools import reduce

data = [x.strip() for x in open('in').readlines()]

def getMaxWithRest(l,lenInt):
    M = -99
    for i, elem in enumerate(l):
        if len(l)-i < lenInt:
            break
        if elem > M:
            M = elem
            maxI = i
    return (M, l[maxI+1:])


def getMaxInt(l, lenInt=2):
    if len(l) <= lenInt:
        return l
    M, ls = getMaxWithRest(l, lenInt)
    if lenInt == 1:
        return [M]
    return [M] + getMaxInt(ls, lenInt=lenInt-1)
    
def parseInput(l):
    return [int(x) for x in list(l)]

ans_1= 0
ans_2= 0

for line in data:
    parsed = parseInput(line)
    ds = reduce(lambda x,y: x*10+y, getMaxInt(parsed))
    ans_1 += ds
    ds2 = reduce(lambda x,y: x*10+y, getMaxInt(parsed,12))
    ans_2 += ds2


print(f"SOLUTION FOR PART1: {ans_1}")
print(f"SOLUTION FOR PART2: {ans_2}")
