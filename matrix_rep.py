row = int(input())
matrix = []
res = []

for i in range(row):
    mat = list(map(int, input().split()))
    column = len(mat)
    matrix.append(mat)

for r in range(row):
    for c in range(column):

        if(c < column-3):
            if(matrix[r][c] == matrix[r][c+1] == matrix[r][c+2] == matrix[r][c+3]):
                res.append(matrix[r][c])
        
        if(r < row-3):
            if(matrix[r][c] == matrix[r+1][c] == matrix[r+2][c] == matrix[r+3][c]):
                res.append(matrix[r][c])

        if(c < column-3 and r >= 3):
            if(matrix[r][c] == matrix[r-1][c+1] == matrix[r-2][c+2] == matrix[r-3][c+3]):
                res.append(matrix[r][c])

        if(c >= 3 and r >= 3):
            if(matrix[r][c] == matrix[r-1][c-1] == matrix[r-2][c-2] == matrix[r-3][c-3]):
                res.append(matrix[r][c])

print(list(set(res)))
