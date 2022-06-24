n = int(input("Введите количество векторов: "))

a = []
for i in range(n):
    print("Введите координаты вектора ", i + 1, " через пробелы:")
    a2 = input()
    a2 = a2.split()
    for j in range(len(a2)):
        a2[j] = float(a2[j])
    a.append(a2)
print("Ваша матрица (внутренние списки - строки): ", a)

def mult(a, b, n):
    m = 0
    for i in range(n):
        m = m + a[i] * b[i]
    return m

b = []
for i in range(n):
    if i == 0:
        b.append((a[0]))
    else:
        b2 = []
        s = []
        for p in range(n):
            s.append(0.0)
        for j in range(i):
            k = mult(a[i], b[j], n) / mult(b[j], b[j], n)
            new = []
            for t in range(n):
                new.append(b[j][t] * k)
            for l in range(n):
                s[l] = s[l] + new[l]
        for g in range(n):
            b2.append(a[i][g] - s[g])
        b.append(b2)
print('Ортоганализированная матрица: ', b)