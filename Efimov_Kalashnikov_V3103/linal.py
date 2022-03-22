a = []
b = list = []

print("Введите количество строк первой матрицы")
i = int(input())
ai1 = i
print("Введите количество элементов строки")
k = int(input())
ak1 = k


def vvod(i, a, b, k):
    h = 0
    for j in range(i):
        for u in range(k):
            b.append(float(input()))
        a.append(b)
        b = list = []
    return a


print("Введите элементы матрицы")
a1 = vvod(i, a, b, k)

a = []
b = list = []
print("Введите количество строк второй матрицы")
i = int(input())
ai2 = i
print("Введите количество элементов строки")
k = int(input())
ak2 = k

print("Введите элементы матрицы")
a2 = vvod(i, a, b, k)

print("Первая матрица")
print(a1)

print("Вторая матрица")
print(a2)

# сумматор

a0 = matrix = []
b = list = []
if ai1 == ai2 and ak1 == ak2:
    for i in range(ai1):
        for j in range(ak1):
            s = a1[i][j] + a2[i][j]
            b.append(s)
        a0.append(b)
        b = list = []
    print("Сумма:")
    print(a0)
else:
    print("Размеры матриц не совпадают")

if ak1 == ai2:
    a = []
    a22 = []
    i = 0
    b = list = []
    for j in range(ak2):
        for i in range(ai2):
            b.append(a2[i][j])
        a22.append(b)
        b = list = []
    s = 0
    for j in range(ai1):
        for h in range(ak2):
            for i in range(ak1):
                s = a1[j][i] * a22[h][i] + s
            b.append(s)
            s = 0
        a.append(b)
        b = list = []
    print("Произведение:")
    print(a)
else:
    print("Количество столбцов первой матрицы не совпадает с количеством строк второй матрицы")


