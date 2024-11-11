import re

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
    if not (len(passport['byr']) == 4 and int(passport['byr']) >= 1920 and int(passport['byr']) <= 2002):
        return False
    if not (len(passport['iyr']) == 4 and int(passport['iyr']) >= 2010 and int(passport['iyr']) <= 2020):
        return False
    if not (len(passport['eyr']) == 4 and int(passport['eyr']) >= 2020 and int(passport['eyr']) <= 2030):
        return False
    if not passport['hgt'][-2:] in ["cm","in"]:
        return False
    if passport['hgt'].endswith("cm") and not (int(passport["hgt"][:-2]) >= 150 and int(passport["hgt"][:-2]) <= 193):
        return False
    if passport['hgt'].endswith("in") and not (int(passport["hgt"][:-2]) >= 59 and int(passport["hgt"][:-2]) <= 76):
        return False
    if not re.search(r'#[1-9a-f]*', passport['hcl']):
        return False
    if not passport['ecl'] in ['amb', 'blu', 'brn', 'gry','grn','hzl','oth']:
        return False
    f = re.search(r'\d{9}', passport['pid'])
    if not f:
        return False
    if not f[0] == passport['pid']:
        return False
    print(passport)
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
