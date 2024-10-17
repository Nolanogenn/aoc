data = open('input.txt').readlines()
def divide_chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

def range_char(start, stop):
        return (chr(n) for n in range(ord(start), ord(stop) + 1))
lowercase= list(range_char('a', 'z'))
uppercase = list(range_char('A', 'Z'))
all_letters = lowercase+uppercase

list_values = list(range(1, 53))
value_items = {x:list_values[j] for j, x in enumerate(all_letters)}
total = 0

chunks = divide_chunks(data, 3)
for chunk in chunks:
    l1 = chunk[0]
    l2 = chunk[1]
    l3 = chunk[2]

    common_item = [x for x in l1 if x in l2 and x in l3][0]
    value = value_items[common_item]
    total += value
print(total)
