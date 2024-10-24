data = open('in').readlines()

ans_1=0
ans_2 = 0
m={
    'abcefg' : 0,
    'cf' : 1, 
    'acdeg' : 2,
    'acdfg' : 3,
    'bcdf' : 4,
    'abdfg' : 5,
    'abdefg' : 6, 
    'acf' : 7,
    'abcdefg' : 8,
    'abcdfg':9
   }
for line in data:
    m = {1:'', 2:'', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9 :'', 0:''}
    d_i = line.strip().split(' | ')[0].split()
    d_i_s = sorted(d_i, key=lambda x: len(x))
    d_o = line.strip().split(' | ')[1].split()
    x = len([x for x in d_o if len(x) in [2,4,3,7]])
    ans_1 += x
    
    m[1] = d_i_s[0]
    m[4] = d_i_s[2]
    m[7] = d_i_s[1]
    m[8] = d_i_s[-1]
    m[3] = [x for x in d_i_s if len(x) == 5 and all([j in x for j in m[7]])][0]
    m[9] = [x for x in d_i_s if len(x) == 6 and all([j in x for j in m[4]])][0]

    for k in d_i_s:
        if k != m[3] and len(k) == 5: #possible: 2, 5
            discr = len([x for x in m[4] if x not in k])
            if discr == 1:
                m[5] = k
            else:
                m[2] = k
        elif k != m[9] and len(k) == 6: #possible: 0, 6
            discr = len([x for x in m[5] if x not in k])
            if discr == 1:
                m[0] = k
            else:
                m[6] = k
    solver = {m[k]:k for k in m}
    digit = ''
    for w in d_o:
        for j in solver:
            if all([c in j for c in w]) and all([c in w for c in j]):
                digit+= str(solver[j])
                break

    ans_2 += int(digit)

print(ans_1)
print(ans_2)
