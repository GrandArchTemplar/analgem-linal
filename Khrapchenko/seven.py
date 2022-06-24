# Скалярное произведение и проекция
def dot_product(u, v):
    res = 0
    for i in range(len(v)):
        res += u[i] * v[i]
    return res


# Считываем два вектора
n = int(input('Сколько будет векторов? '))
print('Ввод векторов')
V = [list(map(float, input().split())) for i in range(n)]
m = len(V[0])

# Проверка на длины векторов
for i in range(n):
    if m != n or m != n:
        print('Ввод некорректный')
        exit(0)

# Ортогонализация
Ort = [[V[j][i] for i in range(len(V))]for j in range(len(V))]
for i in range(1, n):
    for j in range(0, i):
        proj = [i for i in range(m)]
        for n in range(m):
            proj[n] = (dot_product(V[j], Ort[i]) / dot_product(V[j], V[j])) * V[j][n]
        for n in range(m):
            Ort[i][n] -= proj[n]
for k in Ort:
    print(k)
