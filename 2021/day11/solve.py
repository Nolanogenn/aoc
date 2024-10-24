from pprint import pprint
data = open('in').readlines()
board = [x.strip() for x in data]

ans_1= 0
ans_2= 0
turns = 0
m = {}

found = False
while not found:
    illuminated = set()
    if '\n'.join(board) in m:
        state = m['\n'.join(board)]
    else:
        state = [[int(x) for x in l] for l in board]
        toCheck = [(x, y) for x in range(len(state)) for y in range(len(state[0]))]
        while toCheck:
            checking= toCheck[0]
            toCheck = toCheck[1:]
            if checking not in illuminated:
                state[checking[0]][checking[1]] += 1
                currentNum = state[checking[0]][checking[1]] 
                if currentNum > 9:
                    state[checking[0]][checking[1]] = 0                 
                    illuminated.add((checking[0], checking[1]))
                    possible_movs = [x for x in [
                            (checking[0]-1, checking[1]),
                            (checking[0]-1, checking[1]-1),
                            (checking[0]-1, checking[1]+1),
                            (checking[0], checking[1]-1),
                            (checking[0], checking[1]+1),
                            (checking[0]+1, checking[1]),
                            (checking[0]+1, checking[1]-1),
                            (checking[0]+1, checking[1]+1),
                            ] if x[0]>=0 and x[0]<len(state) and x[1]>=0 and x[1]<len(state[0])]
                    toCheck.extend(possible_movs)
    m['\n'.join(board)] = state
    board = [''.join([str(x) for x in line]) for line in state]
    turns += 1
    if turns <= 100:
        ans_1 += sum([x.count('0') for x in board])
    totest = ['0'*len(board[0])]*len(board)
    if totest == board:
        print(board)
        found = True

ans_2 += turns
print(f"SOLUTION FOR PART1: {ans_1}")
print(f"SOLUTION FOR PART2: {ans_2}")
