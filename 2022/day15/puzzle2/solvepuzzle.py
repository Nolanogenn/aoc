import re
from tqdm import tqdm
from collections import defaultdict

pattern = r'[x|y]=([\-0-9]*)'
data = open('input.txt').readlines()
#data = open('test.txt').readlines()

grid = defaultdict()
mds = defaultdict()

min_x_total = min_y = 0
max_x_total = max_y = 4000000

for line in data:
    x = re.findall(pattern, line)
    sensor = (int(x[0]), int(x[1]))
    closest_beam = (int(x[2]), int(x[3]))

    manhattan_x = abs(sensor[0]-closest_beam[0])
    manhattan_y = abs(sensor[1]-closest_beam[1])
    sum_manhattan = manhattan_x + manhattan_y
    mds[sensor] = sum_manhattan

for coord in range(min_y, max_y+1):
    ranges = []
    for point in mds.items():
        dist = abs(point[0][1]-coord)
        if dist <= point[1]:
            reach = point[1]-dist
            min_x = max(point[0][0]-reach,min_x_total) 
            max_x = min(point[0][0]+reach, max_x_total)
            ranges.append((min_x, max_x))

    sorted_ranges = sorted(ranges)
    res = [sorted_ranges[0]]
    for r in sorted_ranges[1:]:
        if r[0] > res[-1][1]:
            res.append(r)
        else:
            old = res[-1]
            res[-1] = (old[0], max(old[1], r[1]))
    if len(res) == 2:
        if res[1][0] - res[0][1] > 1:
            valx = res[0][1] + res[1][0]-res[0][1]-1
            valy = coord
            total = (valx * max_y) + valy
            print(total)
            break
