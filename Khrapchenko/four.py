# Матрица А размера 2*2
n = 2
print('Ввод матрицы А:')
A = [list(map(float, input().split())) for i in range(2)]
m = len(A[0])

# Проверка матрицы  А
for i in range(len(A)):
    if m != n or m != len(A[i]):
        print('Матрица некорректна')
        exit(0)

# Складываем элементы матрицы в переменные a, b, c, d
a = A[0][0]
b = A[0][1]
c = A[1][0]
d = A[1][1]

# Коэффициенты характеристического уравнения bb, cc
bb = -a - d
cc = a * d - c * b

# Решаем характеристическое уравнение det(A-l*I)=0
disc = bb ** 2 - 4 * cc
if disc >= 0:
    l1 = (-bb + disc ** 0.5)/2
    if l1.is_integer():
        l1 = int(l1)
    l2 = (-bb - disc ** 0.5)/2
    if l2.is_integer():
        l2 = int(l2)
else:
    print('Нет рациональных корней')
    exit(0)

# Ищем собственный векторы и выводим результат
if a - l1 == b == c == d - l1 == 0:
    print('l = ', l1, ', собственный вектор любой')
else:
    if b == a-l1 == 0:
        u1 = [l1-d, c]
    else:
        u1 = [-b, a-l1]
    if b == a-l2 == 0:
        u2 = [l2-d, c]
    else:
        u2 = [-b, a-l2]
    for i in range(2):
        if u1[i].is_integer():
            u1[i] = int(u1[i])
        if u2[i].is_integer():
            u2[i] = int(u2[i])
    if l1 != l2:
        print('l1 = ', l1, ', u1 = ', u1)
        print('l2 = ', l2, ', u2 = ', u2)
    else:
        print('l = ', l1, ', u = ', u1)
