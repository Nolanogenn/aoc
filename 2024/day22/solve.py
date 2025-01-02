from tqdm import tqdm

data = open('in').readlines()
data = [int(x.strip()) for x in data]

ans_1= 0
ans_2= 0


def mix(n,m):
    return n^m
def prune(n):
    return n%16777216
def generate_next(n):
    r = n * 64
    m = prune(mix(r,n))
    r2 = m // 32
    m2 = prune(mix(r2,m))
    r3 = m2 * 2048
    m3 = prune(mix(r3,m2))
    return m3

chains = {}
for j in tqdm(range(len(data))):
    current = data[j]
    last = current % 10
    chain = []
    for i in range(2000):
        current = generate_next(current)
        tmp = current % 10
        chain.append(tmp-last)
        if i>3:
            chain = chain[1:]
        k = ','.join([str(x) for x in chain])
        if k not in chains:
            chains[k] = ['a']*len(data)
        if k in chains and chains[k][j] == 'a':
            chains[k][j] = tmp
        last = tmp
    ans_1 += current

s = sorted(chains.items(), key=lambda x:sum([k for k in x[1] if type(k) == int]), reverse=True)
ans_2 = sum([y for y in s[0][1] if type(y) == int])

print(f"SOLUTION FOR PART1: {ans_1}")
print(f"SOLUTION FOR PART2: {ans_2}")
