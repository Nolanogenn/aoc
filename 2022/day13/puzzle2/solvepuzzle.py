import ast

data = open('input.txt').read().split('\n\n')
data = [d.split('\n') for d in data]
elems = []
for p in data:
    p1 = eval(p[0])
    p2 = eval(p[1])
    elems.append(p1)
    elems.append(p2)

decoder1 = [[2]]
decoder2 = [[6]]

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

i_decoder1 = 1
i_decoder2 = 2 #it always beats decoder1

for elem in elems:
    if compare(elem, decoder1) > 0:
        i_decoder1 += 1
        i_decoder2 += 1
    elif compare(elem, decoder2) > 0:
        i_decoder2 += 1

print(i_decoder1 *  i_decoder2)
