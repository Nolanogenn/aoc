from pprint import pprint

data = open('in').readlines()
data = [x.strip() for x in data]

ans_1= 0
ans_2= 0

seats = {}

def find_num(string, start, end):
    if string == '':
        return start
    char = string[0]
    if char in ['B','R']:
        start+=(end-start)//2+1
    if char in ['F', 'L']:
        end -= (end-start)//2+1
    return find_num(string[1:], start, end)



for line in data:
    row = find_num(line[:-3],0,127)
    col = find_num(line[-3:],0,7)
    if row not in seats:
        seats[row] = set()
    seats[row].add(col)

    if row*8+col > ans_1:
        ans_1 = row*8+col

pprint(seats)

print(f"SOLUTION FOR PART1: {ans_1}")
print(f"SOLUTION FOR PART2: {ans_2}")
