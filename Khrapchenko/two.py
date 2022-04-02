import copy


# Функция нахождения минора
def minor(a, i, j):
    m = copy.deepcopy(a)
    del m[i]
    for i in range(len(a[0]) - 1):
        del m[i][j]
    return m


# Функция нахождения определителя
def det(a):
    num = len(a[0])
    if num == 1:
        return a[0][0]
    sign = 1
    determinant = 0

    for j in range(num):
        determinant += a[0][j] * sign * det(minor(a, 0, j))
        sign *= -1
    return determinant


# Функция создания союзной  транспонированной матрицы
def adj(a):
    num = len(a)
    b = [[0] * num for i in range(num)]
    for i in range(num):
        for j in range(num):
            b[i][j] = det(minor(a, j, i)) * (-1) ** (i + j)
    return b


# Матрица А размера n*n
n = int(input('Какой размер матрицы А? '))
print('Ввод матрицы А:')
A = [list(map(float, input().split())) for i in range(n)]
m = len(A[0])

# Проверка матрицы  А
for i in range(len(A)):
    if m != n or m != len(A[i]):
        print('Матрица некорректна')
        exit(0)

d = det(A)

if d == 0:
    print('Определитель равен нулю!')
    exit(0)

B = adj(A)
# Делим на определитель А и выводим результат
print('Обратная матрица: ')
for x in range(n):
    for y in range(n):
        B[x][y] = B[x][y] / d
        if B[x][y].is_integer():
            B[x][y] = int(B[x][y])

for t in B:
    print(t)
