from pprint import pprint
data = open('test').readlines()
data = [x.strip() for x in data]

ans_1= 0
ans_2= 0

def getAdj(i,j):
    i_tocheck = [i]
    j_tocheck = [j]
    if i > 0:
        i_tocheck.append(i-1)
    if i < len(data)-1:
        i_tocheck.append(i+1)
    if j > 0:
        j_tocheck.append(j-1)
    if j < len(data[0])-1:
        j_tocheck.append(j+1)
    tocheck = [
            (x,y)
            for x in i_tocheck
            for y in j_tocheck
            if (x,y) != (i,j)
            ]
    return tocheck
adj = {
        (x,y) : getAdj(x,y)
        for x in range(len(data))
        for y in range(len(data[0]))}
memos = {}
def checkAdj(originalSymbol, symbols):
    k = ''.join([originalSymbol] + symbols)
    if k in memos:
        return memos[k]
    if originalSymbol  == 'L' and '#' not in symbols:
        memos[k] = '#'
        return '#'
    if originalSymbol == '#' and symbols.count('#') >= 4:
        memos[k] = 'L'
        return 'L'
    memos[k] = originalSymbol
    return originalSymbol
    
seen = set()
seen.add(''.join(data))

found = False
while not found:
    newData = []
    for i, line in enumerate(data):
        l = ''
        for j, row in enumerate(line):
            symbols = [data[x[0]][x[1]] for x in adj[(i,j)]]
            newSymbol = checkAdj(data[i][j], symbols)
            l += newSymbol
        newData.append(l)
    check = ''.join(newData)
    if check in seen:
        found = True
        ans_1 += sum([l.count('#') for l in newData])
    else:
        seen.add(check)
        data = newData

### PART 2  
data = open('test').readlines()
data = [x.strip() for x in data]
        
def getDiag(i,j):
    i_tocheck = []
    j_tocheck= []
    for x in range(0, i):
        i_tocheck.append(i-x)
    for y in range(0, j):
        j_tocheck.append(j-y)
    for x in range(i+1, len(data)):
        i_tocheck.append(x)
    for y in range(j+1, len(data[0])):
        j_tocheck.append(y)
    print(i,j)
    print(i_tocheck)
    print(j_tocheck)
    tocheck = [
            [(x,y)
            for x in i_tocheck if (x,y) != (i,j)]
            for y in j_tocheck
            ]
    return tocheck
diag = {
        (x,y) : getDiag(x,y)
        for x in range(len(data))
        for y in range(len(data[0]))}
memos = {}
def checkAdj(originalSymbol, symbols):
    k = ''.join([originalSymbol] + symbols)
    if k in memos:
        return memos[k]
    if originalSymbol  == 'L' and '#' not in symbols:
        memos[k] = '#'
        return '#'
    if originalSymbol == '#' and symbols.count('#') >= 4:
        memos[k] = 'L'
        return 'L'
    memos[k] = originalSymbol
    return originalSymbol

print(f"SOLUTION FOR PART1: {ans_1}")
print(f"SOLUTION FOR PART2: {ans_2}")
