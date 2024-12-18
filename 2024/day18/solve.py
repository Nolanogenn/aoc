data = open('in').readlines()
data = [x.strip().split(',') for x in data]
walls = [(int(x[1]), int(x[0])) for x in data]

ans_1= 0
ans_2= 0



start = (0,0,[(0,0)])
end = (70,70) 

max_grid = (max([x[0] for x in walls]), max([x[1] for x in walls]))

def check_boundaries(pos, walls):
    if (pos[0],pos[1]) in walls:
        return False
    if not 0 <= pos[0] <= max_grid[0]:
        return False
    if not 0 <= pos[1] <= max_grid[1]:
        return False
    return True

def check_pos(pos, path, seen):
    if pos not in seen:
        return True
    if len(path) < seen[pos]:
        return True
    return False

def get_best_path(start,end,walls):
    paths = []
    tocheck = [start]
    seen = {}
    while tocheck:
        p = tocheck.pop(0)
        pos = (p[0],p[1])
        current_path = p[2]
        if (p[0],p[1]) == end:
            paths.append(p)
        else:
            next_up = (pos[0]-1,pos[1])
            tmp_path = current_path+[next_up]
            if check_pos(next_up, tmp_path, seen) and check_boundaries(next_up, walls):
                seen[next_up] = len(tmp_path)
                tocheck.append((next_up[0], next_up[1], tmp_path))

            next_down = (pos[0]+1,pos[1])
            tmp_path = current_path+[next_down]
            if check_pos(next_down, tmp_path, seen) and check_boundaries(next_down, walls):
                seen[next_down] = len(tmp_path)
                tocheck.append((next_down[0], next_down[1], tmp_path))

            next_right = (pos[0],pos[1]+1)
            tmp_path = current_path+[next_right]
            if check_pos(next_right, tmp_path, seen) and check_boundaries(next_right, walls):
                seen[next_right] = len(tmp_path)
                tocheck.append((next_right[0], next_right[1], tmp_path))

            next_left = (pos[0],pos[1]-1)
            tmp_path = current_path+[next_left]
            if check_pos(next_left, tmp_path, seen) and check_boundaries(next_left, walls):
                seen[next_left] = len(tmp_path)
                tocheck.append((next_left[0], next_left[1], tmp_path))
    return paths

best_path = sorted(get_best_path(start,end,walls[:1024]),key=lambda x:len(x[2]))[0]
ans_1 = len(best_path[2])-1
print(f"SOLUTION FOR PART1: {ans_1}")

half_pos = len(walls)//2
i = 0
while abs(half_pos-i) > 1:
    w = walls[:half_pos]
    paths = get_best_path(start,end,w)
    if len(paths) == 0:
        half_pos -= (half_pos-i)//2
    else:
        tmp_i = int(half_pos)
        half_pos += (half_pos-i)//2
        i = tmp_i
ans_2 = walls[half_pos][::-1]
print(f"SOLUTION FOR PART2: {ans_2}")
