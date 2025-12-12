data = [x for x in open('test').readlines()]
shapes = []
regions = []
curr = []
for line in data:
    if ":\n" in line:
        if curr:
            shapes.append(curr)
        curr = []
        pos = 0
    elif "#" in line:
        r = [(pos,i) for i,k in enumerate(line) if k == '#']
        curr.extend(r)
        pos += 1
    elif ":" in line:
        sz, gs = line.split(': ')
        sz = [int(x) for x in sz.split('x')]
        gifts = []
        for i,x in enumerate(gs.split()[:-1]):
            if x != '0':
                gifts.extend([shapes[i] for _ in range(int(x))])
        regions.append((sz, gifts))

def checkBoundaries(pos,box):
    w,h = box
    if 0 <= pos[0] < h and 0 <= pos[1] < w:
        return True
    return False

def move(shape, box, d):
    n = [(s[0]+d[0], s[1]+d[1]) for s in shape]
    if any([not checkBoundaries(s, box) for s in n]):
        return []
    return n
    

ans_1= 0
ans_2= 0

for region in regions:
    box, shapes = region
    print(move(shapes[0], box, (2,0)))
    break

print(f"SOLUTION FOR PART1: {ans_1}")
print(f"SOLUTION FOR PART2: {ans_2}")
