import re
data = open('in').read()
p = r"[X|Y][+|-|=]([0-9]+)"
data = [x.strip().split('\n') for x in data.split("\n\n")]

ans_1= 0
ans_2= 0

def det(l):
    return (l[0][0]*l[1][1])-(l[0][1]*l[1][0])

for eq in data:
    p1 = [int(x) for x in re.findall(p, eq[0])]
    p2 = [int(x) for x in re.findall(p, eq[1])]
    sol = [int(x) for x in re.findall(p, eq[2])]
    sol2 = [10000000000000+x for x in sol]
    mat = [[p1[0], p2[0]], [p1[1],p2[1]]]
    my = [[p1[0],sol[0]], [p1[1], sol[1]]]
    mx = [[sol[0],p2[0]], [sol[1], p2[1]]]
    D = det(mat)
    Dx = det(mx)
    Dy = det(my)
    x = Dx/D
    y = Dy/D
    if x == round(x) and y == round(y):
        ans_1 += x*3 + y
    my2 = [[p1[0],sol2[0]], [p1[1], sol2[1]]]
    mx2 = [[sol2[0],p2[0]], [sol2[1], p2[1]]]
    Dx2 = det(mx2)
    Dy2 = det(my2)
    x2 = Dx2/D
    y2 = Dy2/D
    if x2 == round(x2) and y2 == round(y2):
        ans_2 += x2*3 + y2

print(f"SOLUTION FOR PART1: {ans_1}")
print(f"SOLUTION FOR PART2: {ans_2}")
