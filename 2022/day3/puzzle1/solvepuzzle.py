data = open('input.txt').readlines()

def range_char(start, stop):
        return (chr(n) for n in range(ord(start), ord(stop) + 1))
lowercase= list(range_char('a', 'z'))
uppercase = list(range_char('A', 'Z'))
all_letters = lowercase+uppercase

list_values = list(range(1, 53))
value_items = {x:list_values[j] for j, x in enumerate(all_letters)}
total = 0
for line in data:
    line = line.replace('\n', '')
    y = len(line)
    break_ = int(y/2)
    i1 = line[:break_]
    i2 = line[break_:]
    common_item = [x for x in i1 if x in i2][0]
    value = value_items[common_item]
    total += value
print(total)
