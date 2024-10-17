from tqdm import tqdm
import re

data = open('input.txt').readlines()
pattern = r"Valve ([A-Z]*) has flow rate=([0-9]*); tunnel[s]* lead[s]* to valve[s]* ([A-Z, ]*)"

valves = {}
for line in data:
    values = re.findall(pattern, line)
    valve = values[0][0]
    flow_rate = int(values[0][1])
    connected_to = values[0][2].split(', ')
    valves[valve] = {
            'flow_rate' : flow_rate,
            'connected_to' : connected_to
            }
adj_matrix = []
list_valves = list(valves.keys())
for v in list_valves:
    adj_row = []
    for v2 in list_valves:
        if v2 in valves[v]['connected_to']:
            adj_row.append(1)
        else:
            adj_row.append(0)
    adj_matrix.append(adj_row)

def bfs(matrix, a, b):
    new_row = list(matrix[a])
    queue = [a] + [i for i,x in enumerate(matrix[a]) if x == 1]
    visited = [a]
    previous = {}
    while queue:
        previous[a] = None
        current = queue.pop(0)
        if current == b:
            path = [current]
            p = previous[current]
            while p != None:
                path.append(p)
                p = previous[p]
            return len(path)-1
            break
        neighbors = [i for i,x in enumerate(matrix[current]) if x == 1]
        for n in neighbors:
            if n not in visited:
                visited.append(n)
                previous[n] = current
                queue.append(n)

useful_valves = ['AA'] + [v for v in list_valves if valves[v]['flow_rate'] != 0]
bfs_valves = {}
for i, v in enumerate(list_valves):
    bfs_valves[v] = {}
    for i2, v2 in enumerate(list_valves):
        if v != v2:
            bfs_valves[v][v2] = bfs(adj_matrix, i, i2)

def find_best():
    best = 0
    def search(opened, released, current_valve,time_left, elephant):
        nonlocal best
        if released > best:
            best = released
        if time_left <= 0:
            return
        if current_valve not in opened:
            search(opened.union([current_valve]), released + valves[current_valve]['flow_rate'] * time_left, current_valve, time_left-1, elephant)
            if not elephant:
                search(set([current_valve]).union(opened), released + valves[current_valve]['flow_rate'] * time_left, 'AA', 25, True)
        else:
            for k in [x for x in bfs_valves[current_valve].keys() if x not in opened and x in useful_valves]:
                search(opened, released, k, time_left-bfs_valves[current_valve][k], elephant)
    search(set(['AA']), 0, 'AA', 25, False)
    print(best)

find_best()
