data = open('in').readlines()
#data = [x.strip() for x in data]

valuesToCover = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]

ans_1= 0
ans_2= 0

passport = []
for line in data:
    if line == "\n":
        notcovered = [x for x in valuesToCover if x not in passport and x != "cid"]
        if len(notcovered) == 0:
            ans_1 += 1
        passport = []
    else:
        values = line.replace("\n", '').strip().split(" ")
        passport.extend([x.split(':')[0] for x in values])
notcovered = [x for x in valuesToCover if x not in passport and x != "cid"]
if len(notcovered) == 0:
    ans_1 += 1

def checkvalues(passport):
    if not len(passport['byr']) == 4 and int(passport['byr']) >= 1920 and int(passport['byr']) <= 2002:
        return False

    return True

passport = {}
for line in data:
    if line == "\n":
        notcovered = [x for x in valuesToCover if x not in passport and x != "cid"]
        if len(notcovered) == 0:
            if checkvalues(passport):
                ans_2 += 1
        passport = {}
    else:
        values = line.replace("\n", '').strip().split(" ")
        for value in values:
            passport[value.split(':')[0]] = value.split(':')[1]
notcovered = [x for x in valuesToCover if x not in passport and x != "cid"]
if len(notcovered) == 0:
    if checkvalues(passport):
        ans_2 += 1

print(f"SOLUTION FOR PART1: {ans_1}")
print(f"SOLUTION FOR PART2: {ans_2}")
