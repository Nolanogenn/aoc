data = open('bigboy.txt').readlines()
data = [x.strip() for x in data]

ans_1= 0
ans_2= 0

directions = {
        "R": (0, +1),
        "L" : (0, -1),
        "U" : (-1, 0),
        "D" : (+1, 0),
        "RU" :(-1, +1),
        "RD" : (+1, +1),
        "LU" : (-1, -1),
        "LD" : (+1, -1)
        }
dirs = ["R","L","U","D", "RU", "RD", "LU", "LD"]

def get_xmas(matrix, i, j, movs, l):
    ret = []
    for mov in movs:
        s = matrix[i][j]
        for n in range(1,l):
            new_i = i + directions[mov][0]*n
            new_j = j + directions[mov][1]*n
            s += matrix[new_i][new_j]
        ret.append(s)
    return ret

def check_str_pt2(s):
    if s.count("AM") != 2 or s.count("AS") != 2:
        return False
    if s[0] == s[-1]:
        return False
    if s[1] == s[2]:
        return False
    return True
    

for i, line in enumerate(data):
    for j, char in enumerate(line):
        if char == "X":
            cards = [
                    j<=len(line)-4,
                    j>=3,
                    i>=3,
                    i<=len(data)-4]
            diags = [
                    cards[0] and cards[2],
                    cards[0] and cards[3],
                    cards[1] and cards[2],
                    cards[1] and cards[3]
                    ]
            bool_movs = cards + diags
            curr_movs = [x for i, x in enumerate(dirs) if bool_movs[i]]
            strs = get_xmas(data, i, j, curr_movs, 4)
            ans_1 += len([x for x in strs if x == 'XMAS'])
        if char == "A":
            cards = [
                    j<=len(line)-2,
                    j>=1,
                    i>=1,
                    i<=len(data)-2]
            diags = [
                    cards[0] and cards[2],
                    cards[0] and cards[3],
                    cards[1] and cards[2],
                    cards[1] and cards[3]
                    ]
            bool_movs = [False]*4 + diags
            curr_movs = [x for i, x in enumerate(dirs) if bool_movs[i]]
            strs = get_xmas(data, i, j, curr_movs, 2)
            if check_str_pt2(strs):
                ans_2 += 1

        

print(f"SOLUTION FOR PART1: {ans_1}")
print(f"SOLUTION FOR PART2: {ans_2}")
