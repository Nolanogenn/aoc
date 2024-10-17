from tqdm import tqdm
data = open('input.txt').readlines()
to_parse = [d.replace('\n', '') for d in data]

m = to_parse[::7]
starting_items = [t.split(':')[1].split(', ') for t in to_parse[1::7]]
operations = [t.split(':')[1].split() for t in to_parse[2::7]]
test_divisible_by = [t.split(':')[1].split() for t in to_parse[3::7]]
if_true = [t.split(':')[1].split() for t in to_parse[4::7]]
if_false = [t.split(':')[1].split() for t in to_parse[5::7]]

monkeys = {
        m[i][:-1]:{
            'items' : [int(x) for x in starting_items[i]],
            'num_of_actions' : 0,
            'operation' : operations[i][-2:],
            'to_test' : int(test_divisible_by[i][-1:][0]),
            'if_true' : 'Monkey ' + if_true[i][-1],
            'if_false' : 'Monkey ' + if_false[i][-1]
            }
        for i in range(8)
    }
factors = [monkeys[x]['to_test'] for x in monkeys]
factor = 1
for f in factors:
    factor *= f
for num_round in tqdm(range(10000)):
    for monkey_name in monkeys:
        monkey = monkeys[monkey_name]
        while len(monkey['items']) != 0:
            item = monkey['items'].pop()
            monkey['num_of_actions'] += 1
            operation, value = monkey['operation']
            if value == 'old':
                value = int(item)
            else:
                value = int(value)
            if operation == '*':
                new_value = item * value
            else:
                new_value = item + value
            new_value = new_value%factor
            if new_value%monkey['to_test'] == 0:
               monkeys[monkey['if_true']]['items'].append(new_value)
            else:
                monkeys[monkey['if_false']]['items'].append(new_value)

num_of_actions = sorted([monkeys[m]['num_of_actions'] for m in monkeys], reverse=True)
total = num_of_actions[0] * num_of_actions[1]

print(monkeys)
print(total)
