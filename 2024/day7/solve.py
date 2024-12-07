from tqdm import tqdm 
data = open('in').readlines()
data = [x.strip().split(':') for x in data]

ans_1= 0
ans_2= 0

def generate_sol(eq):
    ret = [eq[0]]
    for y in eq[1:]:
        toext = []
        torem=0
        for x in ret:
            torem+=1
            v1 = x * y
            v2 = x + y
            toext.append(v1)
            toext.append(v2)
        for _ in range(torem):
            ret.pop(0)
        ret += toext
    return ret

def generate_sol_2(eq):
    ret = [eq[0]]
    for y in eq[1:]:
        toext = []
        torem=0
        for x in ret:
            torem+=1
            v1 = x * y
            v2 = x + y
            v3 = int(str(x)+str(y))
            toext.append(v1)
            toext.append(v2)
            toext.append(v3)
        for _ in range(torem):
            ret.pop(0)
        ret += toext
    return ret
for line in tqdm(data):
    sol, eq = line
    eq = [int(x) for x in eq.split()]
    if int(sol) in generate_sol(eq):
        ans_1 += int(sol)
    if int(sol) in generate_sol_2(eq):
        ans_2 += int(sol)

print(f"SOLUTION FOR PART1: {ans_1}")
print(f"SOLUTION FOR PART2: {ans_2}")
