data = open('in').readlines()
data = [x.strip() for x in data]

ans_1= 0
ans_2= 0

acc = 0
line = 0

ops = []
inLoop = False
while not inLoop:
    c = data[line]
    if line in ops:
        inLoop = True
        break
    else:
        ops.append(line)
    if c.startswith("nop"):
        line += 1
    elif c.startswith("acc"):
        _, op = c.split()
        if op.startswith('+'):
            acc += int(op[1:])
        elif op.startswith('-'):
            acc -= int(op[1:])
        line += 1
    elif c.startswith("jmp"):
        _, op = c.split()
        if op.startswith('+'):
            line += int(op[1:])
        elif op.startswith('-'):
            line -= int(op[1:])

ans_1 = acc

tocheck = [(data,0,0,[],False)]
while tocheck:
    currentState = tocheck[0]
    tocheck = tocheck[1:]
    data = currentState[0]
    line = currentState[1]
    acc = currentState[2]
    ops = currentState[3]
    changed = currentState[4]
    c = data[line]
    if not changed and c.startswith("nop"):
        newData = [x for x in data]
        newData[line] = newData[line].replace("nop", "jmp")
        tocheck.append((newData,line,acc,ops,True))
    if not changed and c.startswith("jmp"):
        newData = [x for x in data]
        newData[line] = newData[line].replace("jmp", "nop")
        tocheck.append((newData,line,acc,ops,True))
    print(acc, c, line)
    if c.startswith("nop"):
        line += 1
    else:
        _, op = c.split()
    if c.startswith("acc"):
        if op.startswith('+'):
            acc += int(op[1:])
        elif op.startswith('-'):
            acc -= int(op[1:])
        line += 1
    elif c.startswith("jmp"):
        if op.startswith('+'):
            line += int(op[1:])
        elif op.startswith('-'):
            line -= int(op[1:])
    if line in ops:
        print("EXITED BECAUSE OF LOOP")
    else:
        ops.append(line)
    if line >= len(data):
        ans_2 = acc
        break
    else:
        tocheck.append((data, line, acc, ops, changed))


print(f"SOLUTION FOR PART1: {ans_1}")
print(f"SOLUTION FOR PART2: {ans_2}")
