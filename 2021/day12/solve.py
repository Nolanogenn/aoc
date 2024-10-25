data = open('test').readlines()
data = [x.strip() for x in data]

ans_1= 0
ans_2= 0

network = {}
for line in data:
    start, end = line.split('-')
    if start not in network:
        network[start] = []
    network[start].append(end)

current="start"
seen=[current]
paths=set()

while current != "end":
    n = network[current]
    print(n)
    break
    






print(f"SOLUTION FOR PART1: {ans_1}")
print(f"SOLUTION FOR PART2: {ans_2}")
