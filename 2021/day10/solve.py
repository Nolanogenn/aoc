data = open('in').readlines()
data = [x.strip() for x in data]

ans_1= 0
ans_2= 0

points = {
        ')' : 3,
        ']' : 57,
        '}' : 1197, 
        '>' : 25137
        }
autocomplete = {
        "(" : 1,
        "[" : 2,
        "{" : 3, 
        "<" : 4
        }
scores = []
for line in data:
    o = {')':'(', ']':'[', '}':'{', '>':'<'}
    S = []
    score = 0
    corrupted=False
    for char in line:
        if char in ['(', '[', '{', '<']:
            S.append(char)
        elif S[-1] != o[char]:
            ans_1 += points[char]
            corrupted=True
            break
        else:
            S = S[:-1]
    if not corrupted:
        for s in S[::-1]:
            score *= 5
            score += autocomplete[s]
        scores.append(score)

scores = sorted(scores)
print(scores)
ans_2 = scores[len(scores)//2]
print(f"SOLUTION FOR PART1: {ans_1}")
print(f"SOLUTION FOR PART2: {ans_2}")
