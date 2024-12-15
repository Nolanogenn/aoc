data = open('in').read()
grid, movs = data.split('\n\n')
movs = movs.strip().replace('\n', '')
lines = grid.split('\n')

robot = (0,0)
stones = set()
walls = set()

for i,line in enumerate(lines):
    for j,col in enumerate(line):
        if col == '#':
            walls.add((i,j))
        elif col == 'O':
            stones.add((i,j))
        elif col == '@':
            robot = (i,j)

mov_d = {
        "^":(-1,0),
        ">":(0,+1),
        "v":(+1,0),
        "<":(0,-1)
        }

def move(pos,mov,tomove):
    newpos = (pos[0]+mov_d[mov][0], pos[1]+mov_d[mov][1])
    if newpos in walls:
        return (False, [])
    if newpos in stones:
        tomove[1].add(newpos)
        return move(newpos,mov,tomove)
    else:
        tmpStones = set(stones)
        robot = (tomove[0][0]+mov_d[mov][0], tomove[0][1]+mov_d[mov][1])
        moved = []
        if len(tomove[1]) > 0:
            for s in tomove[1]:
                tmpStones.remove(s)
                moved.append((s[0]+mov_d[mov][0],s[1]+mov_d[mov][1]))
            for m in moved:
                tmpStones.add(m)
        return (True, robot, tmpStones)

def gps(stone):
    return 100 * stone[0] + stone[1]

ans_1= 0
ans_2= 0

for mov in movs:
    res = move(robot,mov,[robot,set()])
    if res[0] == True:
        robot = res[1]
        stones = res[2]

ans_1 = sum([gps(x) for x in stones])
#### PART 2

robot = (0,0)
stones = set()
walls = set()

mov_d = {
        "^":(-1,0,0),
        ">":(0,+1,+1),
        "v":(+1,0,0),
        "<":(0,-1,-1)
        }
for i,line in enumerate(lines):
    for j,col in enumerate(line):
        if col == '#':
            walls.add((i,j*2,j*2+1)) #line, start, end
        elif col == 'O':
            stones.add((i,j*2,j*2+1))
        elif col == '@':
            robot = (i,j*2)
def get_tocheck(pos, d):
    if d == '<':
        tocheck = [(pos[0], pos[1]-2,pos[2]-2)]
    elif d == '>':
        tocheck = [(pos[0], pos[1]+2,pos[2]+2)]
    elif d == '^':
        tocheck = [
                (pos[0]-1,pos[2],pos[2]+1),
                (pos[0]-1,pos[1]-1,pos[1]),
                (pos[0]-1,pos[1],pos[2]),
                ]
    elif d == 'v':
        tocheck = [
                (pos[0]+1,pos[2],pos[2]+1),
                (pos[0]+1,pos[1]-1,pos[1]),
                (pos[0]+1,pos[1],pos[2]),
                ]
    return tocheck
def get_tocheck_robot(pos, d):
    if d == '<':
        tocheck = [(pos[0], pos[1]-2,pos[1]-1)]
    elif d == '>':
        tocheck = [(pos[0], pos[1]+1,pos[1]+2)]
    elif d == '^':
        tocheck = [
                (pos[0]-1,pos[1]-1,pos[1]),
                (pos[0]-1,pos[1],pos[1]+1),
                ]
    elif d == 'v':
        tocheck = [
                (pos[0]+1,pos[1]-1,pos[1]),
                (pos[0]+1,pos[1],pos[1]+1),
                ]
    return tocheck

def move(d,tocheck):
    tomove = set()
    while tocheck:
        checking = tocheck[0]
        tocheck = tocheck[1:]
        if checking in walls:
            return (False, [])
        if checking in stones:
            tomove.add(checking)
            tocheck.extend(get_tocheck(checking,d))
        else:
            continue
    tmpStones = set(stones)
    moved = []
    if len(tomove) > 0:
        for s in tomove:
            tmpStones.remove(s)
            moved.append(
                    (
                        s[0]+mov_d[d][0],
                        s[1]+mov_d[d][1],
                        s[2]+mov_d[d][2])
                    )
        for m in moved:
            tmpStones.add(m)
    return (True, tmpStones)

for d in movs:
    mov = mov_d[d]
    newRobot = (robot[0]+mov[0], robot[1]+mov[1])
    tocheck = get_tocheck_robot(robot,d)
    res = move(d,tocheck)
    if res[0] == True:
        robot = newRobot
        stones = res[1]

print(robot,"||", sorted(stones))

ans_2 = sum([gps(x) for x in stones])
print(f"SOLUTION FOR PART1: {ans_1}")
print(f"SOLUTION FOR PART2: {ans_2}")
