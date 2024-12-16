data = open('in').readlines()
data = [x.strip() for x in data]

start = [(i,j) for i in range(len(data)) for j in range(len(data[0])) if data[i][j] == 'S'][0]
end = [(i,j) for i in range(len(data)) for j in range(len(data[0])) if data[i][j] == 'E'][0]
walls = [(i,j) for i in range(len(data)) for j in range(len(data[0])) if data[i][j] == '#']

paths = []
tocheck = [
        (start,0,'>', [(-1,-1),start])
        ]

seen = {}
while tocheck:
    current_node = tocheck[0]
    tocheck = tocheck[1:]
    pos = current_node[0]
    current_value = current_node[1]
    direction = current_node[2]
    path = current_node[3]
    c = True
    if pos in walls:
        c = False
    if pos == end:
        paths.append([pos, current_value, direction, path+[end]])
        c = False
    if (path[-2],pos) in seen and c == True:
        if current_value <= seen[(path[-2], pos)] and c == True: #offset to account for changing angle
            c = True
            seen[(path[-2],pos)] = current_value
        else:
            c = False
    else:
        seen[(path[-2], pos)] = current_value
    if c:
        if direction in ['>', '<']:
            tocheck.extend(
                    [
                        ((pos[0]-1, pos[1]),current_value+1001,'^',path+[(pos[0]-1,pos[1])]),
                        ((pos[0]+1, pos[1]),current_value+1001,'v',path+[(pos[0]+1,pos[1])]),
                        ((pos[0], pos[1]-1),current_value+1,'<',path+[(pos[0], pos[1]-1)]),
                        ((pos[0], pos[1]+1),current_value+1,'>', path+[(pos[0], pos[1]+1)]),
                        ]
                    )
        if direction in ['^', 'v']:
            tocheck.extend(
                    [
                        ((pos[0]-1, pos[1]),current_value+1,'^', path+[(pos[0]-1, pos[1])]),
                        ((pos[0]+1, pos[1]),current_value+1,'v', path+[(pos[0]+1, pos[1])]),
                        ((pos[0], pos[1]-1),current_value+1001,'<', path+[(pos[0], pos[1]-1)]),
                        ((pos[0], pos[1]+1),current_value+1001,'>', path+[(pos[0], pos[1]+1)]),
                        ]
                    )
paths = sorted(paths, key= lambda x:x[1])
ans_1= paths[0][1]


best_paths = [p[3] for p in paths if p[1] == ans_1]
common_nodes = set([y for x  in best_paths for y in x])
ans_2= len(common_nodes)-1 #remove (-1,-1)

for line in data:
    pass

print(f"SOLUTION FOR PART1: {ans_1}")
print(f"SOLUTION FOR PART2: {ans_2}")
