data = [int(x) for x in open('in').read().strip()]

ans_1= 0
ans_2= 0

v_start = 0
v_end = len(data)//2
v_pos = -1

ret = []
m = len(data)
i = 0

def checksum(l):
    ret = 0
    for i, k in enumerate(l):
        if type(k) == int:
            ret += k*i
    return ret

while i != m:
    k = data[i]
    if i % 2 != 0:
        occupy = min(data[v_pos], k)
        while k > 0:
            for _ in range(occupy):
                ret.append(v_end)
            k -= occupy
            if k > 0:
                v_pos -= 2
                v_end -= 1
                m -= 2
            else:
                data[v_pos] -= occupy
            occupy = min(data[v_pos], k)
    else:
        for _ in range(int(k)):
            ret.append(v_start)
        v_start += 1
    i += 1

ans_1 = checksum(ret)

data = [int(x) for x in open('in').read().strip()]
data_dict = {}
start = end = 0
v = 0
for i, d in enumerate(data):
    end = start+d-1
    if end >= start:
        if i %2 ==  0:
            data_dict[(start,end)] = v
            v += 1
        else:
            data_dict[(start,end)] = '.'
    start = end+1
spaces = [
        k for k in data_dict if data_dict[k] == '.'
        ]
values = [(k,data_dict[k]) for k in data_dict if data_dict[k] != '.']
torem = []
toadd = []
for j, move in enumerate(values[::-1]):
    size = move[0][1]-move[0][0]+1
    for i, space in enumerate(spaces):
        if space[0] < move[0][0]:
            space_dist = (space[1]-space[0])+1
            if size <= space_dist:
                newPos = (space[0], space[0]+size-1)
                newSpaces = []
                if size < space_dist:
                    newSpaces.append((space[0]+size, space[1]))
                data_i = len(values)-j-1
                torem.append(data_i)
                toadd.append((newPos,move[1]))
                spaces.extend(newSpaces)
                spaces = sorted(spaces)
                spaces.pop(i)
                break

values = [v for i,v in enumerate(values) if i not in torem]
for i in toadd:
    values.append(i)
values = sorted(values, key=lambda x:x[0][0])

for value in values:
    for i in range(value[0][0], value[0][1]+1):
        ans_2 += value[1]*i

print(f"SOLUTION FOR PART1: {ans_1}")
print(f"SOLUTION FOR PART2: {ans_2}")
