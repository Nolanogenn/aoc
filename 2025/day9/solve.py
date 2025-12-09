import numpy as np
import shapely
import itertools

def getArea(x,y):
    h = abs(x[0]-y[0])+1
    w = abs(x[1]-y[1])+1
    return h*w

def gethw(x,y):
    h = min((x[0], y[0]))
    H = max((x[0], y[0]))
    w = min((x[1], y[1]))
    W = max((x[1], y[1]))
    return h,H,w,W

data = [x.strip().split(',') for x in open('in').readlines()]
tiles = [(int(x[0]), int(x[1])) for x in data]
x = sorted([t[0] for t in tiles])
y = sorted([t[1] for t in tiles])

tilesPairs = list(itertools.combinations(tiles,2))

areas = [(getArea(x[0], x[1]),x) for x in tilesPairs]
areas = sorted(areas)
best = areas.pop()
ans_1 = best[0]
print(f"SOLUTION FOR PART1: {ans_1}")

ans_2= 0
polygon = shapely.Polygon(tiles)
found = False
while not found:
    xmin,xmax,ymin,ymax = gethw(best[1][0], best[1][1])
    geom = shapely.box(xmin,ymin,xmax,ymax)
    if shapely.contains(polygon, geom):
        found = True
    else:
        best = areas.pop()
ans_2 = best[0]
print(f"SOLUTION FOR PART2: {ans_2}")
