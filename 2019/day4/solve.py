data = open('in').read()
r = data.split('-')
begin,end = [int(x) for x in r]


ans_1= 0
ans_2= 0

def checkPwd(pwd):
    currDigit = 0
    for digit in pwd:
        if int(digit) < currDigit:
            return False
        currDigit = int(digit)
    c = {d:pwd.count(d) for d in pwd}
    return any([c[d] == 2 for d in c])

     


for pwd in range(begin,end):
    if checkPwd(str(pwd)):
        ans_2 += 1


print(f"SOLUTION FOR PART1: {ans_1}")
print(f"SOLUTION FOR PART2: {ans_2}")
