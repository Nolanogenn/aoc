data = open('input.txt').readlines()
movements_h = [d.replace('\n', '').split() for d in data]

class Point:
    def __init__(self, previousPoint = None):
        self.x = 0
        self.y = 0
        self.previousPoint = previousPoint

points = []
head = Point()
points.append(head)

previousPoint = head
for knot in range(1,10):
    p = Point(previousPoint=previousPoint)
    points.append(p)
    previousPoint=p

seen = set()
seen.add((0,0))
movements = {
        'U' : [0, +1],
        'D' : [0, -1],
        'R' : [1, +1],
        'L' : [1, -1]
        }

for m in movements_h:
    direction = m[0]
    steps = int(m[1])
    for _ in range(steps):
        where, operation = movements[direction]
        if where == 0:
            points[0].y += operation
        else:
            points[0].x += operation
        for i in range(1,10):
            abs_y = abs(points[i-1].y - points[i].y) > 1
            abs_x =  abs(points[i-1].x - points[i].x) > 1
            if abs_x:
                if not abs_y:
                    points[i].y = points[i-1].y
                if points[i-1].x > points[i].x:
                    points[i].x= points[i-1].x -1
                else:
                    points[i].x=points[i-1].x+1
            if abs_y:
                if not abs_x:
                    points[i].x = points[i-1].x
                if points[i-1].y > points[i].y:
                    points[i].y= points[i-1].y -1
                else:
                    points[i].y=points[i-1].y+1
        seen.add((points[-1].x, points[-1].y))

print(len(seen))
            
            

