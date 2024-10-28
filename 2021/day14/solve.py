data = open('in').readlines()
data = [x.strip() for x in data]

polymer=data[0]
subs=[x.split(' -> ') for x in data[2:]]
s={}

for sub in subs:
    s[sub[0]] = sub[1]

counts = {
        x:polymer.count(x) if x in polymer else 0 for x in s 
        }
letters = {l:polymer.count(l) for l in polymer}

ans_1= 0
ans_2= 0

for i in range(40):
    newCounts = {key:0 for key in counts}
    for k in counts:
        if counts[k] > 0:
            n = s[k]
            p1 = k[0]+n
            p2 = n+k[1]
            if n not in letters:
                letters[n] = 0
            letters[n] += 1*counts[k]
            newCounts[p1] += counts[k]
            newCounts[p2] += counts[k]
    counts = newCounts
    sorted_letters = sorted(letters.items(), key= lambda x: x[1])
    if i == 9:
        ans_1=sorted_letters[-1][1]-sorted_letters[0][1]
ans_2=sorted_letters[-1][1]-sorted_letters[0][1]


print(f"SOLUTION FOR PART1: {ans_1}")
print(f"SOLUTION FOR PART2: {ans_2}")
