import ast

data = open('input.txt').read().split('\n\n')
pairs = [d.split('\n') for d in data]

def compare(elem1, elem2):
    if type(elem1) == type(elem2) == int:
        return elem2 - elem1
    if type(elem1) == list and type(elem2) == int:
        elem2 = [elem2]
    if type(elem1) == int and type(elem2) == list:
        elem1 = [elem1]
    for a, b in zip(elem1, elem2):
        t = compare(a,b)
        if t != 0:
            return t
    return len(elem2) - len(elem1)

sum_correct = 0
for i, pair in enumerate(pairs, start=1):
    correct = True
    p1 = eval(pair[0])
    p2 = eval(pair[1])
    if compare(p1, p2) > 0:
        sum_correct += i
print(sum_correct)
    


        
