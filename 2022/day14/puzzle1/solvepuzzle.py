import numpy as np

data = open('input.txt').readlines()
rock_movements = [d.replace('\n', '') for d in data]

#matrix = np.chararray((600,200))
#matrix[:] = '.'
matrix = [['.']*600]*600
max_depth = 0

for mov in rock_movements:
    previous = None
    cells = mov.split('->')
    for rock in cells:
        x,y = rock.split(',')
        x = int(x)
        y = int(y)
        #check if y is the new max depth
        if y > max_depth:
            max_depth = y
        matrix[y][x] = '#'
        if previous:
            if x == previous[0]:
                for i in range(y-previous[1]):
                    matrix[y-i][x] = '#'
            else:
                for i in range(x-previous[0]):
                    matrix[y][x-i] = '#'
print(matrix[:max_depth][:])

        

