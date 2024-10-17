import scipy.ndimage as ndi
import numpy as np
from collections import defaultdict
from pprint import pprint

#data = open('test.txt').readlines()
data = open('input.txt').readlines()
cubes = [d.replace('\n', '') for d in data]

connections = {}

#for cube in cubes:
#    cube = [int(x) for x in cube.split(',')]
#    cube_hash = (cube[0], cube[1], cube[2])
#    connections[cube_hash] = []
#    for cube2 in cubes:
#        cube2 = [int(x) for x in cube2.split(',')]
#        distances = [
#                abs(cube[0]-cube2[0]),
#                abs(cube[1]-cube2[1]),
#                abs(cube[2]-cube2[2])
#                ]
#        if sum(distances) == 1:
#            connections[cube_hash].append(cube2)

#min_x = min([i[0] for i in connections])
#min_y = min([i[1] for i in connections])
#min_z = min([i[2] for i in connections])
#max_x = max([i[0] for i in connections])
#max_y = max([i[1] for i in connections])
#max_z = max([i[2] for i in connections])


#while queue:
#    current = queue.pop()
#    if current not in filled and current not in connections:
#        filled.append(current)
#    next_candidates = [
#            (
#                current[0]+m[0],
#                current[1]+m[1],
#                current[2]+m[2]
#            )
#            for m in movs
#            ]
#    for n in next_candidates:
#        if (n[0] >= min_x and n[0] <= max_x) and (n[1] >= min_y and n[1] <= max_y) and (n[2] >= min_z and n[2] <= max_z):
#            queue.append(n)

cubes = np.array([[int(x) for x in row.split(',')] for row in cubes])
space = np.zeros(cubes.max(axis=0) + 1)

i, j, k = cubes.T
space[i,j,k] = 1
space =  ndi.binary_fill_holes(space)

cubes = set(zip(*np.where(space)))
exposed = 0
for x,y,z in cubes:
    for dx, dy, dz in (
            (1,0,0),
            (-1,0,0),
            (0,1,0),
            (0,-1,0),
            (0,0,1),
            (0,0,-1),
            ):
        if (x+dx, y+dy, z+dz) not in cubes:
            exposed += 1
print(exposed)
