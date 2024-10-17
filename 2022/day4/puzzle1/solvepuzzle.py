data = open('input.txt').readlines()

overlapping_pairs = 0
for line in data:
    pairs = line.replace('\n', '').split(',')
    pair1, pair2 = [int(x) for x in pairs[0].split('-')], [int(x) for x in pairs[1].split('-')]
    check1 = (pair1[0] <= pair2[0] and pair1[1] >= pair2[1])
    check2 = (pair2[0] <= pair1[0] and pair2[1] >= pair1[1])
    if check1 or check2:
        overlapping_pairs += 1

print(overlapping_pairs)
    

