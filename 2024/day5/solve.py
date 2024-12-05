data = open('in').read()

rules, updates = data.split('\n\n')
rules = [rule.split('|') for rule in rules.split('\n')]
rules_dict = {}
for rule in rules:
    if rule[1] not in rules_dict:
        rules_dict[rule[1]] = set()
    rules_dict[rule[1]].add(rule[0])

updates = [x.strip() for x in updates.split('\n')][:-1]

ans_1= 0
ans_2= 0

prints = []

def correct_order(x,y):
    if y in rules_dict.get(x, []):
        return False
    return True

def check_update(l):
    seen = []
    for page in l:
        tocheck = [x for x in rules_dict.get(page, []) if x in l]
        if tocheck != [] and not all([x in seen for x in tocheck]):
            return False
        seen.append(page)
    return True

def fix_update(l):
    seen = []
    isFixed = False
    while not isFixed:
        for i, j in enumerate(l[:-1]):
            if not correct_order(j, l[i+1]):
                l[i], l[i+1] = l[i+1], l[i]
        isFixed = check_update(l)
    return l


for update in updates:
    l = update.split(',')
    k = len(l)
    if check_update(l):
        ans_1 += int(l[len(l)//2])
    else:
        f = fix_update(l)
        toadd = f[k//2]
        ans_2 += int(toadd)

print(f"SOLUTION FOR PART1: {ans_1}")
print(f"SOLUTION FOR PART2: {ans_2}")

