data = [x.split() for x in open('input.txt').readlines()]

values_shape = {'A':1, 'B' : 2, 'C':3}
values_results = {'X' : 0 , 'Y':3, 'Z' : 6}
id_rows = {'A':0, 'B':1, 'C':2} #rock, paper, scissors
id_columns = {'X':0, 'Y':1, 'Z':2} #win, draw, lose
#matrix for the shape to choose
shapes = [
        ['C', 'A', 'B'],
        ['A', 'B', 'C'],
        ['B', 'C', 'A']
        ]


grand_total = 0
for turn in data:
    row = id_rows[turn[0]]
    column = id_columns[turn[1]]
    shape_to_take = shapes[row][column]
    value_shape = values_shape[shape_to_take]
    value_result = values_results[turn[1]]
    total = value_shape + value_result
    grand_total += total

print(grand_total)
