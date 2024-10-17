import ast 

data = open('input.txt').read()
data = data.split('\n\n')

def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i+= 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i+1], array[high]) = (array[high], array[i+1])
    return i + 1

def quicksort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quicksort(array, low, pi-1)
        quicksort(array, pi + 1, high)


calories = []

for k in data:
    total = sum([int(x) for x in k.split('\n') if x.isnumeric() == True])
    calories.append(total)

calories = sorted(calories, reverse=True)
size = len(calories)
quicksort(calories, 0, size-1)
print(sum(calories[-3:]))

