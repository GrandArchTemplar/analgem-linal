import sys
i1 = int(input('количество строк первой матрицы'))
j1 = int(input('количество столбцов первой матрицы'))
mat1 = [[0]*j1 for _ in range(i1)]
for i in range(i1):
    mat1[i] = input().split()
i2 = int(input('количество строк второй матрицы'))
j2 = int(input('количество столбцов второй матрицы'))
mat2 = [[0] * j2 for _ in range(i2)]
for i in range(i2):
    mat2[i] = input().split()
q = input('+ или *')
if q == '+':
    mat = [[0] * j1 for _ in range(i1)]
    if i1 == i2 and j1 == j2:
        for i in range(i1):
            for j in range(j1):
                mat[i][j] = int(mat1[i][j])+int(mat2[i][j])
    else: sys.exit()
if q == '*':
    mat = [[0] * j2 for _ in range(i1)]
    if j1 == i2:
        for i in range(i1):
            for j in range(j2):
                for k in range(j1):
                    mat[i][j] += int(mat1[i][k])*int(mat2[k][j])
    else: sys.exit()
for i in range(i1):
    print(mat[i])