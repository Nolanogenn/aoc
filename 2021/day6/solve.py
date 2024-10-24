from collections import defaultdict
data = open('in').read().strip()
nums = [int(x) for x in data.split(',')]

X = defaultdict(int)
for n in nums:
    if n not in X:
        X[n] = 0
    X[n] += 1

for d in range(256):
    Y = defaultdict(int)
    for k, cnt in X.items():
        if k == 0:
            Y[6] += cnt
            Y[8] += cnt
        else:
            Y[k-1] += cnt
    X = Y
print(sum(X.values()))
