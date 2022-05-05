strok = (int(input('Введите количество строк ')))
alim = (int(input("Введите количество элементов в строке ")))
Matrix = []  # матрица
s = 0  # счетчик строк
c = 0  # счетчик элементов в строке
while s < strok:  # создает строки
    a = []
    c = 0
    p = 0
    if s > 0:
        print("Cледующая строка ")
    while c < alim:  # элементы в строках
        p = float(input("Введите число в строке "))
        a.insert(c, p)
        c += 1
    s += 1
    Matrix.insert(s, a)
print(Matrix)
print("Вторая матрица ")
strok2 = (int(input('Введите количество строк ')))
alim2 = (int(input("Введите количество элементов в строке ")))
Matrix2 = []  # матрица
s2 = 0  # счетчик строк
c2 = 0  # счетчик элементов в строке
while s2 < strok2:  # создает строки
    a2 = []
    c2 = 0
    i2 = 0
    if s2 > 0:
        print("Cледующая строка ")
    while c2 < alim2:  # элементы в строках
        i2 = float(input("Введите число в строке "))
        a2.insert(c2, i2)
        c2 += 1
    s2 += 1
    Matrix2.insert(s2, a2)
print(Matrix2)
gav = int(input("Введите 1 чтобы сложить матрицы, 2 чтобы умножить "))
if gav == 1:
    end = []  # итоговая матрица
    en = []  # строка в итоговой матрице
    u = 0
    o = 0
    if alim != alim2 or strok != strok2:
        print("Матрицы не сложить, матрицы должны быть одинаковых размеров (((")
    else:
        for k in range(0, strok):
            en = []
            for h in range(0, alim):
              w = Matrix[k][h] + Matrix2[k][h]
              en.insert(o, w)
              o += 1
            end.insert(u, en)
            u += 1  # считаем потому что можем
    print(end)
else:
    if alim != strok2:
        print("Матрицы не умножить количество столбцов в первой матрице должно ровняться количесвту строк во второй ")
    else:
        END = [[0 for i in range(alim2)] for i in range(strok)]
        for i in range(strok):
            for j in range(alim2):
                for k in range(alim):
                    END[i][j] += Matrix[i][k] * Matrix2[k][j]
        print(END)






