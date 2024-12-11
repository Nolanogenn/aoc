from tqdm import tqdm 
data = open('in').read()
data = [int(x) for x in data.strip().split()]

ans_1= 0
ans_2= 0

memos = {}

def solver(n):
    ret = n
    if n in memos:
        return memos[n]
    if n == 0:
        ret = (1,)
    elif len(str(n))%2 == 0:
        l = len(str(n))//2
        ret = (int(str(n)[:l]),int(str(n)[l:]))
    else:
        ret = (n*2024,)
    memos[n] = ret
    return ret

def solve(blinks):
    nums = {n:1 for n in data}
    for _ in tqdm(range(blinks)):
        x = {}
        for n in nums:
            vs = solver(n)
            for v in vs:
                if v not in x:
                    x[v] = 0
                x[v] += nums[n]
        nums = x
    return x

ans_1 = sum(solve(25).values())
ans_2 = sum(solve(75).values())

print(f"SOLUTION FOR PART1: {ans_1}")
print(f"SOLUTION FOR PART2: {ans_2}")
