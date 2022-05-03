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

# Поиск собственных векторов из задания 4
a = A[0][0]
b = A[0][1]
c = A[1][0]
d = A[1][1]

bb = -a - d
cc = a * d - c * b

disc = bb ** 2 - 4 * cc
if disc >= 0:
    l1 = (-bb + disc ** 0.5) / 2
    if l1.is_integer():
        l1 = int(l1)
    l2 = (-bb - disc ** 0.5) / 2
    if l2.is_integer():
        l2 = int(l2)
else:
    print('Нет рациональных корней')
    exit(0)

if a - l1 == b == c == d - l1 == 0:
    print('l = ', l1, ', собственный вектор любой')
else:
    if b == a - l1 == 0:
        u1 = [l1 - d, c]
    else:
        u1 = [-b, a - l1]
    if b == a - l2 == 0:
        u2 = [l2 - d, c]
    else:
        u2 = [-b, a - l2]
    for i in range(2):
        if u1[i].is_integer():
            u1[i] = int(u1[i])
        if u2[i].is_integer():
            u2[i] = int(u2[i])

v1 = u1[0]
v2 = u1[1]
w1 = u2[0]
w2 = u2[1]

# Ищем матрицу функционалов
B = [[v1, w1], [v2, w2]]
detB = v1 * w2 - w1 * v2
f1, f2 = w2 / detB, -w1 / detB
r1, r2 = -v2 / detB, v1 / detB

# Записываем матрицы проекторов
P1 = [[v1 * f1, v1 * f2], [v2 * f1, v2 * f2]]
P2 = [[w1 * r1, w1 * r2], [w2 * r1, w2 * r2]]

for i in range(2):
    for j in range(2):
        if P1[i][j].is_integer():
            P1[i][j] = int(P1[i][j])
        if P2[i][j].is_integer():
            P2[i][j] = int(P2[i][j])

print('Проектор для собственного числа l1 = ', l1, ': ')
for t in P1:
    print(t)
print('Проектор для собственного числа l2 = ', l2, ': ')
for t in P2:
    print(t)
