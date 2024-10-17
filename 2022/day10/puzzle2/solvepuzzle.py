from pprint import pprint
data = open('input.txt').readlines()
commands_raw = [d.replace('\n', '') for d in data]
commands = []
for c in commands_raw:
    if 'addx' in c:
        commands.append('none')
    commands.append(c)

monitor = [[] for _ in range(6)]

current_cycle =  0
current_signal = 1
i=0

for command in commands:
    c = command.split()
    cycle_command = c[0]
    current_cycle += 1

    if ((current_cycle-1)%40) in [current_signal-1, current_signal, current_signal+1]:
        monitor[i].append('#')
    else:
        monitor[i].append('.')

    if current_cycle%40==0:
        i += 1
    if current_cycle == 240:
        break
    if cycle_command == 'addx':
        current_signal += int(c[1])
    


for line in monitor:
    print("".join(line))
