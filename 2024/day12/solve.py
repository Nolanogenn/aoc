data = open('in').readlines()
data = [x.strip() for x in data]

patches = {}
seen = set()

for i, line in enumerate(data):
    for j, k in enumerate(line):
        if (i,j) not in seen:
            a = 0
            p = 0
            queue = [(i,j)]
            visited = set()
            while queue:
                elem = queue.pop()
                if elem not in visited:
                    visited.add(elem)
                    seen.add(elem)
                    a +=1
                    if elem[0] <= 0:
                        p += 1
                    else:
                        tocheck = (elem[0]-1, elem[1])
                        if data[tocheck[0]][tocheck[1]] != data[i][j]:
                            p += 1
                        else:
                            queue.append(tocheck)
                    if elem[1] <= 0:
                        p += 1
                    else:
                        tocheck = (elem[0], elem[1]-1)
                        if data[tocheck[0]][tocheck[1]] != data[i][j]:
                            p += 1
                        else:
                            queue.append(tocheck)
                    if elem[0] >= len(data)-1:
                        p += 1
                    else:
                        tocheck = (elem[0]+1, elem[1])
                        if data[tocheck[0]][tocheck[1]] != data[i][j]:
                            p += 1
                        else:
                            queue.append(tocheck)
                    if elem[1] >= len(data[0])-1:
                        p += 1
                    else:
                        tocheck = (elem[0], elem[1]+1)
                        if data[tocheck[0]][tocheck[1]] != data[i][j]:
                            p += 1
                        else:
                            queue.append(tocheck)
            patches[(i,j)] = (a,p,visited)


ans_1= 0
ans_2= 0

for v in patches.values():
    ans_1 += v[0]*v[1]

for patch in patches:
    a = patches[patch][0]
    squares = patches[patch][2]
    walls = []
    for square in squares:
        if (square[0]-1, square[1]) not in squares:
            walls.append((square[0], square[1], '^'))
        if (square[0]+1, square[1]) not in squares:
            walls.append((square[0], square[1], 'v'))
        if (square[0], square[1]+1) not in squares:
            walls.append((square[0], square[1], '>'))
        if (square[0], square[1]-1) not in squares:
            walls.append((square[0], square[1], '<'))
    visited = set()
    walls = sorted(walls)
    p = 0
    for wall in walls:
        if wall[2] in ['^', 'v']:
            if not (wall[0], wall[1]-1, wall[2]) in visited and not (wall[0], wall[1]+1, wall[2]) in visited:
                p += 1
        if wall[2] in ['<', '>']:
            if not (wall[0]-1, wall[1], wall[2]) in visited and not (wall[0]+1, wall[1], wall[2]) in visited:
                p += 1
        visited.add(wall)
    ans_2 += p*a
        


print(f"SOLUTION FOR PART1: {ans_1}")
print(f"SOLUTION FOR PART2: {ans_2}")
