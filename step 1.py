row = int(input("Введите количество строк в первой матрице:"))
column = int(input("Введите количество столбцов в первой матрице:"))
A = []
print("Введите данные по строкам слева направо:")
for i in range(row):
    a = []
    for j in range(column):
        a.append(float(input()))
    A.append(a)
row2 = int(input("Введите количество строк во второй матрице:"))
column2 = int(input("Введите количество столбцов во второй матрице:"))
B = []
print("Введите данные по строкам слева направо:")
for i in range(row2):
    b = []
    for j in range(column2):
        b.append(float(input()))  
    B.append(b)
print(" ")
for i in range(row):
    for j in range(column):
        print(A[i][j], end=" ")
    print()
print(" ")
for i in range(row2):
    for j in range(column2):
        print(B[i][j], end=" ")
    print()
C = []
znak = int(input("введите тип операции: 1 - сложение, 2 - умножение"))
if znak == 1:
    if row != row2 and column != column2:
        print("error - разные размерности матриц")
    else:
        for i in range(row):
            c = []
            for j in range(column):
                c.append(0)
            C.append(c)
        for i in range(row):
            for k in range(column):
                C[i][k] = A[i][k] + B[i][k]
        for i in range(row):
            for j in range(column):
                print(C[i][j], end=" ")
            print()
if znak == 2:
    if column != row2:
        print("error - умножение невозможно")
    else:
        for z in range(row):
            t = []
            s = 0
            for j in range(column2):
                for i in range(column):
                    s = s + A[z][i] * B[i][j]
                t.append(s)
                s = 0
            C.append(t)
            t = []
        for i in range(row):
            for j in range(column2):
                print(C[i][j], end=" ")
            print()