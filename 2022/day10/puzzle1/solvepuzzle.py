data = open('input.txt').readlines()
commands = [d.replace('\n', '') for d in data]

total_signal = current_cycle =  0
current_signal = 1
for command in commands:
    c = command.split()
    cycle_command = c[0]
    current_cycle += 1
    if (current_cycle+20) % 40 == 0:
        print(current_cycle)
        total_signal += current_signal * current_cycle
    if cycle_command != 'noop':
        current_cycle += 1
        if (current_cycle+20)%40==0:
            print(current_cycle)
            total_signal += current_signal * current_cycle
        current_signal += int(c[1])

print(total_signal)


