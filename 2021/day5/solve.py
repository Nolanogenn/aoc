covered_squares = {}
for line in open('in').readlines():
    move = line.strip().split(' -> ')
    x1,y1 = [int(point) for point in move[0].split(',')]
    x2,y2= [int(point) for point in move[1].split(',')]
    dx=x2-x1
    dy=y2-y1
    for i in range(1+max(abs(dx),abs(dy))):
        x = x1 + (1 if dx>0 else (-1 if dx<0 else 0))*i
        y = y1 + (1 if dy>0 else (-1 if dy<0 else 0))*i
        if (x,y) not in covered_squares:
            covered_squares[(x,y)] = 0
        covered_squares[(x,y)]+=1

#part1
ans = 0
for k in covered_squares:
    if covered_squares[k] > 1:
        ans += 1
print(f"SOLUTION FOR PT2: {ans}")

#part2
