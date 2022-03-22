# Матрица А размера n*m
n = int(input('Сколько строк в матрице А? '))
print('Ввод матрицы А:')
A = [list(map(float, input().split())) for i in range(n)]
m = len(A[0])

# Проверка матрицы  А
for i in range(len(A)):
    if len(A[0]) != len(A[i]):
        print('Матрица некорректна')
        exit(0)

# Матрица В размера x*y
x = int(input('Сколько строк в матрице B? '))
print('Ввод матрицы В:')
B = [list(map(float, input().split())) for i in range(x)]
y = len(B[0])

# Проверка матрицы В
for i in range(len(B)):
    if len(B[0]) != len(B[i]):
        print('Матрица некорректна')
        exit(0)

# Пустые матрицы для сложения и умножения
Sum = [[0] * m for i in range(n)]
Multi = [[0] * y for i in range(n)]

# Сложение
print('Результат сложения:')
if n != x or m != y:
    print('Сложить нельзя!')
else:
    for i in range(len(A)):
        for j in range(len(A[0])):
            Sum[i][j] = A[i][j] + B[i][j]
            if Sum[i][j].is_integer():
                Sum[i][j] = int(Sum[i][j])
    for t in Sum:
        print(t)

# Умножение
print('Результат умножения:')
if m != x:
    print('Умножить нельзя')
else:
    for i in range(n):
        for j in range(y):
            for r in range(m):
                Multi[i][j] += A[i][r] * B[r][j]
            if Multi[i][j].is_integer():
                Multi[i][j] = int(Multi[i][j])
    for t in Multi:
        print(t)
