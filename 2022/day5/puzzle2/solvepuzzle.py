data = open('input.txt').readlines()

crates = [d.replace('\n', '') for d in data[:8]]
moves = [d.replace('\n', '') for d in data[10:]]
stacks = {x:[] for x in range(1,10)}

for crate in crates:
    for i, char in enumerate(crate[1::4], start=1):
        if char != ' ':
            stacks[i].insert(0, char)

for move in moves:
    compressed_move = [int(x) for x in move.split() if x.isnumeric()]
    movement, source, target = compressed_move
    tomove = []
    for m in range(movement):
        tomove.append(stacks[source].pop())
    for m in reversed(tomove):
        stacks[target].append(m)


for stack in stacks:
    print(stacks[stack][-1])
