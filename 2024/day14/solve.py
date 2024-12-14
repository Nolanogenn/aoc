from consoledraw import Console
import time
import re

data = open('in').readlines()
guards = [x.strip().split(' ') for x in data]
guard_pos = [[int(y) for y in list(re.findall(r'[0-9]+', x[0]))][::-1] for x in guards]
guard_mov = [[int(y) for y in list(re.findall(r'[-0-9]+', x[1]))][::-1] for x in guards]

h = 102
w = 100
#h = 6
#w = 10

ans_1= 0
ans_2= 0

def move_guards(guard_pos, guard_mov, rounds):
    final_pos = []
    for guard_i in range(len(guard_pos)):
        pos = guard_pos[guard_i]
        mov = guard_mov[guard_i]
        for _ in range(rounds):
            newpos = [pos[0]+mov[0], pos[1]+mov[1]]
            if newpos[0] < 0:
                newpos[0] = h + newpos[0]+1
            if newpos[1] < 0:
                newpos[1] = w + newpos[1]+1
            if newpos[0] > h:
                newpos[0] = newpos[0]-h-1
            if newpos[1] > w:
                newpos[1] = newpos[1]-w-1
            pos = newpos
        final_pos.append(pos)
    return final_pos

s = ""
q1 = 0
q2 = 0
q3 = 0
q4 = 0

final_pos = move_guards(guard_pos, guard_mov, 100)
for i in range(h+1):
    l = ""
    for j in range(w+1):
        if [i,j] in final_pos:
            c = final_pos.count([i,j])
            if i < h/2 and j < w/2:
                q1 += c
            if i > h/2 and j < w/2:
                q3 += c
            if i > h/2 and j > w/2:
                q4 += c
            if i < h/2 and j > w/2:
                q2 += c
            l += f"{c}"
        else:
            l += '.'
    s += l
    s += "\n"
ans_1 = q1 * q2 * q3 * q4

seconds = 0
ans_2 = 0
pos = guard_pos
max_sec = 9999999999999
longest_line = 0
while True:
    pos = move_guards(pos, guard_mov,1)
#    q1 = sum([1 for x in pos if x[0]<=h/2 and x[1]<=w/2])
#    q2 = sum([1 for x in pos if x[0]<=h/2 and x[1]>=w/2])
#    q3 = sum([1 for x in pos if x[0]>=h/2 and x[1]<=w/2])
#    q4 = sum([1 for x in pos if x[0]>=h/2 and x[1]>=w/2])
#    curr_sec = q1 * q2 * q3 * q4
    max_current_line = 0
    for row in range(h):
        line = 0
        for column in range(w):
            if [row, column] in pos:
                line +=1
            else:
                if line > max_current_line:
                    max_current_line = line
                line = 0
    seconds +=1 
    if max_current_line > longest_line:
        s = ""
        for i in range(h+1):
            l = ""
            for j in range(w+1):
                if [i,j] in pos:
                    l += "@"
                else:
                    l += '.'
            s += l
            s += "\n"
            longest_line = max_current_line
            ans_2 = seconds
            with open(f"./imgs/{seconds}", "w+") as f:
                f.write(s)
    print(seconds, longest_line, end='\r', flush=True)
print(f"SOLUTION FOR PART1: {ans_1}")
print(f"SOLUTION FOR PART2: {ans_2}")
