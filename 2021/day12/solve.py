data = open('in').readlines()
data = [x.strip() for x in data]

ans_1= 0
ans_2= 0

network = {}
for line in data:
    start, end = line.split('-')
    if start not in network:
        network[start] = set()
    if end not in network:
        network[end] = set()
    network[start].add(end)
    network[end].add(start)
    

m={}
def continueSequence1(sequence,seen=set(),possible=[]):
    last=sequence[-1]
    if last == "end":
        possible.append(sequence)
    if ''.join(sequence) in m:
        possibleNext = m[''.join(sequence)]
    else:
        possibleNext=[x for x in network[last] if not x.islower() or x not in sequence]
        m[''.join(sequence)] = possibleNext
    for n in possibleNext:
        newSequence = sequence + [n]
        if ''.join(newSequence) not in seen:
            seen.add(''.join(newSequence))
            continueSequence1(newSequence, seen, possible)
    return possible

s=["start"]
ans_1 = len(continueSequence1(s))

m={}
def check(sequence):
    last = sequence[-1]
    xs = []
    for x in network[last]:
        good = True
        if not x.islower():
            xs.append(x)
        if x == 'start':
            good=False
        if x == 'end' and x in sequence:
            good=False
        l = [s for s in sequence if s.islower()]
        if x in l and any([l.count(x) > 1 for x in l]):
            good=False
        if good:
            xs.append(x)
    return xs

def continueSequence2(sequence,seen=set(),possible=[]):
    last=sequence[-1]
    if last == "end":
        possible.append(sequence)
    if ''.join(sequence) in m:
        possibleNext = m[''.join(sequence)]
    else:
        possibleNext = check(sequence)
        m[''.join(sequence)] = possibleNext
    for n in possibleNext:
        newSequence = sequence + [n]
        if ''.join(newSequence) not in seen:
            seen.add(''.join(newSequence))
            continueSequence2(newSequence, seen, possible)
    return possible

s=["start"]
ans_2 = len(continueSequence2(s))

print(f"SOLUTION FOR PART1: {ans_1}")
print(f"SOLUTION FOR PART2: {ans_2}")
