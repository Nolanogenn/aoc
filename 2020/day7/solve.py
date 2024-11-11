import re

data = open('in').readlines()
data = [x.strip() for x in data]

ans_1= 0
ans_2= 0

seen = set()
search_for = ["shiny gold"]
while search_for:
    bag = search_for[0]
    search_for = search_for[1:]
    for line in data:
        x = re.search(r"[^\n]"+bag, line)
        if x:
            b = ' '.join(line.split()[:2])
            if b not in search_for:
                search_for.append(b)
                seen.add(b)
ans_1 = len(seen)

check = [("shiny gold", 1)]
curr_bags = 0
while check:
    bag = check[0]
    check = check[1:]
    curr_bags += bag[1]
    for line in data:
        if line.startswith(bag[0]):
            l = line.split()
            if " no " in l:
                pass
            else:
                digits = [(i, x) for i, x in enumerate(l) if x.isnumeric()]
                for d in digits:
                    n = int(d[1])
                    b = ' '.join(l[d[0]+1:d[0]+3])
                    check.append((b, n*bag[1]))
ans_2 = curr_bags -1 #remove the shiny gold one

print(f"SOLUTION FOR PART1: {ans_1}")
print(f"SOLUTION FOR PART2: {ans_2}")
