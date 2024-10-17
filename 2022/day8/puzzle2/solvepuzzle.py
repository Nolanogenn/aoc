from pprint import pprint

data = open('input.txt').readlines()

rows = [[int(x) for x in d.replace('\n', '')] for d in data]
columns = [[row[i] for row in rows] for i in range(len(rows[0]))] 
numCols = len(columns)
numRows = len(rows)
lenRow = len(rows[0])
lenCol = len(columns[0])

highestScore = 0
for i in range(numRows):
    row = rows[i]
    for j in range(numCols):
        if (i != 0 and j != 0) and (i!=98 and j != 98):
            column = columns[j]
            elem = row[j]
            u = d = l = r = 0
            for up in range(i-1, -1, -1):
                u += 1
                if elem <= rows[up][j]:
                    break
            for down in range(i+1, lenCol, 1):
                d += 1
                if elem <= rows[down][j]:
                    break
            for left in range(j-1, -1, -1):
                l += 1
                if elem <= row[left]:
                    break
            for right in range(j+1, lenRow, 1):
                r += 1
                if elem <= row[right]:
                    break
            score = u*d*r*l

            if score > highestScore:
                highestScore = score


print(highestScore)






