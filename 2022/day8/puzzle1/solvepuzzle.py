from pprint import pprint
import numpy as np

data = open('input.txt').readlines()

rows = [[int(x) for x in d.replace('\n', '')] for d in data]
columns = [[row[i] for row in rows] for i in range(len(rows[0]))] 
numCols = len(columns)
numRows = len(rows)
lenRow = len(rows[0])

visibleTrees = 0
matrixVisible = []
for i in range(numRows):
    row = rows[i]
    newRow = [0]*lenRow
    for j in range(numCols):
        column = columns[j]
        elem = row[j]
        if (i==0 or j==0) or (j==numRows-1 or i==numRows-1):
            newRow[j] = 1
            visibleTrees += 1
        else:
            maxWest = max(np.array(row[:j]))
            maxEast = max(np.array(row[j+1:]))
            maxNorth = max(np.array(column[:i]))
            maxSouth = max(np.array(column[i+1:]))

            toCheck = any(elem > x for x in [maxWest, maxEast, maxNorth, maxSouth])
            if toCheck:
                newRow[j] = 1
                visibleTrees += 1

    matrixVisible.append(newRow)

#pprint(matrixVisible[1])
print(visibleTrees)






