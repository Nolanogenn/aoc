data = [x.split() for x in open('input.txt').readlines()]

values_shape = {'X':1, 'Y' : 2, 'Z':3}

id_columns = {'X':0, 'Y':1, 'Z':2} #rock, paper, scissors
id_rows = {'A':0, 'B':1, 'C':2} #rock, paper, scissors

#matrix for the results
results = [
        [3, 6, 0],
        [0, 3, 6],
        [6, 0, 3]
        ]

grand_total = 0
for turn in data:
    row = id_rows[turn[0]]
    column = id_columns[turn[1]]
    result = results[row][column]

    vote_shape = values_shape[turn[1]]
    total = result + vote_shape
    grand_total += total
print(grand_total)
