data = open('in').readlines()
data = [x.strip().split() for x in data]

ans_1= 0
ans_2= 0

memo = {}
def is_safe(n1,n2,decr):
    k = "|".join([str(n1),str(n2),str(decr)])
    if k in memo:
        return memo[k]
    if abs(n2-n1) > 3 or n2 == n1:
        memo[k] = False
        return False
    if n2 < n1:
        if decr:
            memo[k] = True
            return True
        memo[k] = False
        return False
    if not decr:
        memo[k] = True
        return True
    memo[k] = False
    return False

def check_level(level):
    decr = level[1]<level[0]
    pairs = [is_safe(level[i],level[i+1],decr)
             for i in range(len(level)-1)]
    return pairs


for line in data:
    level = [int(x) for x in line]
    pairs = check_level(level)
    if all([x for x in pairs]):
        ans_1 += 1
        ans_2 += 1
    else:
        possible_levels = [
                [x for i,x in enumerate(level) if i != j] for j in range(len(level))
                ]
        possible_pairs = [check_level(l) for l in possible_levels]
        if any([all([x for x in p]) for p in possible_pairs]):
            ans_2 += 1

print(f"SOLUTION FOR PART1: {ans_1}")
print(f"SOLUTION FOR PART2: {ans_2}")
