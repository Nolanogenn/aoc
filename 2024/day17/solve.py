data = open('in').read()
regis, program = data.split('\n\n')

def xor(a,b):
    res = b''
    for i, _ in enumerate(a):
        checka = a[i]
        checkb = b[i]
        print(checka, checkb)
        if (checka and not checkb) or (not checka and checkb):
            res += b'1'
        else:
            res += b'0' 
    return res

def get_combo(v):
    if v == 7:
        raise Exception('7 should never appear')
    if v <= 3:
        return v
    return registers[operators[v]]

operators = {
        4 : 'A',
        5 : 'B',
        6 : 'C'
        }

registers = {'A':0, 'B':0, 'C':0}
for line in regis.split('\n'):
    l = line.split()
    registers[l[1][:-1]] =  int(l[-1])
program = program.split()[-1].split(',')

def do_action(i, program, register, operators):
    a = int(program[i])
    o = int(program[i+1])
    if a == 0:
        denom = 2**get_combo(o)
        register['A'] = register['A'] // denom
        return program, register, operators,i
    if a == 1:
        v1 = register['B']
        v2 = int(o)
        register['B'] = v1 ^ v2
        return program, register, operators,i
    if a == 2:
        v1 = get_combo(o)
        register['B'] = v1 % 8
        return program, register, operators,i
    if a == 3:
        if register['A'] == 0:
            return program, register, operators,i
        else:
            return do_action(o, program, register, operators)
    if a == 4:
        v1 = register['B']
        v2 = register['C']
        register['B'] = v1^v2
        return program, register, operators,i
    if a == 5:
        out.append(get_combo(o) % 8)
        return program, register, operators,i
    if a == 6:
        num = register['A']
        denom = 2**get_combo(o)
        register['B'] = num // denom
        return program, register, operators,i
    if a == 7:
        num = register['A']
        denom = 2**get_combo(o)
        register['C'] = num // denom
        return program, register, operators,i

out = []
i = 0
while i < len(program):
    program, registers, operators,j = do_action(i, program, registers, operators)
    i = j+2
           
ans_1= ','.join([str(x) for x in out])
ans_2 = 0

######## PART 2

possible_programs = ['']
for j in range(len(program)):
    curr_program = program[-j-1:]
    toadd = []
    for i in range(8):
        s = "{0:03b}".format(i)
        tocheck = list(possible_programs)
        while tocheck:
            current_a = tocheck.pop()
            a = int(current_a+s,2)
            k = 0
            out = []
            registers = {'A':a, 'B' : 0, 'C' : 0}
            while k < len(program):
                program,registers, operators,x = do_action(k, program, registers, operators)
                k = x+2
            out = [str(num) for num in out]
            if out == curr_program:
                new_a = "{0:03b}".format(a)
                toadd.append(new_a)
    possible_programs = toadd

possible_programs = sorted([int(x,2) for x in possible_programs])
ans_2 = possible_programs[0]
registers = {'A':ans_2, 'B':0, 'C':0}
out = []
i = 0
while i < len(program):
    program, registers, operators,j = do_action(i, program, registers, operators)
    i = j+2
out = [str(x) for x in out]
print(f"OUT:\t{out}")
print(f"PRG:\t{program}")
print(f"SOLUTION FOR PART1: {ans_1}")
print(f"SOLUTION FOR PART2: {ans_2}")
