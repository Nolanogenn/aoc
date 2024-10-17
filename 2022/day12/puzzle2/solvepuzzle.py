from tqdm import tqdm 

data = open('input.txt').readlines()

class Point:
    def __init__(self, x=0, y=0, steps = 0, value='a'):
        self.x = x
        self.y = y
        self.steps = steps
        self.repr = ''.join([str(x), str(y)])
        self.value = value
    def __str__(self):
        return str((self.x, self.y, self.value))
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

grid = [list(d.replace('\n', '')) for d in data]
num_row = len(grid)
num_column = len(grid[0])

possible_starting_pos = []
ending_pos = Point()
for r, row in enumerate(grid):
    for c, cell in enumerate(row):
        if cell == 'a':
            possible_starting_pos.append(
                    Point(
                        x = r,
                        y = c,
                        value = 'a'
                        ))
        elif cell == 'E':
            ending_pos.x = r
            ending_pos.y = c
            ending_pos.value = 'E'


letters = ['S'] + [chr(n) for n in range(ord('a'), ord('z')+1)] + ['E']
def nextLetter(letter):
    i = letters.index(letter)
    if i < len(letters):
        return letters[i+1]
    else:
        return None


def get_neighbors(pos):
    neighbors = []
    nextletter = nextLetter(pos.value)
    if pos.x > 0: 
        #up
        neighbors.append(Point(x = pos.x-1, y=pos.y, value=grid[pos.x-1][pos.y]))
    if pos.y > 0:
        #left
        neighbors.append(Point(x=pos.x, y=pos.y-1, value=grid[pos.x][pos.y-1]))
    if pos.x < num_row-1:
        #right
        neighbors.append(Point(x=pos.x+1, y=pos.y, value=grid[pos.x+1][pos.y]))
    if pos.y < num_column-1:
        #down
        neighbors.append(Point(x=pos.x, y=pos.y+1, value=grid[pos.x][pos.y+1]))
    neighbors = [n for n in neighbors if letters.index(n.value)-letters.index(pos.value) <= 1]
    return neighbors

paths_to_e = []

min_steps = 999999
for point in tqdm(possible_starting_pos):
    queue = get_neighbors(point)
    visited = set()
    while len(queue) > 0:
        #print([(n.x, n.y, n.value, n.steps) for n in queue])
        point = queue[0]
        queue = queue[1:]
        steps = point.steps
        if point == ending_pos:
            min_steps = min(min_steps, steps+1)
            continue
        for neighbor in get_neighbors(point):
            if neighbor.repr not in visited:
                visited.add(neighbor.repr)
                neighbor.steps = steps + 1
                #print(neighbor.steps)
                queue.append(neighbor)
print(min_steps)
