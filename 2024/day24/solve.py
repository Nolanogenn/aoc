from collections import defaultdict
def parse_gates(g):
    f, o = g.split(' -> ')
    arg1, op, arg2 = f.split(' ')
    return (arg1,arg2,op,o)

data = open('in').read()
inputs, gates = data.split('\n\n')
gates = [parse_gates(g) for g in gates.strip().split('\n')]
inputs = [x.strip().split(':') for x in inputs.split('\n')]
wires = {x[0]:int(x[1]) for x in inputs}

def solve(wires,gates=gates):
    seen = set()
    while len(seen) != len(wires):
        for wire in [x for x in wires.keys() if x not in seen]:
            seen.add(wire)
            fs = [g for g in gates if g[0] == wire and g[1] in wires or g[1] == wire and g[0] in wires]
            for f in fs:
                if f[2] == 'OR':
                    wires[f[3]] = wires[f[0]] or wires[f[1]]
                elif f[2] == 'AND':
                    wires[f[3]] = wires[f[0]] and wires[f[1]]
                else:
                    wires[f[3]] = wires[f[0]] ^ wires[f[1]]
    ret = sorted(wires.items(),key= lambda x:x[0],reverse=True)
    return int(''.join([str(x[1]) for x in ret if x[0].startswith('z')]),2)

ans_1 = solve(wires)
#the following code finds the bits where faults lie, once they are found I manually looked at the operations and compare them to an actual full adder
for k in range(45):
    curr_n = int('1'+'0'*k,2)
    if k < 10:
        x = f'x0{k}'
        y = f'y0{k}'
    else:
        x = f'x{k}'
        y = f'x{k}'
    tmp_wires = {j:1 if j in [x] else 0 for j in wires}
    ans = solve(tmp_wires)
    if ans != curr_n:
        if k < 10:
            z_to_check = f'z0{k}'
        else:
            z_to_check = f'z{k}'
        print(z_to_check, "is: ", ans, "~ should be: ", curr_n)

ans_2= "I know it in my heart lmao"


print(f"SOLUTION FOR PART1: {ans_1}")
print(f"SOLUTION FOR PART2: {ans_2}")
