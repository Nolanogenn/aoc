import time

start_time = time.time()
data = open('input.txt').read()

buffer = []
for i, char in enumerate(data):
    if len(buffer) == 14:
        if len(set(buffer)) == 14:
            print(i)
            break
        else:
            buffer.pop(0)
    buffer.append(char)

print("--- %s seconds ---" % (time.time() - start_time))

