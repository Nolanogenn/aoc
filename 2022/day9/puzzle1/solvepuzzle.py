data = open('input.txt').readlines()
movements_h = [d.replace('\n', '').split() for d in data]

class Point:
    x = 0
    y = 0

head = Point()
tail = Point()

seen = set()
seen.add((tail.x, tail.y))

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
            head.y += operation
            if abs(head.y - tail.y) > 1:
                tail.x = head.x
                tail.y += operation
        else:
            head.x += operation
            if abs(head.x - tail.x) > 1:
                tail.y = head.y
                tail.x += operation
        seen.add((tail.x, tail.y))

print(seen)
print(len(seen))
            
            


