import ast 

data = open('input.txt').read()
data = data.split('\n\n')

maxValue = 0
for k in data:
    print(k)
    total = sum([int(x) for x in k.split('\n') if x.isnumeric() == True])
    if total > maxValue:
        maxValue = total
    print('--')

print(maxValue)
