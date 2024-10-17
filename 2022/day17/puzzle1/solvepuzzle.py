from pprint import pprint

#data = open('test.txt').read()
data = open('input.txt').read()
movs_ = list(data.replace('\n',''))

movs = {
        '>' : +1,
        '<' : -1
        }

#shapes given the lowest block
shapes = {
        '-' : [
            (0, 0), (0,+1), (0,+2), (0,+3)
            ],
        '+' : [
            (0,+1),(+1,+0), (+1,+1),(+1, +2), (+2, +1)
            ],
        'L' : [
            (0,0), (0, +1), (0,+2), (+1, +2), (+2, +2)
            ],
        'I': [
            (0,0), (+1,0), (+2, 0), (+3,0)
            ],
        'square' : [
            (0,0), (0,+1), (+1,0), (+1,+1)
            ]
        }
list_shapes = list(shapes.keys())
gallery = [['-' for i in range(7)]]+[['.' for i in range(7)] for k in range(100000)]
#def find_highest_point():
#    highest_point = 0
#    found = False
#    for i, level in enumerate(gallery[1:], start=1):
#        if not found:
#            if '@' in level:
#                found = True
#        else:
#            if '@' not in level:
#                highest_point = i
#                break
#    return i
        
def find_highest_point():
    highest_point = 0
    for i, level in enumerate(gallery[1:], start=1):
        if '#' not in level:
            highest_point = i
            break
    return i

rocks_settled = 0
current_shape_i = 0
current_mov_i = 0
current_highest_point = 0

shape = shapes[list_shapes[current_shape_i]]
highest_pos_x = current_highest_point + 4
highest_pos_y = 2

shape_pos = [(i[0]+highest_pos_x, i[1]+highest_pos_y) for i in shape]

highest_rock = 0

while rocks_settled < 2022:
    shape = shapes[list_shapes[current_shape_i]]
    highest_pos_x = current_highest_point + 4
    highest_pos_y = 2

    shape_pos = [(i[0]+highest_pos_x, i[1]+highest_pos_y) for i in shape]
    done=False
    while not done:
        mov = movs_[current_mov_i]
        shape_pos_tmp = [(i[0], i[1]+movs[mov]) for i in shape_pos]
        for p in shape_pos_tmp:
            if p[1] >= 7 or p[1] < 0 or gallery[p[0]][p[1]] == '#':
                break
        else:
            shape_pos = shape_pos_tmp
        if current_mov_i+1 < len(movs_):
            current_mov_i += 1
        else:
            current_mov_i = 0
        next_to_check = [gallery[i[0]-1][i[1]] for i in shape_pos]
        if '#' in next_to_check or '-' in next_to_check:
            rocks_settled += 1
            for p in shape_pos:
                gallery[p[0]][p[1]] = '#'
            if current_shape_i+1 < len(list_shapes):
                current_shape_i += 1
            else:
                current_shape_i = 0
            current_highest_point = max(i for i,r in enumerate(gallery) if '#' in r)
            done=True
        else:
            shape_pos = [(i[0]-1, i[1]) for i in shape_pos]

shape_pos = [(i[0]+4+current_highest_point, i[1]+2) for i in shapes[list_shapes[current_shape_i]]]
for point in shape_pos:
    gallery[point[0]][point[1]] = '@'
highest_point = find_highest_point()
toprint = [' '.join([str(e) for e in row]) for row in gallery[:highest_point]]
toprint.reverse()

#for i, line in enumerate(toprint):
#    print('|', line, '|')

print(highest_point-1)
