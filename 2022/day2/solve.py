data = open('in').readlines()
data = [x.strip() for x in data]

ans_1= 0
ans_2= 0

same = {
        'A':'X',
        'B':'Y',
        'C':'Z'
        }
scores = {
        'X':1,
        'Y':2,
        'Z':3
        }
win = {
        'A':'Y',
        'B':'Z',
        'C':'X'
        }
lose = {
        'A':'Z',
        'B':'X',
        'C':'Y'
        }
for line in data:
    opp, me = line.split(' ')
    v = scores[me]
    if same[opp] == me:
        v += 3
    elif me == win[opp]:
        v += 6
    ans_1 += v

for line in data:
    opp, me = line.split(' ')
    if me == 'X':
        actual_me = lose[opp]
        v = 0
    elif me == 'Y':
        actual_me = same[opp]
        v = 3
    else:
        actual_me = win[opp]
        v = 6
    v += scores[actual_me]
    ans_2 += v

print(f"SOLUTION FOR PART1: {ans_1}")
print(f"SOLUTION FOR PART2: {ans_2}")
