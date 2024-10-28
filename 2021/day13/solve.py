from pprint import pprint
data = open('in').read()
movs, folds = data.split('\n\n')
points = set([(int(x.split(',')[0]), int(x.split(',')[1])) for x in movs.split('\n')])
folds = [x.split()[-1] for x in folds.split('\n') if len(x) > 1]

def foldAlong(point, along, direction):
    newpoint = [point[0], point[1]]
    if direction=='y':
        newpoint[1]=2*along-point[1]
    else:
        newpoint[0]=2*along-point[0]
    return tuple(newpoint)

ans_1= 0
ans_2= 0

for i, fold in enumerate(folds):
    d,a=fold.split('=')
    a=int(a)
    ps = []
    remove=[]
    if d == 'y':
        toprocess = [p for p in points if p[1]>=a]
    else:
        toprocess = [p for p in points if p[0]>=a]
    for point in toprocess:
        p=foldAlong(point,a,d)
        print(f"{point}->{p}")
        ps.append(p)
    for x in ps:
        points.add(x)
    for x in toprocess:
        points.remove(x)
    if i == 0:
        ans_1 = len(points)

h = max([x[1] for x in points])
w = max([x[0] for x in points])

grid = [['.' for _ in range(w+1)] for _ in range(h+1)]
for p in points:
    grid[p[1]][p[0]] = '#'
grid = [''.join(line) for line in grid]
pprint(grid)

print(f"SOLUTION FOR PART1: {ans_1}")
print(f"SOLUTION FOR PART2: {ans_2}")
