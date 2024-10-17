import re
from tqdm import tqdm
from collections import defaultdict

pattern = r'[x|y]=([\-0-9]*)'
data = open('input.txt').readlines()
#data = open('test.txt').readlines()

grid = defaultdict()
mds = defaultdict()
for line in data:
    x = re.findall(pattern, line)
    sensor = (int(x[0]), int(x[1]))
    closest_beam = (int(x[2]), int(x[3]))

    manhattan_x = abs(sensor[0]-closest_beam[0])
    manhattan_y = abs(sensor[1]-closest_beam[1])
    sum_manhattan = manhattan_x + manhattan_y
    mds[sensor] = sum_manhattan

ranges = []
for point in mds.items():
    dist = abs(point[0][1] - 2000000)
    if dist <= point[1]:
        reach = point[1]-dist
        min_x = point[0][0]-reach
        max_x = point[0][0]+reach
        ranges.append((min_x, max_x))

sorted_ranges = sorted(ranges)
res = [sorted_ranges[0]]
for r in sorted_ranges[1:]:
    if r[0] > res[-1][1]:
        res.append(r)
    else:
        old = res[-1]
        res[-1] = (old[0], max(old[1], r[1]))

print(res)
print(res[0][1]-res[0][0])

