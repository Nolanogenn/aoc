data = [x for x in open('in').readlines()]
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
        if curr:
            shapes.append(curr)
            curr = []
        sz, gs = line.split(': ')
        sz = [int(x) for x in sz.split('x')]
        gifts = []
        for i,x in enumerate(gs.split()):
            if x != '0':
                gifts.extend([shapes[i] for _ in range(int(x))])
        regions.append((sz, gifts))

def checkBox(box,shapes):
    maxGifts = (box[0]//3)*(box[1]//3)
    occupied = sum([len(s) for s in shapes])
    if maxGifts >= len(shapes):
        return 1
    if box[0]*box[1] >= occupied:
        return 0
    return 0

ans_1= 0
for region in regions:
    box, shapes = region
    ans_1 += checkBox(box, shapes)

print(f"SOLUTION FOR PART1: {ans_1}")
